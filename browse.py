from tkinter import filedialog

def browse_file():
    fname = filedialog.askopenfilenames(initialdir = ".",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
    fname = "\n".join(fname)
    return(fname)