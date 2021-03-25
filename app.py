import threading;
import keyboard;
import os.path;
import re;
import win32api;

def press_key(key, interval):
    
    keyboard.send(key);
    key_timer = threading.Timer(interval, press_key, [key, interval]);
    key_timer.start();

def assign_timer(key, interval):
    
    #tmr = setInterval(interval, press_key, args);
    key_timer = threading.Timer(interval, press_key, [key, interval]);
    key_timer.start();
    
def main():
    config_exists = os.path.isfile("config.txt");
    if(config_exists == False):
        temp = open("config.txt", "w+");
        default_line = "#Key = interval in seconds e.g A = 4";
        temp.write(default_line);
        temp.close();
    config = open("config.txt", "r+");
    lines = config.readlines();
    for i in range(1, len(lines)):
        try:
            temp = re.search("(?P<key>[^=]) = (?P<interval>([1-9][0-9]*[^.])|((([1-9][0-9]*)|0)\.[0-9]+))", lines[i]);
            key = temp.group("key");
            interval = float(temp.group("interval"));

            assign_timer(key, interval);
        except:
            win32api.MessageBox(0, 'At least one line does not meet the format specified in config.txt. Please fix the error and restart the program', 'Error' );
            raise SystemExit(0);
        
    config.close();

if __name__ == "__main__":
    main();
    
    