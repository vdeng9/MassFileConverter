#Personal Mass file conversion (w/ basic GUI) with base python libraries written by me, Victor Deng
#TODO Maybe make extfrom and extto be buttons MAYBE there are a ton of file extensions.....so maybe not
import os
import sys
import tkinter as tk
from tkinter import filedialog

#non-tkinter implementation
#folderpath = r'C:\Users\'
#extfrom = ".cbz"
#extto = ".zip"

#tk implemented 

root = tk.Tk()
root.geometry("600x400")

folderpath = tk.StringVar()
ktextfrom = tk.StringVar()
ktextto = tk.StringVar()
browsedfilecheck = 0

def submit():
    if browsedfilecheck == 0: 
        general_label.configure(text="add folder path")
        return 
    extfrom = ktextfrom.get()
    extto = ktextto.get()

    for beforecheck in os.listdir(folderpath):
        print("before conversion: {}".format(beforecheck))

    for file in os.listdir(folderpath):
        currentfile = os.path.join(folderpath, file)
        basefile = os.path.splitext(currentfile)
        if basefile[1] == extfrom:
            os.rename(currentfile, basefile[0] + extto)

    for aftercheck in os.listdir(folderpath):
        print("after conversion: {}".format(aftercheck))

def exit():
    sys.exit("goodbye")

def browsefile():
    global browsedfilecheck
    global folderpath
    temp = "List of files: "
    folderpath = filedialog.askdirectory(title='select folder')
    folderpath_label.configure(text=folderpath)
    for file in os.listdir(folderpath):
        temp += file + ", "
    print(temp)
    browsedfilecheck = 1

extfrom_label = tk.Label(root, text='from:', font=('arial', 12, 'normal'))
extfrom_entry = tk.Entry(root, textvariable=ktextfrom, font=('arial', 12, 'normal'))

extto_label = tk.Label(root, text='to:', font=('arial', 12, 'normal'))
extto_entry = tk.Entry(root, textvariable=ktextto, font=('arial', 12, 'normal'))

folderpath_label = tk.Label(root, width= 50, height=4)
folderpath_btn = tk.Button(root, text="Browse Folders", command=browsefile)

general_label = tk.Label(root)

sub_btn = tk.Button(root, text="Okay", command=submit)
exit_btn = tk.Button(root, text="Exit", command=exit)

extfrom_label.grid(row=0,column=3)
extfrom_entry.grid(row=0,column=4)

extto_label.grid(row=1, column= 3)
extto_entry.grid(row=1, column=4)

folderpath_label.grid(row=2, column=4)

folderpath_btn.grid(row=4, column=3)
sub_btn.grid(row=4, column=4)
exit_btn.grid(row=4, column=5)

general_label.grid(row=5, column=4)

root.mainloop()
