from tkinter import *
import backend

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    e5.delete(0,END)
    e5.insert(END,selected_tuple[5])
    e6.delete(0,END)
    e6.insert(END,selected_tuple[6])

def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(student_Name_text.get(), study_field_text.get(),year_text.get(), scientific_work_text.get(), supervisor_text.get(),mark_text.get()):
        list1.insert(END,row)

def add_command():
    backend.insert(student_Name_text.get(), study_field_text.get(),year_text.get(), scientific_work_text.get(), supervisor_text.get(),mark_text.get())
    list1.delete(0,END)
    list1.insert(END, (student_Name_text.get(), study_field_text.get(),year_text.get(), scientific_work_text.get(), supervisor_text.get(),mark_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],student_Name_text.get(), study_field_text.get(),year_text.get(), scientific_work_text.get(), supervisor_text.get(),mark_text.get())

window=Tk()

window.wm_title("Project of Shaposhnikov")

l1=Label(window, text="Student Name")
l1.grid(row=0, column=0)

l2=Label(window, text="Study Field")
l2.grid(row=0, column=7)

l3=Label(window, text="Year")
l3.grid(row=0, column=12)

l4=Label(window, text="Scientific Work")
l4.grid(row=1,column=0)

l5=Label(window, text="Supervisor Name")
l5.grid(row=1,column=7)

l6=Label(window, text="Mark")
l6.grid(row=1, column=12)

student_Name_text=StringVar()
e1=Entry(window, textvariable=student_Name_text)
e1.grid(row=0,column=3)

study_field_text=StringVar()
e2=Entry(window, textvariable=study_field_text)
e2.grid(row=0,column=9)

year_text=StringVar()
e3=Entry(window, textvariable=year_text)
e3.grid(row=0,column=14)

scientific_work_text=StringVar()
e4=Entry(window, textvariable=scientific_work_text)
e4.grid(row=1,column=3)

supervisor_text=StringVar()
e5=Entry(window, textvariable=supervisor_text)
e5.grid(row=1,column=9)

mark_text=StringVar()
e6=Entry(window, textvariable=mark_text)
e6.grid(row=1,column=14)

list1=Listbox(window, height=10, width=72)
list1.grid(row=2, column=0, rowspan=7, columnspan=11)

sb1=Scrollbar(window)
sb1.grid(row=2, column=12, rowspan=7)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)

b1=Button(window, text="View All", width=13, command=view_command)
b1.grid(row=2, column=14)

b2=Button(window, text="Add Entry", width=13, command=add_command)
b2.grid(row=3, column=14)

b3=Button(window, text="Delete Selected", width=13,command=delete_command)
b3.grid(row=4, column=14)

b4=Button(window, text="Search Entry", width=13, command=search_command)
b4.grid(row=5, column=14)

b5=Button(window, text="Update Selected", width=13, command=update_command)
b5.grid(row=6, column=14)

b6=Button(window, text="Close", width=13, command=window.destroy)
b6.grid(row=7, column=14)

window.mainloop()
