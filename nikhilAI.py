# Nikhil AI 
import tkinter as tk
from datetime import datetime

app = tk.Tk()
app.title("NIKHIL AI")
app.geometry("600x800")
app.configure(bg="#171b26")

heading = tk.Label(
    app,
    text="NIKHIL AI",
    font=("Arial", 22, "bold"),
    bg="#171b26",
    fg="white"
)
heading.pack(pady=15)

chat = tk.Text(
    app,
    height=18,
    bg="#252239",
    fg="white",
    font=("Arial", 11),
    state="disabled"
)
chat.pack(padx=10, pady=10, fill="both", expand=True)

def write_chat(name, text):
    chat.config(state="normal")
    chat.insert("end", name + ": " + text + "\n\n")
    chat.config(state="disabled")
    chat.see("end")

def reply():
    question = box.get().lower().strip()
    box.delete(0, "end")

    if question == "":
        return

    write_chat("You", question)

    if question == "hello" or question == "hi":
        answer = "Hello! Welcome to NIKHIL AI."

    elif "name" in question:
        answer = "My name is NIKHIL AI."

    elif "time" in question:
        answer = datetime.now().strftime("%I:%M %p")

    elif "date" in question:
        answer = datetime.now().strftime("%d-%m-%Y")

    elif question == "help":
        answer = "Try hello, name, time or date."

    else:
        answer = "Mai Abhi Nahi Janta hu Mai Jald Hi Sikh lunga."

    write_chat("NIKHIL AI", answer)

def clear():
    chat.config(state="normal")
    chat.delete("1.0", "end")
    chat.config(state="disabled")
    write_chat("NIKHIL AI", "Chat cleared!")

box = tk.Entry(
    app,
    font=("Arial", 12)
)
box.pack(fill="x", padx=10, pady=5)
box.bind("<Return>", lambda event: reply())

buttons = tk.Frame(app, bg="#171b26")
buttons.pack(pady=8)

tk.Button(
    buttons,
    text="Send",
    command=reply,
    width=12
).pack(side="left", padx=5)

tk.Button(
    buttons,
    text="Clear",
    command=clear,
    width=12
).pack(side="left", padx=5)

write_chat("NIKHIL AI", "Hello! Ask me something.")
box.focus_set()

app.mainloop()