import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200) #add space around the edges

#Label
my_label = tkinter.Label(text = "I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=1)
#my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.config(padx=50, pady=50)

#Button
def button_click():
    my_label.config(text=input.get())

button = tkinter.Button(text="Please click me", command=button_click)
button.grid(column=2, row=2)

new_button = tkinter.Button(text="New Button")
new_button.grid(column=3, row=1)

#Entry
input = tkinter.Entry(width = 10)
input.grid(column=4, row=3)
#print(input.get())

window.mainloop()