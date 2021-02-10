from tkinter import Tk, Menu, scrolledtext, filedialog, END, messagebox
from os.path import basename as bn
from os import system

filename: str = ""

# Tk stuff
window = Tk(className = " Text Editor")

# Functions for Menubar
def NSSave(*args):
    try:
        global filename
        with open(filename, "w") as fn:
            data = textArea.get("1.0", END+"-1c")
            fn.write(data)
    except FileNotFoundError:
        NSSaveAs()
def NSSaveAs(*args):
    file = filedialog.asksaveasfile(mode="w", defaultextension="*.tim", filetypes=(("Thulium 2 (*.tim)", "*.tim"), ("Thulium 1 (*.tlm)", "*.tlm"), ("Generic Text (*.txt)", "*.txt"), ("All files", "*.*")))
    global filename
    filename = file.name
    window.title(f"{bn(file.name)} - No Sweat")
    if file != None:
        data = textArea.get("1.0", END+"-1c")
        file.write(data)
        file.close()
def NSNew(*args):
    global filename
    filename = "Untitled"
    textArea.delete("1.0", END+"-1c")
def NSOpen(*args):
    global filename
    file = filedialog.askopenfile(parent=window, title="No Sweat: Open file", filetypes=(("Thulium 2 (*.tim)", "*.tim"), ("Thulium 1 (*.tlm)", "*.tlm"), ("Generic Text (*.txt)", "*.txt"), ("All files", "*.*")))
    filename = file.name
    window.title(f"{bn(file.name)} - No Sweat")
    if file != None:
        contents = file.read()
        textArea.delete("1.0", END+"-1c")
        textArea.insert("1.0", contents)
        file.close()
def NSAbout():
    label = messagebox.showinfo("About", "No Sweat (or NSCode) is a simple editor made with python.")
def NSRun2(*args):
    system(f"thulium run {filename} a.tlmc")
def NSRun1(*args):
    system(f"thulium execute {filename}")


# Body of editor
window.title("No Sweat")
textArea = scrolledtext.ScrolledText(window, width=window.winfo_reqwidth(), height=window.winfo_reqheight())

# Menu
menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
runmenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New                (Ctrl-N)", command=NSNew)
filemenu.add_command(label="Open              (Ctrl-O)", command=NSOpen)
filemenu.add_command(label="Save                (Ctrl-S)", command=NSSave)
filemenu.add_command(label="Save As           (Ctrl-Shift-S)", command=NSSaveAs)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit)

# Running files
menu.add_cascade(label="Run", menu=runmenu)
runmenu.add_command(label="Thulium 1     (Ctrl-Shift-R)", command=NSRun1)
runmenu.add_command(label="Thulium 2     (Ctrl-R)", command=NSRun2)


# Help menu
helpMenu = Menu(menu)
menu.add_cascade(label="Help")
menu.add_cascade(label="About", command=NSAbout)

# Keyboard Bindings
textArea.bind("<Control-o>", NSOpen)
textArea.bind("<Control-n>", NSNew)
textArea.bind("<Control-s>", NSSave)
textArea.bind('<Control-Shift-KeyPress-S>', NSSaveAs)
textArea.bind("<Control-r>", NSRun2)
textArea.bind('<Control-Shift-KeyPress-R>', NSRun1)

# More Tk stuff
textArea.pack()
window.mainloop()