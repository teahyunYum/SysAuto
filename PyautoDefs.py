import pyautogui
import time
import sys
timeout=10
def find_target(imgfile,con=0.8, timeout=15):
    start=time.time()
    target=None
    while target is None:
        target = pyautogui.locateOnScreen(imgfile,confidence=con)
        end=time.time()
        if end-start>timeout:
            break
    return target
def findall_target(imgfile,con=0.9,dur=0.25, timeout=15):
    start=time.time()
    target=None
    while target is None:
        for i in pyautogui.locateAllOnScreen(imgfile,confidence=con):
            pyautogui.click(i,duration=dur)
        end=time.time()
        if end-start>timeout:
            break
def findall_dtarget(imgfile,con=0.9,dur=0.25, timeout=15):
    start=time.time()
    target=None
    while target is None:
        for i in pyautogui.locateAllOnScreen(imgfile,confidence=con):
            pyautogui.doubleClick(i,duration=dur)
        end=time.time()
        if end-start>timeout:
            break

def clickdef(imgfile,case=0,con=0.8,dur=0.5,timeout=15):
    if case==0:
        target=find_target(imgfile,con, timeout)
        if target:
            pyautogui.click(target,duration=dur)
        else:
            pyautogui.alert(f"Not foun {imgfile}")
    elif case==1:
        target=findall_target(imgfile,con,dur, timeout)
    elif case==2:
        target=findall_dtarget(imgfile,con,dur, timeout)
        
def controlnotice():
    pyautogui.hotkey('winleft','r')
    pyautogui.time.sleep(0.5)
    pyautogui.write("wscui.cpl",interval=0.1)
    pyautogui.hotkey('enter')
    pyautogui.time.sleep(1)
    clickdef('image\controlboard_img\control1.png')
    clickdef('image\controlboard_img\control2.png',1,0.9,0.25,5)
    clickdef('image\controlboard_img\control3.png')
    pyautogui.hotkey('altleft','f4')
    


def systemnotice():
    pyautogui.hotkey('winleft','r')
    pyautogui.time.sleep(0.5)
    pyautogui.write("ms-settings:notifications",interval=0.1)
    pyautogui.hotkey('enter')
    fw=pyautogui.getActiveWindow()
    fw.maximize()
    clickdef('image\sysnotice_img\imege2.png',1,0.95,0.25,5)
    clickdef('image\sysnotice_img\imege1.png',1,0.9,0.25,5)
    pyautogui.hotkey('altleft','f4')
    
def defendernotice():
    pyautogui.hotkey('winleft','r')
    pyautogui.time.sleep(0.5)
    pyautogui.write("ms-settings:windowsdefender",interval=0.1)
    pyautogui.hotkey('enter')
    pyautogui.time.sleep(1)
    clickdef('image\defendernotice_img\imege1.png')
    pyautogui.time.sleep(1)
    fw=pyautogui.getActiveWindow()
    fw.maximize()
    clickdef('image\defendernotice_img\imege2.png')
    clickdef('image\defendernotice_img\imege3.png',0,0.9)
    clickdef('image\defendernotice_img\imege4.png',0,0.9)
    clickdef('image\defendernotice_img\imege5.png',2,0.9,0.25,5)
    pyautogui.hotkey('altleft','f4')
    pyautogui.time.sleep(1)
    pyautogui.hotkey('altleft','f4')
    

def allrun():
    controlnotice()
    systemnotice()
    defendernotice()
    

