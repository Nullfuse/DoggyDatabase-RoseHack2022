import tkinter as tk
from tkinter import Entry
from tkinter import ttk
from tkinter import Scrollbar
from tkinter import IntVar
from tkinter import Radiobutton
from PIL import Image,ImageTk
import DogData

doglist = []
DogData.readList(doglist)

def show_frame(frame):
    frame.tkraise()
    
window = tk.Tk()
window.geometry('400x300')
window.attributes('-zoomed', True)
window.title('Dog Adoption Center')
window['bg']='#D3E4E4'

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
frame3 = tk.Frame(window)
frame4 = tk.Frame(window)
frame5 = tk.Frame(window)
frame6 = tk.Frame(window)

for frame in (frame1, frame2, frame3, frame4, frame5, frame6):
    frame.grid(row=0,column=0,sticky='nsew')
    
f = ("Times bold", 14)
t = ("Times bold", 35)

#==================Main Page Code (Frame 1)
frame1_title = tk.Label(frame1, text='Welcome', font=t, padx=10, pady=10, bg='#D3E4E4')
frame1_title.pack(fill='both', expand=True)

frame1_addadog_btn = tk.Button(frame1, text='Add a Dog', font = f, command=lambda:show_frame(frame2))
frame1_addadog_btn.pack(fill='both', expand=True, side=tk.LEFT)

frame1_viewalldogs_btn = tk.Button(frame1, text='View all Dogs', font = f, command=lambda:show_frame(frame4))
frame1_viewalldogs_btn.pack(fill='both', expand=True, side=tk.LEFT)

frame1_deleteadog_btn = tk.Button(frame1, text='Remove a Dog', font = f, command=lambda:show_frame(frame3))
frame1_deleteadog_btn.pack(fill='both', expand=True, side=tk.LEFT)

#==================Add a Dog Page (Frame 2)
frame2_title= tk.Label(frame2, text='Add a Dog', font='times 24 bold')
frame2_title.grid(row = 0, column = 1, padx = 50, pady = 50, columnspan='3')

frame2_name = tk.Label(frame2, text='Dog Name', font='times 14')
frame2_name.grid(row = 1, column = 1, padx = 5, pady = 5)

frame2_breed = tk.Label(frame2, text='Dog Breed', font='times 14')
frame2_breed.grid(row = 2, column = 1, padx = 5, pady = 5)

frame2_age = tk.Label(frame2, text='Dog Age', font='times 14')
frame2_age.grid(row = 3, column = 1, padx = 5, pady = 5)

frame2_p_name = Entry(frame2, width=30)
frame2_p_name.grid(row = 1, column = 2, padx = 5, pady = 5, columnspan=2)
frame2_p_breed = Entry(frame2, width=30)
frame2_p_breed.grid(row = 2, column = 2, padx = 5, pady = 5, columnspan=2)
frame2_p_age = Entry(frame2, width=30)
frame2_p_age.grid(row = 3, column = 2, padx = 5, pady = 5, columnspan=2)

frame2_rb_val = IntVar()
frame2_rb_val.set(0)

frame2_undetermined_rb = Radiobutton(frame2, text = 'Undetermined', value = 0, variable = frame2_rb_val)
frame2_undetermined_rb.grid(row = 4, column = 1, padx = 5, pady = 5)

frame2_male_rb = Radiobutton(frame2, text = 'Male', value = 1, variable = frame2_rb_val)
frame2_male_rb.grid(row = 4, column = 2, padx = 5, pady = 5)

frame2_female_rb = Radiobutton(frame2, text = 'Female', value = 2, variable = frame2_rb_val)
frame2_female_rb.grid(row = 4, column = 3, padx = 5, pady = 5)

frame2_previous_btn = tk.Button(frame2, text='Previous Page',command=lambda:show_frame(frame1))
frame2_previous_btn.grid(row = 5, column = 0, padx = 10, pady = 10)

def submit_add():
  DogData.addDog(doglist, [frame2_p_name.get(), frame2_p_age.get(), DogData.dog_gender(frame2_rb_val.get()), frame2_p_breed.get()])
  frame2_p_name.delete(0, 'end')
  frame2_p_breed.delete(0, 'end')
  frame2_p_age.delete(0, 'end')
  frame2_rb_val.set(0)
  show_frame(frame5)

frame2_submit_btn = tk.Button(frame2, text='Submit',command=lambda:submit_add())
frame2_submit_btn.grid(row = 5, column = 4, padx = 50, pady = 50)

#==================Delete a Dog Page (Frame 3)
frame3_title= tk.Label(frame3, text='Remove a Dog', font='times 24 bold')
frame3_title.grid(row = 0, column = 1, padx = 50, pady = 50, columnspan='3')

frame3_name = tk.Label(frame3, text='Dog Name', font='times 14')
frame3_name.grid(row = 1, column = 1, padx = 5, pady = 5)

frame3_breed = tk.Label(frame3, text='Dog Breed', font='times 14')
frame3_breed.grid(row = 2, column = 1, padx = 5, pady = 5)

frame3_age = tk.Label(frame3, text='Dog Age', font='times 14')
frame3_age.grid(row = 3, column = 1, padx = 5, pady = 5)

frame3_p_name = Entry(frame3, width=30)
frame3_p_name.grid(row = 1, column = 2, padx = 5, pady = 5, columnspan=2)
frame3_p_breed = Entry(frame3, width=30)
frame3_p_breed.grid(row = 2, column = 2, padx = 5, pady = 5, columnspan=2)
frame3_p_age = Entry(frame3, width=30)
frame3_p_age.grid(row = 3, column = 2, padx = 5, pady = 5, columnspan=2)

frame3_rb_val = IntVar()
frame3_rb_val.set(0)

frame3_undetermined_rb = Radiobutton(frame3, text = 'Undetermined', value = 0, variable = frame3_rb_val)
frame3_undetermined_rb.grid(row = 4, column = 1, padx = 5, pady = 5)

frame3_male_rb = Radiobutton(frame3, text = 'Male', value = 1, variable = frame3_rb_val)
frame3_male_rb.grid(row = 4, column = 2, padx = 5, pady = 5)

frame3_female_rb = Radiobutton(frame3, text = 'Female', value = 2, variable = frame3_rb_val)
frame3_female_rb.grid(row = 4, column = 3, padx = 5, pady = 5)

frame3_previous_btn = tk.Button(frame3, text='Previous Page',command=lambda:show_frame(frame1))
frame3_previous_btn.grid(row = 5, column = 0, padx = 10, pady = 10)

def submit_remove():
  DogData.deleteDog(doglist, [frame3_p_name.get(), frame3_p_age.get(), DogData.dog_gender(frame3_rb_val.get()), frame3_p_breed.get()])
  frame3_p_name.delete(0, 'end')
  frame3_p_breed.delete(0, 'end')
  frame3_p_age.delete(0, 'end')
  frame3_rb_val.set(0)
  show_frame(frame6)
  
frame3_submit_btn = tk.Button(frame3, text='Submit',command=lambda:submit_remove())
frame3_submit_btn.grid(row = 5, column = 4, padx = 50, pady = 50)

#==================View all Dogs Page Code (Frame 4)
frame4_btn = tk.Button(frame4, text='Home',command=lambda:show_frame(frame1))
frame4_btn.pack(fill='x', expand='TRUE', side='top', anchor = "w")

tv = ttk.Treeview(frame4, columns=(1, 2, 3, 4), show='headings', height=15)
tv.pack(side='left', fill='both', expand='TRUE')

tv.heading(1, text="Name")
tv.heading(2, text="Breed")
tv.heading(3, text="Age")
tv.heading(4, text="Gender")

sb = Scrollbar(frame4, orient='vertical')
sb.pack(side='right', fill='y')

tv.config(yscrollcommand=sb.set)
sb.config(command=tv.yview)

for i in range(len(doglist)):
  tv.insert(parent='', index=i, iid=i, values=(doglist[i].name, doglist[i].breed,doglist[i].age, doglist[i].gender))

#==================Add a Dog Confirmation Page (Frame 5)    
frame5_title = tk.Label(frame5, text="Confirmed - Dog has been Added", font = f, padx=20,pady=20,bg='#bfff00')
frame5_title.pack(fill='both', expand=True)

frame5_btn = tk.Button(frame5, text="Home", font=f, command=lambda:show_frame(frame1))
frame5_btn.pack(fill='x', expand='TRUE', side='right')

#==================Delete a Dog Confirmation Page (Frame 6)    
frame6_title = tk.Label(frame6, text="Confirmed - Dog has been Deleted", font = f, padx=20,pady=20,bg='#bfff00')
frame6_title.pack(fill='both', expand=True)

frame6_btn = tk.Button(frame6, text="Home", font=f, command=lambda:show_frame(frame1))
frame6_btn.pack(fill='x', expand='TRUE', side='right')


show_frame(frame1)

window.mainloop()