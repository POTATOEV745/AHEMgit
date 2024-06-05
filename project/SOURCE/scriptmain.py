import tkinter as tk
from tkinter import *
from time import *
from PIL import Image, ImageTk

def update_runtime() :
    time_string_runtime = strftime("MAIN CLOCK - %I:%M %p")
    time_runt.config(text=time_string_runtime)
    time_runt.after(6000,
                     update_runtime)

    day_str = strftime("%A")
    day_label.config(text=day_str)

    date_string = strftime("%B / %d / %Y")
    date_label.config(text=date_string)


def update_ANN():
    text = entry_var.get()
    INP_ANN_var.set(text)

AHEM = tk.Tk()

AHEM.geometry("800x500")
AHEM.title("AHEMsystem_alpha1 demo")

AHEM.background_image = Image.open("asset2.png")  # Replaceimage file
AHEM.background_photo = ImageTk.PhotoImage(AHEM.background_image)

        # Create a label with the background image
AHEM.background_label = tk.Label(AHEM, image=AHEM.background_photo)
AHEM.background_label.place(x=0, y=0, relwidth=1, relheight=1)

time_runt = Label(AHEM, font=("Arial", 40), fg="#7AD5CB", bg="yellow")
time_runt.pack()

day_label = Label(AHEM, font=("Franklin Gothic Heavy", 25))
day_label.pack()

AHEMLABEL = tk.Label(AHEM, text="AHEM system", font=('Arial', 10, 'bold'))
AHEMLABEL.pack()

entry_var = tk.StringVar()

Workframe = Frame(AHEM)
Workframe.pack()

date_label = Label(Workframe, font=("Franklin Gothic Heavy", 25))
date_label.grid(row=0, column=0)

update_runtime()

entry = tk.Entry(Workframe, font=('Helvitica', 16, 'bold'), textvariable=entry_var)
entry.grid(row=0, column=1)

ButtFrame = Frame(AHEM)
ButtFrame.pack()
Announce_UPDATE = tk.Button(ButtFrame, text="Update Output", font=('Franklin Gothic Heavy', 18, 'bold'), command=update_ANN)
Announce_UPDATE.grid(row=0, column=1)

#Second Window, for some reason with the second window running, I can't get the first window to update properly.

def update() :
    time_string = strftime("%I:%M %p")
    time_label.config(text=time_string)
    time_label.after(6000,
                     update)

    day_str = strftime("%A")
    day_label.config(text=day_str)

    date_string = strftime("%B / %d / %Y")
    date_label.config(text=date_string)

AHEMOutput = tk.Toplevel()
AHEMOutput.geometry("800x500")
AHEMOutput.title("AHEM System - Output")

AHEMOutput.background_image = Image.open("asset2.png")
AHEMOutput.background_photo = ImageTk.PhotoImage(AHEMOutput.background_image)

AHEMOutput.background_label = tk.Label(AHEMOutput, image=AHEMOutput.background_photo)
AHEMOutput.background_label.place(x=0, y=0, relwidth=1, relheight=1)

time_label = tk.Label(AHEMOutput, font=("Arial", 300), fg="#7AD5CB", bg="yellow")
time_label.pack(pady=60)

day_label = Label(AHEMOutput,
                  font=("Franklin Gothic Heavy",
                        25),fg="#FFE922", bg="#0076D6")
day_label.pack()


Workframe1 = Frame(AHEMOutput, bg="#0040D6")
Workframe1.pack()

date_label = Label(Workframe1,
                   font=("Franklin Gothic Heavy",
                         25),fg="#FFE922", bg="#0040D6")
date_label.grid(row=0,
                column=0,
                )

INP_ANN_var = tk.StringVar()
label = tk.Label(AHEMOutput,
                 font=('Helvitica', 70, 'bold'),
                 fg="#FEFF4C",
                 bg="#7AD5CB",
                 textvariable=INP_ANN_var)
label.pack()



update()

AHEM.mainloop()

