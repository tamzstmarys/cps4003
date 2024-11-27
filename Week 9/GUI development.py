import tkinter as tk
from tkinter import messagebox

widgets = {}


def setup_window():
    window = tk.Tk()
    window.geometry("300x100")
    window.title("Subscribe")
    window.config(bg="#eef")
    return window


def add_components(window):
    add_email_label(window)
    add_subscribe_button(window)
    add_email_entry(window)
    add_email_label(window)


def add_email_label(window):
    email_label = tk.Label(window)
    email_label.grid(row=0, column=0)
    email_label.config(text="Email: ", background="#b6ed9b")


def run():
    window = setup_window()
    add_components(window)
    window.mainloop()


def add_email_entry(window):
    email_entry = tk.Entry(window)
    email_entry.grid(row=0, column=1)
    widgets["email_entry"] = email_entry


def add_subscribe_button(window):
    subscribe_button = tk.Button(window)
    subscribe_button.grid(row=1, column=0, columnspan=2, sticky="EW")
    subscribe_button.config(text="Subscribe")
    subscribe_button.bind('<ButtonRelease-1>', subscribe_button_clicked)


def subscribe_button_clicked(event):
    email = widgets["email_entry"].get()
    messagebox.showinfo("Subscribed!",
                        f"You have successfully subbed with {email}")


run()
