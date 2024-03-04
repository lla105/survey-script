import tkinter as tk
from tkinter import messagebox



class MyGUI:
    def __init__(self):
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=exit)
        self.menubar.add_cascade(menu=self.filemenu, label="File1")
        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10,pady=10)
        self.textbox = tk.Text(self.root, height=5, font=('Arial', 18))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10,pady=5)

        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message) 
        #NOT show_msg(). we're not calling it, we're just passing it as a parameter
        self.button.pack(padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.ENDK))

    def shortcut(self, event):
        if event.state ==8 and event.keysym=="Return":
            self.show_message()

    def on_closing(self):
        if messagebox.askyesno(title="Quits?", message="Do you really want to quit?"):
            self.root.destroy()
MyGUI()
# from tkinter import * #import more than you need. leads to ambiguity 

# root = tk.Tk()
# root.geometry("800x500")
# root.title("My First GUI")

# label = tk.Label(root,  text="Hello World!", font=('arial', 18))
# label.pack(padx=20, pady=20)
# textbox = tk.Text(root, height=3, font=('Arial', 16))
# textbox.pack(padx=10, pady=10)

# buttonframe = tk.Frame(root)
# buttonframe.columnconfigure(0, weight=1)
# buttonframe.columnconfigure(1, weight=1)
# buttonframe.columnconfigure(2, weight=1)

# btn1 = tk.Button(buttonframe, text="1", font=('Arial', 18))
# btn1.grid(row=0, column=0, sticky=tk.W+tk.E) #means start counting from first row and column. tk.W E is West and East
# btn2 = tk.Button(buttonframe, text="2", font=('Arial', 18))
# btn2.grid(row=0, column=1, sticky=tk.W+tk.E)
# btn3 = tk.Button(buttonframe, text="3", font=('Arial', 18))
# btn3.grid(row=0, column=2, sticky=tk.W+tk.E)
# btn4 = tk.Button(buttonframe, text="4", font=('Arial', 18))
# btn4.grid(row=1, column=0, sticky=tk.W+tk.E)
# btn5 = tk.Button(buttonframe, text="5", font=('Arial', 18))
# btn5.grid(row=1, column=1, sticky=tk.W+tk.E)
# btn6 = tk.Button(buttonframe, text="6", font=('Arial', 18))
# btn6.grid(row=1, column=2, sticky=tk.W+tk.E)

# buttonframe.pack(fill='x') # or use .place

# anotherbtn = tk.Button(root, text="TEST") # a pop up widget
# anotherbtn.place(x=200, y=200, height=100, width=100)
# # one line input
# myentry = tk.Entry(root)
# myentry.pack()



# a grid of buttons. like calculator

# root.mainloop()