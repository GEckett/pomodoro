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
marks = []
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    global reps
    global marks
    marks = []
    reps = 0
    timer_label.config(text="Timer", fg=GREEN)
    pom_count.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps == 0 or reps == 2 or reps == 4 or reps == 6:
        pom_time = work_sec
        timer_label.config(text="Work", fg=GREEN)
    elif reps == 1 or reps == 3 or reps == 5:
        pom_time = short_break_sec
        timer_label.config(text="Break", fg=PINK)
        marks.append("✔")
        pom_count.config(text="".join(marks))
    elif reps == 7:
        pom_time = long_break_sec
        timer_label.config(text="Break", fg=RED)
        marks.append("✔")
        pom_count.config(text="".join(marks))
    count_down(pom_time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global reps
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(10, count_down, count-1)
    elif count == 0 and reps < 8:
        reps += 1
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)



#tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112,image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00",fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=2)

#Labels

timer_label = Label(text="Timer", font=(FONT_NAME, 30), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=2)

pom_count = Label(text="", font=(FONT_NAME, 10), fg=GREEN, bg=YELLOW)
pom_count.grid(row=4, column=2)

#Buttons

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=3, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=3, column=3)



window.mainloop()