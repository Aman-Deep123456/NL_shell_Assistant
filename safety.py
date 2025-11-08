from pathlib import Path
from typing import Final
from config import SANDBOX_ROOT, BANNED_SUBSTRINGS
from logger import get_logger

logger = get_logger(__name__)

def is_safe_command(raw: str) -> bool:
    if raw is None:
        return True
    lowered = raw.lower()
    for s in BANNED_SUBSTRINGS:
        if s in lowered:
            logger.warning("Blocked substring found in command: %s", s)
            return False
    return True

def normalize_and_validate_path(path_like: str) -> Path:
    p = Path(path_like).expanduser().resolve()
    sandbox = SANDBOX_ROOT.resolve()
    # allow sandbox itself or anything inside
    if p != sandbox and sandbox not in p.parents:
        logger.error("Attempted access outside sandbox: %s", p)
        raise ValueError("Access to paths outside the project directory is blocked.")
    return p
