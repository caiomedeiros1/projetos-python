from tkinter import *

window = Tk()
window.title("Mile to KM converter")
window.config(padx=20, pady=20)

entry_distance_miles = Entry()
entry_distance_miles.grid(row=0, column=1)

label_miles = Label(text="miles")
label_miles.grid(row=0, column=2)

label_is_equal = Label(text="is equal to")
label_is_equal.grid(row=1, column=0)

label_distance_km = Label(text="0")
label_distance_km.grid(row=1, column=1)

label_km = Label(text="Km")
label_km.grid(row=1, column=2)

def button_calculate_clicked ():
    new_text = float(entry_distance_miles.get()) * 1.609
    label_distance_km.config(text=new_text)

button_calculate = Button(text="Calculate", command=button_calculate_clicked)
button_calculate.grid(row=2, column=1)



window.mainloop()