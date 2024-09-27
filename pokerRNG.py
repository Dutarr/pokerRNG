# imports
import tkinter as tk 
import customtkinter
import random

highrng_on = False

def highrng_toggle():
    global current_rngmode
    global highrng_on
    current_rngmode = main_menu.entrycget(1, "label")

    if current_rngmode == "High RNG (off)":
        main_menu.entryconfig(1, label="High RNG (on)")
        main_menu.entryconfig(1, background="white", activebackground="white")
        highrng_on = True
        
    else:
        main_menu.entryconfig(1, label="High RNG (off)", background="#d9d8d8", activebackground="#edeced")
        highrng_on = False

def run_cycle():
    if cycle_running:
        rng_button.invoke()
        root.after(4000, run_cycle)

def toggle_cycle():
    global cycle_running
    if current_mode == "Timed mode off":
        cycle_running = False
    else:
        cycle_running = True
        run_cycle()

def start_cycle():
    if cycle_running:
        generate_number()
        root.after(4000, run_cycle)

def generate_number():
    number = random.randint(1, 100)
    rngnumber.configure(text=str(number)) 

    if highrng_on:
        if number < 26:
            rngnumber.configure(text_color="green")
        elif number < 76:
            rngnumber.configure(text_color="yellow")
        else:
            rngnumber.configure(text_color="red")
    else:
        if number < 26:
            rngnumber.configure(text_color="red")
        elif number < 76:
            rngnumber.configure(text_color="yellow")
        else:
            rngnumber.configure(text_color="green")

def timedmode_toggle():
    global current_mode
    global cycle_running
    current_mode = main_menu.entrycget(2, "label")

    if current_mode == "Timed mode (off)":
        main_menu.entryconfig(2, label="Timed mode (on)")
        main_menu.entryconfig(2, background="white", activebackground="white")
        cycle_running = True
        start_cycle()
        
    else:
        main_menu.entryconfig(2, label="Timed mode (off)", background="#d9d8d8", activebackground="#edeced")
        cycle_running = False
    
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

# Create High RNG button 
# highrng_mode = tk.Menu(main_menu, tearoff=False)
main_menu.add_command(label = "High RNG (off)", font=menu_font, command=highrng_toggle)

# timedmode_menu = tk.Menu(main_menu, tearoff=False)
main_menu.add_command(label="Timed mode (off)", font=menu_font, command=timedmode_toggle)

# Label for the RNG number
rngnumber = customtkinter.CTkLabel(frame)
rngnumber.configure(text="", text_color="white", font=("Ubuntu", 95))
rngnumber.pack(expand=True)

# RNG Button to RNG the rngnumber
rng_button = customtkinter.CTkButton(frame,
                                 text="RNG",
                                 text_color="white", 
                                 font=("Ubuntu", 20), 
                                 width=150,
                                 height=50,
                                 command=generate_number)
rng_button.pack(side="bottom", fill="x")
root.mainloop()



