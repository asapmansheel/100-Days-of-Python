from tkinter import *

window = Tk()
window.title('Mile to KM Converter')
window.minsize(width=500, height=300)

input = Entry(width=10)
input.grid(column=1,row=1)

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=1)

equal_label = Label(text='is equal to')
equal_label.grid(column=0,row=2)

answer_label = Label(text='0')
answer_label.grid(column=1, row=2)

km_label = Label(text='km')
km_label.grid(column=2,row=2)

def click_button():
    miles = int(input.get())
    km = miles * 1.60934
    answer_label['text'] = str(km)
    
button = Button(text='Calculate', command=click_button)
button.grid(column=1,row=3)

# Keeps the window on screen
window.mainloop() # This line of code has to be at the very end of the program
