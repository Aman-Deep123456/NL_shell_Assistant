import re
from difflib import SequenceMatcher
from intent_definitions import Intent, INTENT_SYNONYMS
from dataclasses import dataclass
from logger import get_logger

logger = get_logger(__name__)

@dataclass
class Action:
    intent: Intent
    src: str | None = None
    dst: str | None = None
    raw: str | None = None


def best_match(text: str) -> Intent:
    """Find the most likely intent based on synonym similarity."""
    text = text.lower()
    best_intent = Intent.UNKNOWN
    best_score = 0.0

    for intent, synonyms in INTENT_SYNONYMS.items():
        for phrase in synonyms:
            if phrase in text:
                return intent  # direct match
            score = SequenceMatcher(None, phrase, text).ratio()
            if score > best_score:
                best_intent = intent
                best_score = score
    return best_intent


def parse(text: str) -> Action:
    """Parse raw user text into an Action with guessed intent and arguments."""
    if not text.strip():
        return Action(Intent.UNKNOWN, raw=text)

    text = text.strip().lower()
    intent = best_match(text)
    src = dst = None

    # Extract arguments if any
    if " to " in text and ("move" in text or "copy" in text or "rename" in text):
        parts = text.split(" to ", 1)
        src = parts[0].split()[-1]
        dst = parts[1].strip()
    elif "file" in text:
        src = text.split("file")[-1].strip()
    elif "folder" in text or "directory" in text:
        src = text.split()[-1].strip()

    return Action(intent=intent, src=src, dst=dst, raw=text)
