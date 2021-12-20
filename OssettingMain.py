import tkinter as tk
from Mainui import Mainui
class OssetingMain(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.title("OS InfoMation AutoSetting")
        self.geometry("830x520+500+200")
        self.switch_frame(Mainui)
        Mainmenu=tk.Menu(self)
        Mainmenu=tk.Menu(Mainmenu,tearoff=0)
        Mainmenu.add_command(label='Sys Info',command=lambda:self.switch_frame(Mainui))
        Mainmenu.add_command(label='Run',command=lambda:self.switch_frame(Mainui))
        Mainmenu.add_command(label='Setting',command=lambda:self.switch_frame(Mainui))
        self.config(menu=Mainmenu)
        
    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        
if __name__ == "__main__":
    app = OssetingMain()
    app.mainloop()
