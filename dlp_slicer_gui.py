from gettext import npgettext
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import trimesh as trimesh

root = Tk()
root.title("DLP Slicer")
root.geometry("800x500")
myLabel = Label(text= "DLP Slicer")
myLabel.pack()

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

#This is suppose to display a fixed 3-D Image (still figuring out how to display)
def display_3d():

    mymesh = trimesh.load_mesh('{}.stl'.format(name))

    vertices = mymesh.vertices
    array = np.array(vertices)
    minZ = np.min(array[:,2])
    maxZ = np.max(array[:,2])

    mymesh.show()

    slices = []

    for z in np.linspace(minZ, maxZ, 40):
        print(z)
    l = mymesh.section(plane_origin=[0, 0, z], 
                     plane_normal=[0,0,1])

    slices.append(l)
    slices = [slice for slice in slices if slice is not None]


    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    for idx, slice in enumerate(slices):
        x = [slice.vertices[:,0]]
        y = [slice.vertices[:,1]]
        z = [slice.vertices[:,2]]

    ax.scatter(x, y, z)


    ax.grid(True)
    fig.tight_layout()
    fig.pack()

#Input boxes and labels for width, x-scale, height, y-scale, slices, and z-scale
width_label = Label(root, text="Width: ")
width_label.place(x=157, y=250)
width = Entry(root, width=10)
width.place(x=200, y=250)

x_scale_label = Label(root, text="X-Scale: ")
x_scale_label.place(x=150, y=350)
x_scale = Entry(root, width=10)
x_scale.place(x=200, y=350)

height_label = Label(root, text="Height: ")
height_label.place(x=318, y=250)
height = Entry(root, width=10)
height.place(x=365, y=250)

y_scale_label = Label(root, text="Y-Scale: ")
y_scale_label.place(x=316, y=350)
y_scale = Entry(root, width=10)
y_scale.place(x=365, y=350)

slices_label = Label(root, text="Slices: ")
slices_label.place(x=490, y=250)
slices = Entry(root, width=10)
slices.place(x=530, y=250)

z_scale_label = Label(root, text="Z-Scale: ")
z_scale_label.place(x=480, y=350)
z_scale = Entry(root, width=10)
z_scale.place(x=530, y=350)

def myClick():
    e.get()


#menu bar
my_menu = Menu(root)

root.config(menu=my_menu)

def our_command():
    pass
file_menu = Menu(my_menu)

my_menu.add_cascade(label="File", menu=file_menu) #File option

file_menu.add_command(label="New...", command=our_command)
file_menu.add_separator()#Creates bar
file_menu.add_command(label="Exit",command=exit)

#create and edit menu item.
edit_menu = Menu(my_menu)
my_menu.add_cascade(label='Settings', menu = edit_menu)
edit_menu.add_command(label='Settings1', command=our_command)
edit_menu.add_command(label='Settings2', command=root.quit)

#Slice button
Slice = Button(root, text="Slice",padx = 15, pady = 5, command=myClick, fg= "blue", bg = "white")
Slice.place(x=365, y=450)

#upload button


# display_3d()


root.mainloop()