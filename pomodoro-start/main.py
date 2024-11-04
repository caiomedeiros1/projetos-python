from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
reps = 0
timer_seconds = None
timer_minutes = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    reps = 0
    
    if timer_seconds is not None:
        window.after_cancel(timer_seconds)
        
    if timer_minutes is not None:
        window.after_cancel(timer_minutes)
        
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="TIMER", fg=GREEN)
    checkmark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(0, 3) #19 59
        timer.config(text="Rest", fg=RED)
        checkmark.config(text="✔"*(reps//2))
        
    elif reps % 2 == 1:
        count_down(0, 3) #24 59
        timer.config(text="Work", fg=PINK)
    else:
        count_down(0, 3) #4 59
        timer.config(text="Rest", fg=GREEN)
        checkmark.config(text="✔"*(reps//2))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(minute, second):
    if second < 10:
        second_str = f"0{second}"
    else:
        second_str = str(second)

    if minute < 10:
        minute_str = f"0{minute}"
    else:
        minute_str = str(minute)

    canvas.itemconfig(timer_text, text=f"{minute_str}:{second_str}")

    if minute == 0 and second == 0:
        start_timer()

    if second > 0:
        global timer_seconds
        timer_seconds = window.after(1000, count_down, minute, second-1)

    elif second == 0:
        if minute > 0:
            global timer_minutes
            timer_minutes = window.after(1000, count_down, minute-1, 59)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

timer = Label(text="TIMER", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
timer.grid(row=0, column=1)

checkmark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmark.grid(row=3, column=1)

start = Button(text="START", command=start_timer)
start.grid(row=2, column=0)

reset = Button(text="RESET", command=reset_timer)
reset.grid(row=2, column=2)

window.mainloop()