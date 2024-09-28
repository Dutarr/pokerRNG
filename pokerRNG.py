# imports
import tkinter as tk
import customtkinter
import random

highrng_on = False

def update_cycle():
    global cycle_running
    current_mode = main_menu.entrycget(2, "label")
    if current_mode == "Timed mode (off)":
        main_menu.entryconfig(2, label="Timed mode (on)")
        main_menu.entryconfig(2, background="white", activebackground="white")
        cycle_running = True
        start_cycle()
    else:
        pass


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
    global cycle_running
    refresh_time_ms = selected_refreshtime.get()
    if cycle_running:
        rng_button.invoke()
        root.after(refresh_time_ms, run_cycle)

def toggle_cycle():
    global cycle_running
    if current_mode == "Timed mode (off)":
        cycle_running = False
    else:
        cycle_running = True

def start_cycle():
    refresh_time_ms = selected_refreshtime.get()
    if cycle_running:
        generate_number()
        root.after(refresh_time_ms, run_cycle)

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
menu_font = ("Ubuntu", 7)

# Create High RNG button 
main_menu.add_command(label = "High RNG (off)", font=menu_font, command=highrng_toggle)

# Create Timemode toggle button
main_menu.add_command(label="Timed mode (off)", font=menu_font, command=timedmode_toggle)

# Create Timemode settings menu
timedmode_settings = tk.Menu(main_menu, tearoff=False)

# Create list of selectable refresh times
main_menu.add_cascade(label="Refresh time", font=menu_font, menu=timedmode_settings)

# Selected refresh time 
global selected_refreshtime
selected_refreshtime = tk.IntVar(value=3000)

#Create Refresh times
timedmode_settings.add_radiobutton(label="1sec", variable=selected_refreshtime, value=1000, command=update_cycle)
timedmode_settings.add_radiobutton(label="2sec", variable=selected_refreshtime, value=2000, command=update_cycle)
timedmode_settings.add_radiobutton(label="3sec", variable=selected_refreshtime, value=3000, command=update_cycle)
timedmode_settings.add_radiobutton(label="4sec", variable=selected_refreshtime, value=4000, command=update_cycle)
timedmode_settings.add_radiobutton(label="5sec", variable=selected_refreshtime, value=5000, command=update_cycle)
timedmode_settings.add_radiobutton(label="6sec", variable=selected_refreshtime, value=6000, command=update_cycle)
timedmode_settings.add_radiobutton(label="7sec", variable=selected_refreshtime, value=7000, command=update_cycle)
timedmode_settings.add_radiobutton(label="8sec", variable=selected_refreshtime, value=8000, command=update_cycle)
timedmode_settings.add_radiobutton(label="9sec", variable=selected_refreshtime, value=9000, command=update_cycle)

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



