from gettext import npgettext
from tkinter import *
import tkinter
import numpy as np
import matplotlib.pyplot as plt
import trimesh as trimesh
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter.filedialog import askopenfile 
from PIL import ImageTk, Image
from createImage import *



root = Tk()
root.title("DLP Slicer")
root.geometry("1920x1080")
wWidth = 800
wHeight = 500
myLabel = Label(text= "DLP Slicer")
myLabel.place(relx=0.5, rely= 15/wHeight, anchor=CENTER)

file = None


#Contains features for the exit window
def exit():
    child = Toplevel(root)
    child.geometry("250x150")
    exit_label= Label(child, text="Do you want save changes?", font = ('TkDefaultFont', 10))
    exit_label.pack()

    save_button = Button(child, text= "Save", command=save) #should save to a file?
    save_button.place(x=42, y=50)
    dont_save_button = Button(child, text= "Don't save", command=root.quit)
    dont_save_button.place(x=86, y=50)
    cancel_button = Button(child, text= "Cancel", command=child.destroy)
    cancel_button.place(x=160, y=50)

#Contains the save button's functionality
def save():
	save_window = Toplevel(root)
	save_window.geometry("500x400")
	file_name_label = Label(save_window, text= "Enter file name: ")
	file_name_label.place(x=95, y=100)
	file_name = Entry(save_window, width=20)
	file_name.place(x= 185, y=100)
	file_name_button = Button(save_window, text= "Save", padx = 20, pady=-10)
	file_name_button.place(x = 300, y = 100)

#open file
def open_file():
    global file
    file_path = askopenfile(mode='r', filetypes=[('3D Object File', '*jpeg *stl *png')])
    if file_path is not None:
        file = r"{}".format(file_path.name)

    stlImage(file)
    #image frame

    # Create a photoimage object of the image in the path
    photo = PhotoImage(file = "./ImageSTL/file.png")

    # Resize image to fit on button
    photoimage = photo.subsample(2, 2)

    # Position image on button
    Button(root, image = photoimage,).place(relx= 0.5, rely= 100/wHeight, anchor=CENTER)

#slice functionality
def myClick():
    zip_window = Toplevel(root)
    zip_window.geometry("780x200")

    zip_label = Label(zip_window, text="Enter file name: ")
    zip_label.place(relx= 0.165, rely = 0.5, anchor=CENTER)
    zip_input = Entry(zip_window)
    zip_input.place(relx= 0.3, rely = 0.5, anchor=CENTER)

    dpi_label = Label(zip_window, text="Enter DPI: ")
    dpi_label.place(relx= 0.695, rely = 0.5, anchor=CENTER)
    dpi_input = Entry(zip_window)
    dpi_input.place(relx= 0.81, rely = 0.5, anchor=CENTER)

    e.get()

# #Input boxes and labels for width, x-scale, height, y-scale, slices, and z-scale
width_label = Label(root, text="Width: ")
width_label.place(relx=0.39, rely=200/wHeight, anchor=CENTER)
width = Entry(root, width=10)
width.place(relx=0.42, rely = 200/wHeight, anchor=CENTER)

x_scale_label = Label(root, text="X-Scale: ")
x_scale_label.place(relx=0.39, rely=250/wHeight, anchor=CENTER)
x_scale = Entry(root, width=10)
x_scale.place(relx=0.42, rely = 250/wHeight, anchor=CENTER)

height_label = Label(root, text="Height: ")
height_label.place(relx=0.47, rely=200/wHeight, anchor=CENTER)
height = Entry(root, width=10)
height.place(relx=0.5, rely = 200/wHeight, anchor=CENTER)

y_scale_label = Label(root, text="Y-Scale: ")
y_scale_label.place(relx=0.47, rely=250/wHeight, anchor=CENTER)
y_scale = Entry(root, width=10)
y_scale.place(relx=0.5, rely = 250/wHeight, anchor=CENTER)

slices_label = Label(root, text="Slices: ")
slices_label.place(relx=0.55, rely=200/wHeight, anchor=CENTER)
slices = Entry(root, width=10)
slices.place(relx=0.58, rely=200/wHeight, anchor=CENTER)

z_scale_label = Label(root, text="Z-Scale: ")
z_scale_label.place(relx=0.55, rely=250/wHeight, anchor=CENTER)
z_scale = Entry(root, width=10)
z_scale.place(relx=0.58, rely=250/wHeight, anchor=CENTER)

# #menu bar
my_menu = Menu(root)

root.config(menu=my_menu)

def our_command():
    pass
file_menu = Menu(my_menu)

my_menu.add_cascade(label="File", menu=file_menu) #File option

file_menu.add_command(label="New...", command=our_command)
file_menu.add_separator()#Creates bar
file_menu.add_command(label="Exit",command=exit)

# #Choose file button
dlbtn = Button(
    root, 
    text ='Choose File ', 
    command = lambda:open_file()
    ) 


dlbtn.place(x=20, y=20)
# #create and edit menu item.
# edit_menu = Menu(my_menu)
# my_menu.add_cascade(label='Settings', menu = edit_menu)
# edit_menu.add_command(label='Settings1', command=our_command)
# edit_menu.add_command(label='Settings2', command=root.quit)

# #Slice button
Slice = Button(root, text="Slice",padx = 15, pady = 5, command=myClick)
Slice.place(relx=0.5, rely = 300/wHeight, anchor=CENTER)

# #upload button
root.mainloop()