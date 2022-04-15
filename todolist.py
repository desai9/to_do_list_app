## Import the tkinter module
from tkinter import *
#import messagebox function
import tkinter.messagebox

#create a task entering 
def entry_task():
    #A window popup to enter the text
    input_text =""
    def add():
        input_text=entry_task.get(1.0,"end-1c")
        if input_text=="":
            tkinter.messagebox.showwarning(title='Warning!',message='Please enter some text')
        else:
            listbox.insert(END,input_text)
            #close the root1 window
            root1.destroy()
    
    root1=Tk()
    root1.title('Add Task')
    entry_task=Text(root1,height=3,width=50)
    entry_task.pack()
    button_temp = Button(root1,text='Add Task',command=add)
    button_temp.pack()
    root1.mainloop()
# Create a function for delete task
def deletetask():
    #selects the slected item and then deletes it
    select = listbox.curselection()
    listbox.delete(select[0])
# Create a function for mark completed
def marktask():
    #selects the slected item and then mark it completed
    mark = listbox.curselection()
    temp = mark[0]
    temp_mark = listbox.get(mark)
    temp_mark = temp_mark + " ✔"
    listbox.delete(temp)
    listbox.insert(temp,temp_mark)
# Create a function for clear all
def clearall():
    listbox.delete(0,END)
# Create a function for exit
def exit():
    window.destroy()
# Create a function for save
def save():
    #open the file in write mode
    file = open("todolist.txt","w")
    #write the data in the file
    for i in range(listbox.size()):
        file.write(listbox.get(i)+"\n")
    #close the file
    file.close()
# Create a function for open
def openfile():
    #open the file in read mode
    file = open("todolist.txt","r")
    #read the data from the file
    data = file.read()
    #close the file
    file.close()
    #split the data into lines
    lines = data.split("\n")
    #delete the previous data
    listbox.delete(0,END)
    #insert the data into the listbox
    for i in lines:
        listbox.insert(END,i)
# Create a function for load
def load():
    #open the file in read mode
    file = open("todolist.txt","r")
    #read the data from the file
    data = file.read()
    #close the file
    file.close()
    #split the data into lines
    lines = data.split("\n")
    #delete the previous data
    listbox.delete(0,END)
    #insert the data into the listbox
    for i in lines:
        listbox.insert(END,i)
# Create a function for save as
def saveas():
    #open the file in write mode
    file = open("todolist.txt","w")
    #write the data in the file
    for i in range(listbox.size()):
        file.write(listbox.get(i)+"\n")
    #close the file
    file.close()
# Create a function for open as
def openas():
    #open the file in read mode
    file = open("todolist.txt","r")
    #read the data from the file
    data = file.read()
    #close the file
    file.close()
    #split the data into lines
    lines = data.split("\n")
    #delete the previous data
    listbox.delete(0,END)
    #insert the data into the listbox
    for i in lines:
        listbox.insert(END,i)
# Create a function for about
def about():
    #A window popup to show the about message
    tkinter.messagebox.showinfo(title='About',message='This is a simple todo list application')
# Create a function for help
def help():
    #A window popup to show the help message
    tkinter.messagebox.showinfo(title='Help',message='This is a simple todo list application')

#Creates a window
window = Tk()
#Set the title of the window
window.title("To-Do List")
#Set Frame
frame =Frame(window)
#Pack the frame
frame.pack()
#Create a listbox
listbox = Listbox(frame,bg="black",fg="white",height=15,width=50,font='helvetica')
listbox.pack(side=tkinter.LEFT)
#Create a scrollbar
scrollbar = Scrollbar(frame)
scrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
#Create a entry button
entry_button = Button(window,text='AddTask',width=50,command=entry_task)
entry_button.pack(pady=3)
#Create a delete button
delete_button = Button(window,text='DeleteTask',width=50,command=deletetask)
delete_button.pack(pady=3)
#Create a mark button
mark_button = Button(window,text='Mark As Complete',width=50,command=marktask)
mark_button.pack(pady=3)
#Create a clear button
clear_button = Button(window,text='Clear All',width=50,command=clearall)
clear_button.pack(pady=3)
#Create a save button
save_button = Button(window,text='Save',width=50,command=save)
save_button.pack(pady=3)
#Create a open button
open_button = Button(window,text='Open',width=50,command=openfile)
open_button.pack(pady=3)
#Create a save as button
saveas_button = Button(window,text='Save As',width=50,command=saveas)
saveas_button.pack(pady=3)
#Create a open as button
openas_button = Button(window,text='Open As',width=50,command=openas)
openas_button.pack(pady=3)
#Create a about button
about_button = Button(window,text='About',width=50,command=about)
about_button.pack(pady=3)
#Create a help button
help_button = Button(window,text='Help',width=50,command=help)
help_button.pack(pady=3)
#Create a exit button
exit_button = Button(window,text='Exit',width=50,command=exit)
exit_button.pack(pady=3)

window.mainloop()


