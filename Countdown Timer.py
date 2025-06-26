import tkinter as tk
import pyttsx3
import time
from tkinter import StringVar, IntVar
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def format_time(seconds):
    return time.strftime('%H:%M:%S', time.gmtime(seconds))

def start_timer():
    if not is_running.get():
        is_running.set(True)
        total = hour_var.get() * 3600 + min_var.get() * 60 + sec_var.get()
        if total > 0:
            countdown(total)

def countdown(remaining):
    if not is_running.get():
        return
    time_display.set(format_time(remaining))
    progress.set((total_time.get() - remaining) / total_time.get() * 100)
    if remaining > 0:
        app.after(1000, countdown, remaining - 1)
    else:
        time_display.set("00:00:00")
        speak("Time's up.")
        progress.set(100)
        is_running.set(False)

def pause_timer():
    is_running.set(False)

def reset_timer():
    is_running.set(False)
    time_display.set("00:00:00")
    progress.set(0)

def prepare_timer():
    t = hour_var.get() * 3600 + min_var.get() * 60 + sec_var.get()
    total_time.set(t)
    time_display.set(format_time(t))
    progress.set(0)

def toggle_dark_mode():
    style.theme_use("darkly" if style.theme.name == "flatly" else "flatly")

app = ttk.Window(themename="flatly")
app.title("Elite Countdown Timer")
app.geometry("500x500")
app.resizable(False, False)

style = ttk.Style()

title = ttk.Label(app, text="⏳ Elite Countdown Timer", font=("Segoe UI", 20, "bold"))
title.pack(pady=15)

frame = ttk.Frame(app)
frame.pack()

hour_var = IntVar(value=0)
min_var = IntVar(value=0)
sec_var = IntVar(value=0)

ttk.Label(frame, text="Hours").grid(row=0, column=0, padx=5)
ttk.Spinbox(frame, from_=0, to=23, textvariable=hour_var, width=5).grid(row=1, column=0, padx=5)

ttk.Label(frame, text="Minutes").grid(row=0, column=1, padx=5)
ttk.Spinbox(frame, from_=0, to=59, textvariable=min_var, width=5).grid(row=1, column=1, padx=5)

ttk.Label(frame, text="Seconds").grid(row=0, column=2, padx=5)
ttk.Spinbox(frame, from_=0, to=59, textvariable=sec_var, width=5).grid(row=1, column=2, padx=5)

ttk.Button(app, text="⏱ Prepare", command=prepare_timer, bootstyle=SECONDARY).pack(pady=5)

time_display = StringVar(value="00:00:00")
display_label = ttk.Label(app, textvariable=time_display, font=("Digital-7", 40), foreground="lime")
display_label.pack(pady=15)

progress = tk.DoubleVar()
progressbar = ttk.Floodgauge(app, variable=progress, bootstyle=INFO, mode="determinate", length=400)
progressbar.pack(pady=10)

btn_frame = ttk.Frame(app)
btn_frame.pack(pady=10)

ttk.Button(btn_frame, text="▶ Start", command=start_timer, bootstyle=SUCCESS).grid(row=0, column=0, padx=5)
ttk.Button(btn_frame, text="⏸ Pause", command=pause_timer, bootstyle=WARNING).grid(row=0, column=1, padx=5)
ttk.Button(btn_frame, text="🔄 Reset", command=reset_timer, bootstyle=DANGER).grid(row=0, column=2, padx=5)
ttk.Button(btn_frame, text="🌓 Dark Mode", command=toggle_dark_mode, bootstyle=SECONDARY).grid(row=0, column=3, padx=5)

total_time = IntVar()
is_running = tk.BooleanVar(value=False)

app.mainloop()
