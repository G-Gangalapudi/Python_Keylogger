# Python Keylogger

A simple Python-based keystroke logger, for educational / security-audit purposes.  
Created by G-Gangalapudi — [GitHub Repository](https://github.com/G-Gangalapudi/Python_Keylogger)

---

## Table of Contents  
- [Features](#features)  
- [How It Works](#how-it-works)  
- [Requirements](#requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Configuration](#configuration)  
- [Ethics & Legal Notice](#ethics--legal-notice)  
- [License](#license)  
- [Disclaimer](#disclaimer)  

---

## Features  
- Captures all keystrokes typed (including letters, numbers, special keys) while the script is running  
- Writes a raw log file (`keylog.txt`) showing each key event  
- Includes a secondary helper script (`keylogcleaner.py`) that processes the raw log into a more readable format (`cleaned_output.txt`)  
- Minimal external dependencies  
- Simple, compact code structure — suitable for educational / proof-of-concept uses

---

## How It Works  
1. The main script (`keylogger.py`) sets up a keyboard hook/listener to intercept each keystroke  
2. Each keystroke is logged to a file — including timing and key name/modifier  
3. The log accumulates until the program is terminated  
4. Run the cleaning tool (`keylogcleaner.py`) which reads `keylog.txt`, formats entries, and writes `cleaned_output.txt`  
5. Open `cleaned_output.txt` to inspect what was typed

---

## Requirements  
- Python 3.x (tested with Python 3.*)  
- (Optional) If using a third-party library for keyboard hooks (e.g., `pynput`, `keyboard`), install accordingly  
- Elevated/admin privileges may be required depending on OS/hook method  
- Run on a machine that you own or are authorised to monitor

---

## Installation  
```bash
git clone https://github.com/G-Gangalapudi/Python_Keylogger.git
cd Python_Keylogger
# (Optional) create virtual env
python3 -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Usage
1. Capture keystrokes
```bash
python keylogger.py
```

 Let the script run for the session you wish to capture. When done, stop it (e.g., Ctrl+C) and the log will be saved as keylog.txt.

2. Clean the log
```bash
python keylogcleaner.py
```

This reads keylog.txt and writes a cleaned, human-readable version as cleaned_output.txt.

3. View cleaned output

Open cleaned_output.txt in a text editor to inspect what was typed during the session.

---

## Configuration
You can adjust settings in the scripts, such as:
- Output file paths (raw log, cleaned log)
- Whether to include timestamps or session markers
- Which key-events to ignore (e.g., only record letters/numbers, skip modifiers)
- OS-specific behaviours (Windows vs. Linux vs. macOS)

---

## Ethics & Legal Notice

⚠️ Important: Use only in legal, authorised contexts.
- Using keyloggers without the informed consent of the person being monitored is a serious invasion of privacy and potentially illegal.
- In many jurisdictions (under GDPR, CCPA, etc.), capturing keystrokes secretly may violate laws.
- If you’re using this tool in a workplace, parental-control, or investigatory setting, ensure you have:
  - Explicit, informed consent from the monitored user
  - Clear disclosure of what is being recorded and why
  - Secure storage and limited access to logged data
  - A lawful purpose (e.g., security auditing, training, research)
- Never use this tool on a system you do not own or manage, or without full authorization.
- Use of this project for malicious purposes (covert spying, identity theft, etc.) is strictly prohibited.

---

## License

**Educational Use Only License (EUOL) © 2025 G-Gangalapudi**

This repository and its code are provided for **education, research, and study only**. You may view and inspect the source code, but you may **not**:

- Execute, run, deploy, or use the code on systems or networks for operational purposes.
- Redistribute, publish, sublicense, or share the code or any derivative works.
- Use the code to monitor, record, or otherwise collect data from persons or systems without explicit legal authorization.

If you would like permission for a use not covered here (e.g., controlled security testing, audit engagements), please contact the repository owner on GitHub to request written permission.

---

## Disclaimer

This software is provided “as-is”, without warranty of any kind.
The author(s) are not responsible for any misuse, data loss, legal liability, or damage arising from its use. By using this software you accept full responsibility and declare that you are authorised to monitor the device in question.

---

Thank you for exploring Python_Keylogger!

If you found this project useful for legitimate security awareness or testing, please feel free to open issues or send feedback via GitHub.
