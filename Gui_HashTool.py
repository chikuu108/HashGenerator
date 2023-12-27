
#chosse which type of hash do you want ?\n press 1 for sha1()\n press 2 for sha224() \n press 3 for shake_128() \n press 4 for blake2b() \n press 5 for md5()"
import tkinter as tk
import tkinter.font as tkFont
import hashlib
#from tkinter import *

def dh():
    #e = input("Enter the value that you want to convert in hash : \n")
    v = value_input.get()
    #a = input("""Which type of hash do you want In the following option?
    #press 1 for sha1() 
    #press 2 for sha224() 
    #press 3 for shake_128() 
    #press 4 for blake2b() 
    #press 5 for md5() \n """)
    a = opt_input.get()
    ravi = ""
    if(a == '1'):
        ravi = hashlib.sha1(v.encode()).hexdigest() 
    elif(a == '2'):
        ravi = hashlib.sha224(v.encode()).hexdigest() 
    elif(a == '3'): 
        ravi = hashlib.sha3_224(v.encode()).hexdigest() 
    elif(a == '4'):
        ravi = hashlib.blake2b(v.encode()).hexdigest() 
    elif(a == '5'):
        ravi = hashlib.md5(v.encode()).hexdigest() 
    else:
        ravi ="Slect right option"
    return ravi
        

class App:
    def __init__(self, root):
        #setting title
        root.title("GUI hash converter ver-1.1.0")
        #setting window size
        width=600
        height=500
        root.minsize(500,500)
        root.iconbitmap("has.ico")
        root.configure(background='#fab055')
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_866=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        GLabel_866["font"] = ft
        GLabel_866["fg"] = "#333333"
        GLabel_866["justify"] = "center"
        GLabel_866["text"] = "Enter the value for convert in hash"
        GLabel_866["background"] = "#fab055"
        GLabel_866.place(x=130,y=30,width=317,height=30)
        
        global value_input
        value_input=tk.Entry(root)
        value_input["borderwidth"] = "2px"
        value_input["cursor"] = "target"
        ft = tkFont.Font(family='Times',size=14)
        value_input["font"] = ft
        value_input["fg"] = "#333333"
        value_input["justify"] = "center"
        
        #value_input["text"] = "Value for hash"
        value_input.place(x=190,y=80,width=160,height=30)
        #e = GLineEdit_835.get 
        #v = value_input.get()
        

        global opt_input
        opt_input=tk.Entry(root)
        opt_input["borderwidth"] = "2px"
        opt_input["cursor"] = "target"
        ft = tkFont.Font(family='Times',size=12)
        opt_input["font"] = ft
        opt_input["fg"] = "black"
        opt_input["justify"] = "center"
        #opt_input["text"] = "No. For convert"
        opt_input.place(x=190,y=280,width=160,height=30)
        #opt = opt_input.get()
        

        btn=tk.Button(root)
        btn["bg"] = "#5fb878"
        btn["cursor"] = "target"
        ft = tkFont.Font(family='Times',size=14)
        btn["font"] = ft
        btn["fg"] = "#000000"
        btn["justify"] = "center"
        btn["text"] = "Convert"
        btn.place(x=470,y=430,width=103,height=40)
        btn["command"] = self.btn_command

        text_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=16)
        text_label["font"] = ft
        text_label["fg"] = "#333333"
        text_label["justify"] = "left"
        text_label["text"] = "Which type of hash do you want ?\n press 1 for sha1()\n press 2 for sha224()\n press 3 for shake_128()\n press 4 for blake2b()\n press 5 for md5()"
        text_label["bg"] = "#fab055"
        text_label.place(x=150,y=110,width=278,height=164)

        
    def btn_command(self):
        GLabel_745=tk.Label(root)
        GLabel_745["bg"] = "#66f2f2"
        GLabel_745["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_745["font"] = ft
        GLabel_745["fg"] = "#333333"
        GLabel_745["justify"] = "center"
        #GLabel_745["text"] = dh()
        #GLabel_745.config(text=dh())
        GLabel_745.place(x=50,y=370,width=494,height=50)
        GLabel_745["text"] = dh()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
