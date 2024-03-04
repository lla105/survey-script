import tkinter as tk
# from tkinter import tk

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Add Transactions")
        self.root.geometry("800x500")
        # self.button = tk.Button(self.root, text="Add Transactions", command=self.open_popup)
        # self.button.pack(side="right")
        # style = tk.Style()
        # style.configure("TButton", padding=10, height=100, width=40)
        buttonx = int(0.8 * 800)
        buttony = int(0.2 * 500)
        self.button = tk.Button(self.root, 
                                text="Add Transactions", 
                                command=self.open_popup,
                                padx = 50,
                                pady = 20)
        self.button.place(relx=0.65, rely=0.2)

    def open_popup(self):
        popup_window = PopupWindow(self.root)

class PopupWindow:
    def __init__(self, parent):
        self.popup = tk.Toplevel(parent)
        self.popup.title("Popup Window")

        self.entry = tk.Entry(self.popup)
        self.entry.pack()

        self.submit_button = tk.Button(self.popup, text="Submit", command=self.submit)
        self.submit_button.pack()

    def submit(self):
        entered_value = self.entry.get()
        print("Entered value:", entered_value)
        self.popup.destroy()

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()
