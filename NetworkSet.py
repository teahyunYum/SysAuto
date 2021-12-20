import tkinter as tk
import OsInfoDefs as osdef
from typing import Text
class NetworkSet(tk.Tk):
    def __init__(self,temp):
        tk.Tk.__init__(self)
        self.geometry("300x260+800+400")
        self.labelframe=tk.LabelFrame(self,text=f'Network Setting\n{temp[0]}', relief="ridge",font=('Malgun Gothic',13, 'bold'), bd=2,)
        self.labelframe.pack(side='left',fill='both',expand=True,anchor='w')
        self.infoframe=tk.Frame(self.labelframe, relief="solid",bg='white')
        self.infoframe.pack(side='top',fill='both',expand=True)
        self.btframe=tk.Frame(self.labelframe, relief="solid",bg='white')
        self.btframe.pack(side='top',fill='both',expand=True)
        self.label1=tk.Label(self.infoframe,text='Address:',font=('Malgun Gothic', 12, 'bold'),bg='white',width=12,anchor='e')
        self.label1.grid(row=0,column=0,sticky='E')
        self.label2=tk.Label(self.infoframe,text='Gateway:',font=('Malgun Gothic', 12, 'bold'),bg='white',width=12,anchor='e')
        self.label2.grid(row=1,column=0,sticky='E')
        self.label3=tk.Label(self.infoframe,text='Subnet Mask:',font=('Malgun Gothic', 12, 'bold'),bg='white',width=12,anchor='e')
        self.label3.grid(row=2,column=0,sticky='E')
        self.label4=tk.Label(self.infoframe,text='DNS Setting',font=('Malgun Gothic', 12, 'bold'),bg='white',width=12,anchor='e')
        self.label4.grid(row=3,column=0,sticky='E')
        self.label5=tk.Label(self.infoframe,text='└─Basic:',font=('Malgun Gothic', 12, 'bold'),bg='white',width=12,anchor='e')
        self.label5.grid(row=4,column=0,sticky='E')
        self.label6=tk.Label(self.infoframe,text='└─Sub:',font=('Malgun Gothic', 12, 'bold'),bg='white',width=12,anchor='e')
        self.label6.grid(row=5,column=0,sticky='E')
        self.i_ent1=tk.Entry(self.infoframe,bg='#ffe6cc',font=('Malgun Gothic', 10, 'bold'),justify='center')
        self.i_ent1.grid(row=0,column=1)
        self.i_ent2=tk.Entry(self.infoframe,bg='#ffe6cc',font=('Malgun Gothic', 10, 'bold'),justify='center')
        self.i_ent2.grid(row=1,column=1)
        self.i_ent3=tk.Entry(self.infoframe,bg='#ffe6cc',font=('Malgun Gothic', 10, 'bold'),justify='center')
        self.i_ent3.grid(row=2,column=1)
        self.i_ent5=tk.Entry(self.infoframe,bg='#ffe6cc',font=('Malgun Gothic', 10, 'bold'),justify='center')
        self.i_ent5.grid(row=4,column=1)
        self.i_ent6=tk.Entry(self.infoframe,bg='#ffe6cc',font=('Malgun Gothic', 10, 'bold'),justify='center')
        self.i_ent6.grid(row=5,column=1)
        def setip():
            self.i_ent1.insert(0,temp[1])
            self.i_ent2.insert(0,temp[2])
            self.i_ent3.insert(0,temp[3])
            self.i_ent5.insert(0,temp[5])
            self.i_ent6.insert(0,temp[6])
            self.i_ent1.focus_force()
            self.i_ent1.select_range(0,'end')
        setip()
        def refreshbt():
            entrydel()
            ninfo=osdef.selnetwork(temp[0])
            self.i_ent1.insert(0,ninfo[0])
            self.i_ent2.insert(0,ninfo[1])
            self.i_ent3.insert(0,ninfo[2])
            self.i_ent5.insert(0,ninfo[4])
            self.i_ent6.insert(0,ninfo[5])
            self.i_ent1.focus_force()
            self.i_ent1.select_range(0,'end')
        def entrydel():
            self.i_ent1.delete(0,'end')
            self.i_ent2.delete(0,'end')
            self.i_ent3.delete(0,'end')
            self.i_ent5.delete(0,'end')
            self.i_ent6.delete(0,'end')
        def networkset():
            iplist=[]
            iplist.append(self.i_ent1.get())
            iplist.append(self.i_ent2.get())
            iplist.append(self.i_ent3.get())
            iplist.append(self.i_ent5.get())
            iplist.append(self.i_ent6.get())
            osdef.ipset(temp[0],iplist)
        def DHSPser():
            osdef.DHSPset(temp[0])
            


        
        self.rebt=tk.Button(self.btframe,text='Refresh',command=refreshbt,font=('Malgun Gothic', 10, 'bold'))
        self.rebt.pack(side='left',padx=(10,0))
        self.setbt=tk.Button(self.btframe,text='Set',command=networkset,font=('Malgun Gothic', 10, 'bold'))
        self.setbt.pack(side='right',ipadx=(15),padx=(0,10))
        self.dhcpsetbt=tk.Button(self.btframe,command=DHSPser,text='For DHCP Set',font=('Malgun Gothic', 10, 'bold'))
        self.dhcpsetbt.pack(side='right',padx=(0,10))
            
if __name__ == "__main__":
    app = NetworkSet()
    app.mainloop()
