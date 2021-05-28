from tkinter import *
from tkinter.font import Font
root= Tk()
root.title('Simple to-do')
root.geometry('500x500')
my_f = Font( family="Kunstler Script Regular",size=10,weight="bold")
my_frame=Frame(root)
my_frame.pack(pady=10)
my_list=Listbox(my_frame,
                font=my_f ,
                width=25 ,
                height=5,
                bg="light grey",bd=0,
                fg="black",
                highlightthickness=0,
                selectbackground="brown",
                activestyle="none"
                )
my_list.pack()
todo=["Study","Workout","Stay Hydrated"]
for item in todo:
    my_list.insert(END, item)
my_entertodo=Entry(root,font=("Kunstler Script Regular",10))
my_entertodo.pack(pady=20)
b_frame=Frame(root)
b_frame.pack(pady=20)
def delete_this():
    my_list.delete(ANCHOR)
def add_this():
    my_list.insert(END, my_entertodo.get())

def done_this():
    my_list.itemconfig(
        my_list.curselection(),
        fg="white")
#used to not show selection bar
    my_list.selection_clear(0,END)
delete_b=Button(b_frame,text="Delete item", command=delete_this)
add_b=Button(b_frame,text="Add item", command=add_this)
done_b=Button(b_frame,text="Done this", command=done_this)
delete_b.grid(row=0,column=0,padx=10)
add_b.grid(row=0,column=1,padx=10)
done_b.grid(row=0,column=2,padx=10)
root.mainloop()
             