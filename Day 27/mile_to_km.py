import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20) #add space around the edges

#Entry
input = tkinter.Entry(width = 10)
input.grid(column=1, row=0)

#Label
label_1 = tkinter.Label(text = "Miles")
label_1.grid(column=2, row=0)

label_2 = tkinter.Label(text = "is equal to")
label_2.grid(column=0, row=1)

label_output = tkinter.Label(text = "0")
label_output.grid(column=1, row=1)

label_3 = tkinter.Label(text = "Km")
label_3.grid(column=2, row=1)

#Button
def button_click():
    input_miles = float(input.get())
    convert_km = input_miles * 1.609
    label_output.config(text=f"{convert_km}")

button = tkinter.Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)





window.mainloop()