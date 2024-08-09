from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    #timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    #title_label "Timer"
    label_timer.config(text="Timer")
    #reset check marks
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def button_click_start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        label_timer.config(text="Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 40))
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label_timer.config(text="Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 40))
        count_down(short_break_sec)
    else:
        label_timer.config(text="Work", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40))
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        button_click_start()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,132, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

label_timer = Label(text = "Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40))
label_timer.grid(column=1, row=0)

button_start = Button(text="Start", command=button_click_start, highlightthickness=0)
button_start.grid(column=0, row=2)

def button_click_reset():
    return

button_reset = Button(text="Reset", command=reset_timer, highlightthickness=0)
button_reset.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()