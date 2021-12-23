import AutoRunDefs as Adef
import tkinter.ttk
import tkinter as tk
from tkinter import messagebox
import time
class OSAutoRun(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack(side='top',fill='both',expand=True)
        MainFrame=tk.Frame(self)
        MainFrame.pack(side='top',fill='both',expand=True)
        chkvar1=tk.BooleanVar()
        chkvar2=tk.BooleanVar()
        chkvar3=tk.BooleanVar()
        chkvar4=tk.BooleanVar()
        chkvar5=tk.BooleanVar()
        defaultframe=tk.LabelFrame(MainFrame,text='Default Settings', relief="ridge",font=('Malgun Gothic',18, 'bold'), bd=2)
        defaultframe.pack()
        infoframe=tk.Frame(defaultframe)
        infoframe.pack(side='top',fill='both',expand=True,padx=(10,10))
        btframe=tk.Frame(defaultframe)
        btframe.pack(side='top',fill='both',expand=True,padx=(10,10))
        def defaultset():
            temp=Adef.sysdefault()
            chkbox1.config(text=f'Current: {temp[0]}')
            chkbox2.config(text=f'User Name: {temp[1]}')
            chkbox3.config(text=f'Current Update: {temp[2]}')
            chkbox4.config(text=f'Defender Enabled: {temp[3]}')
            chkbox5.config(text='Action Center Off Set')
        def setlist():
            try:
                temp=Adef.defaultlist(chkvar1.get(),chkvar2.get(),chkvar3.get(),chkvar4.get(),chkvar5.get())
                Adef.runset(temp)
            except Exception as e:
                messagebox.showerror(f"","Error{e}")
            else:
                messagebox.showinfo("","Success")
        def updateunset():
            try:
                Adef.updatereset()
            except Exception as e:
                messagebox.showerror(f"","Error{e}")
            else:
                messagebox.showinfo("","Success")

        
            
        #---------------------checkboxlist------------------------------
        chkbox1=tk.Checkbutton(infoframe,var=chkvar1,font=('Malgun Gothic', 13, 'bold'))
        chkbox1.grid(row=0,column=0,sticky='w')
        chkbox2=tk.Checkbutton(infoframe,text='',var=chkvar2,font=('Malgun Gothic', 13, 'bold'))
        chkbox2.grid(row=2,column=0,sticky='w')
        chkbox3=tk.Checkbutton(infoframe,var=chkvar3,font=('Malgun Gothic', 13, 'bold'))
        chkbox3.grid(row=4,column=0,sticky='w')
        chkbox4=tk.Checkbutton(infoframe,var=chkvar4,font=('Malgun Gothic', 13, 'bold'))
        chkbox4.grid(row=6,column=0,sticky='w')
        chkbox5=tk.Checkbutton(infoframe,var=chkvar5,font=('Malgun Gothic', 13, 'bold'))
        chkbox5.grid(row=8,column=0,sticky='w')
        def defaultlist():
            with open('checklist.text','r') as f:
                temp=f.readlines()
            for i in range(len(temp)):temp[i]=temp[i].replace('\n',"").replace(" ","")
            chkvar1.set(temp[0])
            chkvar2.set(temp[1])
            chkvar3.set(temp[2])
            chkvar4.set(temp[3])
            chkvar5.set(temp[4])
        defaultlist()
        
        #---------------------checkboxlabels------------------------------
        label1=tk.Label(infoframe,text='Power Saving Mode Off Set',font=('Malgun Gothic', 13, 'bold'),justify='left')
        label1.grid(row=0,column=1,sticky='w')
        label2=tk.Label(infoframe,text='User Account Control Set',font=('Malgun Gothic', 13, 'bold'),justify='left')
        label2.grid(row=2,column=1,sticky='w')
        label3=tk.Label(infoframe,text='Windows Update Disable',font=('Malgun Gothic', 13, 'bold'),justify='left')
        label3.grid(row=4,column=1,sticky='w')
        label4=tk.Label(infoframe,text='Windows Defender Disable',font=('Malgun Gothic', 13, 'bold'),justify='left')
        label4.grid(row=6,column=1,sticky='w')
        label5=tk.Label(infoframe,text='Base Auto UI Settings',font=('Malgun Gothic', 13, 'bold'),justify='left')
        label5.grid(row=8,column=1,sticky='w')
        exlabel1=tk.Label(infoframe,text='절전모드를 "고성능"그룹으로 설정하고 아래설정을 해제합니다\n(절전모드, 모니터꺼짐, 모니터자동밝기, 디스크절전모드, USB절전모드)',font=('Malgun Gothic', 10, 'bold'))
        exlabel1.grid(row=1,column=0,columnspan=2)
        exlabel2=tk.Label(infoframe,text='사용자를 관리자로 설정하고 알림설정을 해제합니다',font=('Malgun Gothic', 10, 'bold'))
        exlabel2.grid(row=3,column=0,columnspan=2)
        exlabel3=tk.Label(infoframe,text='윈도우 업데이트설정을 해제하고 관련된 아래설정을 해제합니다\n(Health Service, Windows Update, Medic Service, Orchestrator)\n※이설정은 레지스트리값을 수정합니다 \n업데이트를 다시 사용할 경우 <UpdateReset>을 사용하십시요',font=('Malgun Gothic', 10, 'bold'))
        exlabel3.grid(row=5,column=0,columnspan=2)
        exlabel4=tk.Label(infoframe,text='윈도우 Defender 설정을 해제합니다',font=('Malgun Gothic', 10, 'bold'))
        exlabel4.grid(row=7,column=0,columnspan=2)
        exlabel5=tk.Label(infoframe,text='이 설정은 사용자PC UI기준으로 작동합니다(자동마우스,키보드)\n실행환경이 다른 경우 Setting 메뉴를 설정해야 합니다\n(보안 및 유지관리알림해제, 시스템알림해제, 방화벽알림해제)',font=('Malgun Gothic', 10, 'bold'))
        exlabel5.grid(row=9,column=0,columnspan=2)
        upresetbt=tk.Button(btframe,text='Update Reset',font=('Malgun Gothic', 13, 'bold'),command=updateunset)
        upresetbt.pack(side='left',padx=(30,0),pady=(20,10),ipadx=2)
        refreshbt=tk.Button(btframe,text='Refresh',font=('Malgun Gothic', 13, 'bold'),command=defaultlist)
        refreshbt.pack(side='left',padx=(20,0),pady=(20,10),ipadx=2)
        setbt=tk.Button(btframe,text='Set Run',font=('Malgun Gothic', 13, 'bold'),command=setlist)
        setbt.pack(side='right',padx=(0,30),pady=(20,10),ipadx=2)
        defaultset()
        
    
        