from typing import Optional
from logger import get_logger
from config import VOICE_ENABLED

logger = get_logger(__name__)

class TextListener:
    def prompt(self, prompt_text: str = "Enter command: ") -> str:
        try:
            return input(prompt_text).strip()
        except EOFError:
            logger.info("EOF while reading input")
            return ""

class SpeechListener:
    def __init__(self):
        if not VOICE_ENABLED:
            raise RuntimeError("Voice disabled in config")
        try:
            import speech_recognition as sr
            self.sr = sr
        except Exception as exc:
            logger.exception("speech_recognition import failed: %s", exc)
            raise RuntimeError("Speech recognition not available")

    def listen_once(self, timeout: float = 5.0) -> str:
        r = self.sr.Recognizer()
        try:
            with self.sr.Microphone() as mic:
                logger.info("Listening (timeout=%s)...", timeout)
                audio = r.listen(mic, timeout=timeout)
            text = r.recognize_google(audio)
            logger.info("Transcription: %s", text)
            return text.strip()
        except Exception as exc:
            logger.error("Speech listen/recognize failed: %s", exc)
            return ""
