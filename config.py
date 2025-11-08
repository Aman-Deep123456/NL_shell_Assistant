
from pathlib import Path
from typing import Final
import sys

PROJECT_ROOT: Final[Path] = Path(__file__).resolve().parent
SANDBOX_ROOT: Final[Path] = PROJECT_ROOT  # restrict operations to project dir

BANNED_SUBSTRINGS = [
    "rm -rf",
    "sudo",
    ":(){:|:&};:",
    "mkfs",
    "dd if=",
]

DEFAULT_OPEN_CMD = {
    "linux": "xdg-open",
    "darwin": "open",
    "win32": "start",
}
PLATFORM = sys.platform
VOICE_ENABLED = True  # set False to disable voice mode
