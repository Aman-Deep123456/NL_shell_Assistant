# 🧠 NL Shell Assistant — Your AI-Powered Command-Line Companion 🎙️💻

> Talk to your terminal like a human.  
> Create files, open folders, move data, check time, run code — all with voice or natural language.

---

## ⚡️ Overview

**NL Shell Assistant (Natural Language Shell Assistant)** is a smart, modular Python-based command interpreter that lets you control your system using **voice or plain English**.

It supports **500+ natural commands** — from creating files and folders to checking the date, searching text, running Python scripts, and more.

🎯 *It’s like having Siri or Alexa inside your terminal — but smarter, open-source, and developer-friendly.*

---

## ✨ Features

✅ Voice and Text Command Support (Speech-to-Action)  
✅ 500+ Natural English Commands  
✅ Safe Sandboxed File Operations  
✅ NLP-based Command Understanding (Fuzzy Matching)  
✅ System, Network & Developer Utilities  
✅ Lightweight and Fully Offline  
✅ Runs on macOS, Linux, and Windows  

---

## 🧩 Tech Stack

| Category | Technology |
|-----------|-------------|
| 💬 Speech Recognition | `speech_recognition` |
| 🗣️ Voice Output (Optional) | `pyttsx3` |
| 🧠 NLP Parsing | Custom + `difflib` fuzzy matching |
| 🧱 Backend Logic | Python 3.x |
| 🧰 File Safety | Path validation & command sanitizer |
| 🧾 Logging | `logging` + rotating file handler |
| 🧩 Cross-Platform Support | macOS / Linux / Windows |

---

## 🗂️ Project Structure

nl_shell_assistant/
├── main.py # Entry point (voice + text REPL)
├── parser.py # NLP + command understanding
├── executor.py # Executes intents safely
├── listener.py # Voice & text input handler
├── intent_definitions.py # All intents + 500+ synonyms
├── safety.py # Path validation & banned commands
├── logger.py # Centralized logging system
├── config.py # Configuration & platform detection
├── requirements.txt # Dependencies
└── README.md # (this file 😎)

---

## ⚙️ Setup & Installation

### 🧱 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/nl_shell_assistant.git
cd nl_shell_assistant

🐍 2️⃣ Create a Virtual Environment
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .\.venv\Scripts\Activate.ps1   (Windows)

📦 3️⃣ Install Dependencies
pip install -r requirements.txt
If you get an error installing pyaudio (on macOS):
brew install portaudio
pip install pyaudio


🎙️ Run the Assistant
🧠 Text Mode
python3 main.py

🎤 Voice Mode
python3 main.py --voice

Then choose:
Choose mode: (t)ext, (v)oice, (q)uit:

🗣️ Example Voice Commands
🗣️ What You Say	💻 What It Does
“make a file notes.txt”	Creates file
“make folder projects”	Creates folder
“read file notes.txt”	Displays file contents
“write to file notes.txt”	Appends your input
“move file notes.txt to projects”	Moves file
“delete file notes.txt”	Deletes file
“list files”	Lists files in current folder
“show date / show time”	Displays date/time
“ping google.com”	Tests network connectivity
“show my ip address”	Displays local IP
“run script test.py”	Runs Python script
“exit”	Ends session

🧰 Available Command Categories
📁 File Operations → make, move, copy, delete, rename, read, write
🧭 Directory Navigation → make directory, list files, where am I
🕓 System Info → show date/time/disk usage/processes
🔍 Search → find file, search for text
🌐 Network Tools → ping, show IP
🐍 Dev Utilities → run script, show Python version
⚙️ Utility → clear screen, help, exit


🧠 How It Works


1️⃣ You speak or type a natural command
2️⃣ parser.py identifies the intent using fuzzy NLP matching
3️⃣ executor.py safely performs the system action inside a sandbox
4️⃣ logger.py records every action
5️⃣ (Optional) Assistant can speak back using pyttsx3 🎧


🔒 Safety Features
⚠️ Blocks destructive commands like rm -rf / or sudo
🧩 Restricts operations to the current project folder
🛡️ Validates every file path before execution
🧾 Logs all actions for debugging


🧠 Example Session (macOS)


(.venv) amanpayal@MacBook-Air nl_shell_assistant % python3 main.py --voice

NL Shell Assistant — Text and Voice Shell
Choose mode: (t)ext, (v)oice, (q)uit: v

Listening...
✅ Created folder: AmanDeep
Listening...
✅ Created file: report.txt
Listening...
📖 Contents of report.txt:
This is a test
Listening...
📅 Today's date: 2025-11-07
Listening...
🌐 Your IP address: 192.168.1.104
Listening...

👋 Goodbye!

🧑‍💻 Author
Aman Deep 
💼 Computer Science Student | NSS Volunteer | Developer Enthusiast
🌐 LinkedIn   : https://www.linkedin.com/in/aman-deep-74300b28b/
📧 [bhagatamandeep50@gmail.com]

🤝 Contributing
Contributions are always welcome!
1️⃣ Fork this repo
2️⃣ Create a new branch (feature/new-command)
3️⃣ Commit your changes
4️⃣ Submit a Pull Request

🌟 Support
If you find this project useful,
⭐ Star this repo on GitHub — it helps others discover it!
“Automation is good, but voice automation is better.”
— Aman Deep  🧠🎤

🪄 Future Enhancements
✅ Continuous voice mode (hands-free)
✅ Text-to-speech feedback
🔄 Real-time command chaining
💻 GUI dashboard for visual file control
🧠 Integration with ChatGPT or spaCy for smarter NLP
☁️ Cloud sync for commands & logs
🏁 License
This project is licensed under the MIT License — free to use, modify, and share.
📄 MIT License © 2025 Aman Deep 
