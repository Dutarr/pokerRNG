# imports
import tkinter as tk
import customtkinter
import random

highrng_on = False

def change_font_size(change):
    global default_font_size
    default_font_size += change
    rng_number.configure(font=("Ubuntu", default_font_size))

def focus_mode_toggle():
    global current_focusmode
    current_focusmode = popup_menu.entrycget(0, "label")

    if current_focusmode == "Focus mode (off)":
        popup_menu.entryconfig(0, label="Focus mode (on)")
        popup_menu.entryconfig(0, background="white", activebackground="white")
        root.config(menu='')
        root.overrideredirect(False)
        rng_button.pack_forget()
    else:
        popup_menu.entryconfig(0, label="Focus mode (off)", background="#d9d8d8", activebackground="#edeced")
        root.config(menu=main_menu)
        root.overrideredirect(True)
        rng_button.pack(side="bottom", fill="x")

def toggle_menubar():
    if root.cget('menu') == '':
        root.config(menu=main_menu)
    else:
        root.config(menu='')

def toggle_borders():
    if root.overrideredirect():
        root.overrideredirect(False)
    else:
        root.overrideredirect(True)

def do_popup(event):
    try:
        popup_menu.tk_popup(event.x_root, event.y_root)
    finally:
        popup_menu.grab_release()

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
    rng_number.configure(text=str(number)) 

    if highrng_on:
        if number < 26:
            rng_number.configure(text_color="green")
        elif number < 76:
            rng_number.configure(text_color="yellow")
        else:
            rng_number.configure(text_color="red")
    else:
        if number < 26:
            rng_number.configure(text_color="red")
        elif number < 76:
            rng_number.configure(text_color="yellow")
        else:
            rng_number.configure(text_color="green")

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
root.overrideredirect(False)

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
default_font_size = 95 
rng_number = customtkinter.CTkLabel(frame)
rng_number.configure(text="", text_color="white", font=("Ubuntu", default_font_size))
rng_number.pack(expand=True)

# RNG Button to RNG the rngnumber
rng_button = customtkinter.CTkButton(frame,
                                 text="RNG",
                                 text_color="white", 
                                 font=("Ubuntu", 30), 
                                 width=150,
                                 height=50,
                                 fg_color="#b87d02",
                                 hover_color="#976807",
                                 command=generate_number)
rng_button.pack(side="bottom", fill="x")

# Create popup menu
popup_menu = tk.Menu(root, tearoff=False) 
popup_menu.add_command(label="Focus Mode", command=focus_mode_toggle)
popup_menu.add_command(label="Toggle borders", command=toggle_borders)
popup_menu.add_command(label="Toggle menu", command=toggle_menubar)
popup_menu.add_separator()
popup_menu.add_command(label="Increase font", command=lambda:change_font_size(+20))
popup_menu.add_command(label="Decrease font", command=lambda:change_font_size(-20))
popup_menu.add_separator()
popup_menu.add_command(label="Exit", command=root.quit)

# Bind right click for popup menu
root.bind("<Button-3>", do_popup)

root.mainloop()



