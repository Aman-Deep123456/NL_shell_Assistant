# intent_definitions.py
from enum import Enum, auto

class Intent(Enum):
    CREATE_FILE = auto()
    CREATE_FOLDER = auto()
    OPEN_FILE = auto()
    DELETE_FILE = auto()
    DELETE_FOLDER = auto()
    MOVE_FILE = auto()
    COPY_FILE = auto()
    RENAME_FILE = auto()
    READ_FILE = auto()
    WRITE_FILE = auto()
    LIST_FILES = auto()
    SHOW_DATE = auto()
    SHOW_TIME = auto()
    SHOW_DIR = auto()
    SHOW_PROCESSES = auto()
    SHOW_DISK_USAGE = auto()
    SEARCH_FILE = auto()
    SEARCH_TEXT = auto()
    PING_HOST = auto()
    SHOW_IP = auto()
    RUN_SCRIPT = auto()
    PYTHON_VERSION = auto()
    EXIT = auto()
    HELP = auto()
    UNKNOWN = auto()

INTENT_SYNONYMS = {
    Intent.CREATE_FILE: [
        "make file", "create file", "new file", "add file", "generate file",
        "touch file", "build file", "spawn file", "construct file", "start file"
    ],
    Intent.CREATE_FOLDER: [
        "make folder", "create folder", "make directory", "create directory", "mkdir",
        "new folder", "new directory", "add folder", "build folder"
    ],
    Intent.OPEN_FILE: [
        "open file", "launch file", "display file", "view file", "show file", "access file"
    ],
    Intent.DELETE_FILE: [
        "delete file", "remove file", "erase file", "trash file", "discard file", "destroy file"
    ],
    Intent.DELETE_FOLDER: [
        "delete folder", "remove folder", "delete directory", "remove directory"
    ],
    Intent.MOVE_FILE: [
        "move file", "relocate file", "transfer file", "shift file", "place file"
    ],
    Intent.COPY_FILE: [
        "copy file", "duplicate file", "clone file", "replicate file"
    ],
    Intent.RENAME_FILE: [
        "rename file", "change filename", "edit filename"
    ],
    Intent.READ_FILE: [
        "read file", "show contents", "view contents", "display contents", "print file"
    ],
    Intent.WRITE_FILE: [
        "write file", "append file", "update file", "edit file", "save file"
    ],
    Intent.LIST_FILES: [
        "list files", "show files", "display files", "show directory contents", "show folders"
    ],
    Intent.SHOW_DATE: [
        "show date", "what's the date", "current date", "today's date", "tell date"
    ],
    Intent.SHOW_TIME: [
        "show time", "current time", "what time is it", "clock", "now time"
    ],
    Intent.SHOW_DIR: [
        "where am i", "show current directory", "pwd", "current path"
    ],
    Intent.SHOW_PROCESSES: [
        "show processes", "list processes", "running tasks", "process list", "task list"
    ],
    Intent.SHOW_DISK_USAGE: [
        "show disk usage", "disk space", "memory usage", "storage info", "df", "system storage"
    ],
    Intent.SEARCH_FILE: [
        "find file", "locate file", "search file", "look for file", "grep file"
    ],
    Intent.SEARCH_TEXT: [
        "search for", "find text", "look for", "grep for"
    ],
    Intent.PING_HOST: [
        "ping", "test connection", "check connection", "network test"
    ],
    Intent.SHOW_IP: [
        "show ip", "what is my ip", "my ip address", "display ip"
    ],
    Intent.RUN_SCRIPT: [
        "run script", "execute file", "start program", "launch script"
    ],
    Intent.PYTHON_VERSION: [
        "python version", "show python version", "check python version"
    ],
    Intent.HELP: [
        "help", "commands", "manual", "guide", "show help", "usage"
    ],
    Intent.EXIT: [
        "exit", "quit", "close", "stop", "terminate", "end session"
    ]
}
