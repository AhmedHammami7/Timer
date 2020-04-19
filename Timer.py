from tkinter import *
import time
global c
c=0
class timer():
    
    def reset(self):
        global c
        c=1
        self.t.set('00:00:00')
        
    def start(self):
        global c
        c=0
        self.start_timer()
    
    def start_timer(self):
        global c
        self.timer()
    def stop(self):
        global c
        c=1
        
        
    def timer(self):
        global c
        if(c==0):
            self.d = str(self.t.get())
            h,m,s = map(int,self.d.split(":"))
            
            h = int(h)
            m=int(m)
            s= int(s)
            if(s<59):
                s+=1
            elif(s==59):
                s=0
                if(m<59):
                    m+=1
                elif(m==59):
                    h+=1
            if(h<10):
                h = str(0)+str(h)
            else:
                h= str(h)
            if(m<10):
                m = str(0)+str(m)
            else:
                m = str(m)
            if(s<10):
                s=str(0)+str(s)
            else:
                s=str(s)
            self.d=h+":"+m+":"+s
            
            
            self.t.set(self.d)
            if(c==0):
                self.root.after(930,self.start_timer)
            
        
    def __init__(self):
        self.root=Tk()
        self.root.title("Timer")
        self.root.geometry("600x166")
        self.root.resizable(False,False)
        self.t = StringVar()
        self.t.set("00:00:00")
        self.lb = Label(self.root,textvariable=self.t)
        self.lb.config(font=("Calibri 40 bold"),fg='dark turquoise')                
        self.bt1 = Button(self.root,text="Start",command=self.start,font=("Calibri 12 bold"),bg='dark turquoise', fg='light cyan')
        self.bt2 = Button(self.root,text="Stop",command=self.stop,font=("Calibri 12 bold"),bg='dark turquoise', fg='light cyan')
        self.bt3 = Button(self.root,text="Reset",command=self.reset,font=("Calibri 12 bold"),bg='dark turquoise', fg='light cyan')
        self.lb.place(x=160,y=10)
        self.bt1.place(x=130,y=100)
        self.bt2.place(x=255,y=100)
        self.bt3.place(x=370,y=100)
    


a = timer()
