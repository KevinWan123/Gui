from msilib.schema import File
from pydoc import cli
from tkinter import *
from PIL import Image
#Test

root = Tk()
root.title('myTilte')
root.geometry("600x400")

my_menu = Menu(root)

root.config(menu=my_menu)
#click command
def our_command():
    pass
#Create a menu item

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu) #File option

file_menu.add_command(label="New...", command=our_command)
file_menu.add_separator()#Creates bar
file_menu.add_cascade(label="Exit..",command=our_command)


#create and edit menu item.

edit_menu = Menu(my_menu)
my_menu.add_cascade(label='Settings', menu = edit_menu)
edit_menu.add_command(label='Settings1', command=our_command)
edit_menu.add_command(label='Settings2', command=root.quit)
root.mainloop()