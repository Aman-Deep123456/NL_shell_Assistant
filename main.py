from listener import TextListener, SpeechListener
from parser import parse
from executor import execute
from logger import get_logger

logger = get_logger(__name__)

def repl():
    text_listener = TextListener()
    speech_listener = None
    try:
        speech_listener = SpeechListener()
    except Exception:
        speech_listener = None
        logger.info("Speech listener unavailable — continuing with text input")

    print("NL Shell Assistant — type 'q' to quit")
    while True:
        mode = text_listener.prompt("Choose (t)ext/(v)oice/(q)uit: ").lower().strip()
        if mode in ("q", "quit", "exit"):
            print("Goodbye!")
            break

        if mode == "v":
            if not speech_listener:
                print("Voice listener unavailable. Use text mode.")
                continue
            raw = speech_listener.listen_once()
        else:
            raw = text_listener.prompt("Command: ")

        if not raw:
            print("No input. Try again.")
            continue
        if raw.strip().lower() in ("q", "quit", "exit"):
            print("Goodbye!")
            break

        action = parse(raw)
        ok, msg = execute(action)
        if ok:
            print("✅", msg)
        else:
            print("❌", msg)

if __name__ == "__main__":
    repl()
