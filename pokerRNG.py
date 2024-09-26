# imports
import tkinter as tk 
import customtkinter
import random

def generate_number():
    number = random.randint(1, 100)
    rngnumber.configure(text=str(number)) 

    if number < 26:
        rngnumber.configure(text_color="red")
    elif number < 76:
        rngnumber.configure(text_color="yellow")
    else:
        rngnumber.configure(text_color="green")

def timedmode_toggle():
    current_mode = main_menu.entrycget(2, "label")

    if current_mode == "Timed mode off":
        main_menu.entryconfig(2, label="Timed mode on")
        main_menu.entryconfig(2, background="white", activebackground="white")
    else:
        main_menu.entryconfig(2, label="Timed mode off", background="#d9d8d8", activebackground="#edeced")

    
    
# Custom Tkinter theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Create main window
root = customtkinter.CTk()
root.title("RNG")
root.geometry("250x200")
root.attributes("-topmost", True)

# Create the frame
frame = customtkinter.CTkFrame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create main menu
main_menu = tk.Menu(root)
root.config(menu=main_menu)
menu_font = ("Ubuntu", 8)

# Create options menu
options_menu = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label = "Options", font=menu_font, menu=options_menu)

# Create sub menu for RNG Mode
rngmode_menu = tk.Menu(options_menu, tearoff=False)
options_menu.add_cascade(label="RNG Mode", font=menu_font, menu=rngmode_menu)
rngmode_menu.add_command(label="Low RNG", font=menu_font, command=lambda: print("Low RNG"))
rngmode_menu.add_command(label="High RNG", font=menu_font, command=lambda: print("High RNG"))

# timedmode_menu = tk.Menu(main_menu, tearoff=False)
main_menu.add_command(label="Timed mode off", font=menu_font, command=timedmode_toggle)

# Label for the RNG number
rngnumber = customtkinter.CTkLabel(frame)
rngnumber.configure(text="", text_color="white", font=("Ubuntu", 95))
rngnumber.pack(expand=True)

# RNG Button to RNG the rngnumber
button = customtkinter.CTkButton(frame,
                                 text="RNG",
                                 text_color="white", 
                                 font=("Ubuntu", 20), 
                                 width=150,
                                 height=50,
                                 command=generate_number)
button.pack(side="bottom", fill="x")

root.mainloop()



