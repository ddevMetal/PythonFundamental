import tkinter

'''
https://www.youtube.com/watch?v=28tj-IBfGH4

14:40
24:10 <-- last

'''

# Game setup
button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values) #5
column_count = len(button_values[0]) #4

color_light_gray = "#D4D4D2"
color_black = "#1C1C1C"
color_dark_gray = "#505050"
color_white = "white"
color_orange = "#FF9500"

# window setup 
window = tkinter.Tk() # create the window
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", 
                             font=("Arial", 45), 
                             background=color_black, 
                             foreground=color_white, 
                             anchor="e",
                             width=column_count)

label.grid(row=0, 
           column=0, 
           columnspan=column_count, 
           sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, 
                                text=value, 
                                font=("Arial", 30), 
                                width=column_count-1, 
                                height=1, 
                                command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.config(foreground=color_black, 
                          background=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, 
                          background=color_orange)
        else:
            button.config(foreground=color_white, 
                          background=color_dark_gray)
        button.grid(row=row+1, 
                    column=column)

frame.pack()

#A+B, A-B, A*B, A/B
A = "0"
operator = None
B = None


def button_clicked(value):
    global right_symbols, top_symbols, label, A, B, operator

    if value in right_symbols:
        pass
    elif value in top_symbols:
        pass
    else: #digits or .
        # 2 category
        if value ==".":
            if value not in label["text"]:
                # if there is one decimal, there can only have one and not more
                label["text"] += value
        elif value in "0123456789":
            if label ["text"] == "0": #05 --> #5
                label["text"] = value #replace 0
            else:
                label['text'] += value #append digit

# === CENTER THE WINDOW ON SCREEN ===
# Step 1: Force the window to render and calculate its actual size
window.update()  # Updates the window with all widgets packed inside

# Step 2: Get the window's actual dimensions after widgets are added
window_width = window.winfo_width()    # Get actual window width in pixels
window_height = window.winfo_height()  # Get actual window height in pixels

# Step 3: Get the screen dimensions
screen_width = window.winfo_screenwidth()    # Get monitor width in pixels
screen_height = window.winfo_screenheight()  # Get monitor height in pixels

# Step 4: Calculate position to center the window
# Formula: (screen_size / 2) - (window_size / 2) = offset from top-left corner
window_x = int((screen_width / 2) - (window_width / 2))   # X coordinate (horizontal position)
window_y = int((screen_height / 2) - (window_height / 2)) # Y coordinate (vertical position)

# Step 5: Apply the geometry to position and size the window
# Format: "WIDTHxHEIGHT+X+Y" (no spaces allowed)
# Example: "316x468+1562+486" means 316px wide, 468px tall, at position (1562, 486)
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
