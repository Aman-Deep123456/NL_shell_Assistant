
from pathlib import Path
import subprocess
import shutil
import os
import datetime
import socket

from parser import Action
from intent_definitions import Intent
from safety import is_safe_command, normalize_and_validate_path
from config import DEFAULT_OPEN_CMD, PLATFORM
from logger import get_logger

logger = get_logger(__name__)


def execute(action: Action):
    

    if action.raw and not is_safe_command(action.raw):
        return False, "🚫 Command blocked by safety rules."

    try:
        intent = action.intent
        logger.info(f"Executing intent: {intent}, src={action.src}, dst={action.dst}")

        # ---------------------------------------------------------
        # FILE CREATION
        # ---------------------------------------------------------
        if intent == Intent.CREATE_FILE:
            if not action.src:
                return False, "Please specify a file name."
            path = normalize_and_validate_path(action.src)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch(exist_ok=True)
            return True, f"✅ Created file: {path.name}"

 
        if intent == Intent.CREATE_FOLDER:
            if not action.src:
                return False, "Please specify a folder name."
            path = normalize_and_validate_path(action.src)
            path.mkdir(parents=True, exist_ok=True)
            return True, f"📁 Created folder: {path}"

        
        if intent == Intent.OPEN_FILE:
            if not action.src:
                return False, "Please specify a file to open."
            path = normalize_and_validate_path(action.src)
            if not path.exists():
                return False, f"File not found: {path}"
            cmd = DEFAULT_OPEN_CMD.get(PLATFORM, "open")
            subprocess.Popen([cmd, str(path)], shell=False)
            return True, f"📂 Opened {path.name}"

        # ---------------------------------------------------------
        # DELETE FILE / FOLDER
        # ---------------------------------------------------------
        if intent in [Intent.DELETE_FILE, Intent.DELETE_FOLDER]:
            if not action.src:
                return False, "Please specify a file or folder to delete."
            path = normalize_and_validate_path(action.src)
            if not path.exists():
                return False, f"Target not found: {path}"
            if path.is_dir():
                shutil.rmtree(path)
                return True, f"🗑️ Deleted folder: {path}"
            else:
                path.unlink()
                return True, f"🗑️ Deleted file: {path}"

        # ---------------------------------------------------------
        # MOVE FILE
        # ---------------------------------------------------------
        if intent == Intent.MOVE_FILE:
            if not action.src or not action.dst:
                return False, "Usage: move file <src> to <dst>"
            src = normalize_and_validate_path(action.src)
            dst = normalize_and_validate_path(action.dst)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(src), str(dst))
            return True, f"📦 Moved {src} → {dst}"

        # ---------------------------------------------------------
        # COPY FILE
        # ---------------------------------------------------------
        if intent == Intent.COPY_FILE:
            if not action.src or not action.dst:
                return False, "Usage: copy file <src> to <dst>"
            src = normalize_and_validate_path(action.src)
            dst = normalize_and_validate_path(action.dst)
            dst.parent.mkdir(parents=True, exist_ok=True)
            if src.is_dir():
                shutil.copytree(src, dst, dirs_exist_ok=True)
            else:
                shutil.copy2(src, dst)
            return True, f"📋 Copied {src} → {dst}"

        # ---------------------------------------------------------
        # RENAME FILE
        # ---------------------------------------------------------
        if intent == Intent.RENAME_FILE:
            if not action.src or not action.dst:
                return False, "Usage: rename file <src> to <dst>"
            src = normalize_and_validate_path(action.src)
            dst = normalize_and_validate_path(action.dst)
            src.rename(dst)
            return True, f"✏️ Renamed {src.name} → {dst.name}"

        # ---------------------------------------------------------
        # READ FILE
        # ---------------------------------------------------------
        if intent == Intent.READ_FILE:
            if not action.src:
                return False, "Please specify a file to read."
            path = normalize_and_validate_path(action.src)
            if not path.exists():
                return False, f"File not found: {path}"
            with open(path, "r", encoding="utf-8") as f:
                data = f.read()
            return True, f"📖 Contents of {path.name}:\n\n{data or '(empty file)'}"

        # ---------------------------------------------------------
        # WRITE / APPEND TO FILE
        # ---------------------------------------------------------
        if intent == Intent.WRITE_FILE:
            if not action.src:
                return False, "Please specify a file to write to."
            path = normalize_and_validate_path(action.src)
            text = input("Enter text to write: ")
            with open(path, "a", encoding="utf-8") as f:
                f.write(text + "\n")
            return True, f"✍️ Written to {path}"

        # ---------------------------------------------------------
        # LIST FILES
        # ---------------------------------------------------------
        if intent == Intent.LIST_FILES:
            files = [p.name for p in Path(".").iterdir()]
            return True, "📂 Files:\n" + "\n".join(files)

        # ---------------------------------------------------------
        # SHOW DATE / TIME / DIRECTORY
        # ---------------------------------------------------------
        if intent == Intent.SHOW_DATE:
            return True, f"📅 Today's date: {datetime.date.today()}"

        if intent == Intent.SHOW_TIME:
            return True, f"⏰ Current time: {datetime.datetime.now().strftime('%H:%M:%S')}"

        if intent == Intent.SHOW_DIR:
            return True, f"📁 Current directory: {os.getcwd()}"

        # ---------------------------------------------------------
        # SYSTEM INFO
        # ---------------------------------------------------------
        if intent == Intent.SHOW_PROCESSES:
            out = subprocess.check_output(["ps", "aux"]).decode("utf-8")
            return True, out[:1000] + "\n...(trimmed)..."

        if intent == Intent.SHOW_DISK_USAGE:
            out = subprocess.check_output(["df", "-h"]).decode("utf-8")
            return True, out

        # ---------------------------------------------------------
        # SEARCH
        # ---------------------------------------------------------
        if intent == Intent.SEARCH_FILE:
            if not action.src:
                return False, "Please specify a file name to search for."
            matches = [str(p) for p in Path(".").rglob(action.src)]
            return True, "\n".join(matches) if matches else "No matching files found."

        if intent == Intent.SEARCH_TEXT:
            if not action.src:
                return False, "Please specify text to search for."
            found = []
            for p in Path(".").rglob("*.*"):
                try:
                    if action.src in p.read_text():
                        found.append(str(p))
                except Exception:
                    pass
            return True, "\n".join(found) if found else "No text matches found."

        # ---------------------------------------------------------
        # NETWORK COMMANDS
        # ---------------------------------------------------------
        if intent == Intent.PING_HOST:
            host = action.src or "google.com"
            out = subprocess.run(["ping", "-c", "2", host], capture_output=True, text=True)
            return True, out.stdout or out.stderr

        if intent == Intent.SHOW_IP:
            ip = socket.gethostbyname(socket.gethostname())
            return True, f"🌐 Your IP address: {ip}"

        # ---------------------------------------------------------
        # PYTHON / DEV TOOLS
        # ---------------------------------------------------------
        if intent == Intent.PYTHON_VERSION:
            out = subprocess.check_output(["python3", "--version"]).decode("utf-8")
            return True, f"🐍 Python version: {out.strip()}"

        if intent == Intent.RUN_SCRIPT:
            if not action.src:
                return False, "Please specify a Python script to run."
            out = subprocess.run(["python3", action.src], capture_output=True, text=True)
            return True, out.stdout or out.stderr

        # ---------------------------------------------------------
        # HELP / EXIT
        # ---------------------------------------------------------
        if intent == Intent.HELP:
            return True, (
                "🧠 Available commands:\n"
                "- make file <name>\n"
                "- make folder <name>\n"
                "- open file <name>\n"
                "- delete file/folder <name>\n"
                "- move/copy/rename file <src> to <dst>\n"
                "- read file <name>\n"
                "- write to file <name>\n"
                "- show date/time/directory\n"
                "- search for <text> or find file <name>\n"
                "- ping <host>, show ip\n"
                "- run script <file>, show python version\n"
                "- exit / quit"
            )

        if intent == Intent.EXIT:
            print("👋 Goodbye!")
            exit(0)

        # ---------------------------------------------------------
        # UNKNOWN INTENT
        # ---------------------------------------------------------
        return False, "❓ I didn't understand that command."

    except Exception as e:
        logger.exception("Error executing intent.")
        return False, f"❌ Execution failed: {e}"
