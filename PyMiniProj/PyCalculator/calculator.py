import tkinter  # GUI library for creating windows, buttons, labels, etc.
import math     # Math library for mathematical operations like sqrt()

'''
Simple Calculator with GUI using tkinter
- tkinter: Python's standard GUI (Graphical User Interface) library
- Provides widgets: Tk (window), Frame (container), Label (text display), Button (clickable)
'''

# === DATA SETUP ===
# 2D list defining calculator layout: 5 rows × 4 columns
# Each inner list = one row of buttons
button_values = [
    ["AC", "+/-", "%", "÷"],   # Row 1: Clear, negate, percent, divide
    ["7", "8", "9", "×"],      # Row 2: Numbers 7-9, multiply
    ["4", "5", "6", "-"],      # Row 3: Numbers 4-6, subtract
    ["1", "2", "3", "+"],      # Row 4: Numbers 1-3, add
    ["0", ".", "√", "="]       # Row 5: Zero, decimal, square root, equals
]

# Categorize buttons for color coding and behavior
right_symbols = ["÷", "×", "-", "+", "="]  # Math operator buttons (orange)
top_symbols = ["AC", "+/-", "%"]           # Utility function buttons (light gray)

row_count = len(button_values)        # Total rows = 5
column_count = len(button_values[0])  # Total columns = 4

# === COLOR SCHEME ===
# Hex color codes for visual distinction
color_light_gray = "#D4D4D2"  # Utility buttons (AC, +/-, %)
color_black = "#1C1C1C"       # Display screen background
color_dark_gray = "#505050"   # Number buttons (0-9, .)
color_white = "white"         # Text color for buttons
color_orange = "#FF9500"      # Operator buttons (÷, ×, -, +, =)

# === WINDOW SETUP ===
# Create main application window
window = tkinter.Tk()  
# Tk() creates the root window object - the main container for all widgets

window.title("Calculator")  
# title(string) - Sets the window title shown in title bar

window.resizable(False, False)  
# resizable(width_bool, height_bool) - Prevents window from being resized
# False, False = user cannot resize width or height

# === DISPLAY SCREEN ===
# Frame: Container widget that holds other widgets (label + buttons)
frame = tkinter.Frame(window)  
# Frame(parent) - Creates container inside 'window'

# Label: Text display widget (the calculator screen)
label = tkinter.Label(
    frame,                      # parent - Widget is placed inside 'frame'
    text="0",                   # text - Initial display content
    font=("Arial", 45),         # font - Tuple: (font_family, size)
    background=color_black,     # background - Background color (hex or name)
    foreground=color_white,     # foreground - Text color
    anchor="e",                 # anchor - Text alignment: "e" = East (right-align)
                                # Options: "n", "s", "e", "w", "center", "ne", "nw", "se", "sw"
    width=column_count          # width - Width in characters (not pixels)
)

# Grid layout manager: Positions widgets in rows/columns
label.grid(
    row=0,                      # row - Grid row position (0-based)
    column=0,                   # column - Grid column position (0-based)
    columnspan=column_count,    # columnspan - Number of columns to span (4 columns)
    sticky="we"                 # sticky - Stretch direction: "we" = West-East (horizontal stretch)
                                # Options: "n", "s", "e", "w" or combinations like "nsew", "we"
)

# === CALCULATOR STATE ===
# Global variables to store calculation state
# Example: User enters "5 + 3 =" → A="5", operator="+", B="3"
A = "0"          # First operand (stored as string)
operator = None  # Current operator: "+", "-", "×", "÷" (None when no operator selected)
B = None         # Second operand (stored as string, None until operator pressed)

# === HELPER FUNCTIONS ===

def clear_all():
    """
    Reset all calculator state variables to initial values
    Called when: User presses AC or after calculation completes
    """
    global A, B, operator  # Access global variables
    A = "0"
    operator = None
    B = None

def remove_zero_decimal(num):
    """
    Clean up display by removing unnecessary decimal points
    
    Args:
        num (float): Number to clean up
    
    Returns:
        str: Cleaned number as string
    
    Examples:
        5.0 → "5"    (removes .0)
        5.5 → "5.5"  (keeps decimal)
    
    Logic:
        num % 1 gives the decimal part
        If decimal part == 0, number is whole → convert to int
    """
    if num % 1 == 0:      # Check if decimal part is zero
        num = int(num)    # Convert float to int (5.0 → 5)
    return str(num)       # Return as string for display

# === BUTTON CLICK HANDLER ===

def button_clicked(value):
    """
    Main event handler for all button clicks
    
    Args:
        value (str): The text of the button that was clicked
                     Examples: "7", "+", "AC", "="
    
    Design Logic:
        1. Categorize button type (operator, function, or digit)
        2. Execute corresponding action
        3. Update display (label["text"])
    
    Flow:
        - Operators (÷,×,-,+,=) → Perform math or store for later
        - Functions (AC,+/-,%,√) → Transform current number
        - Digits (0-9,.) → Build number on display
    """
    global right_symbols, top_symbols, label, A, B, operator

    # === CASE 1: OPERATOR BUTTONS (÷, ×, -, +, =) ===
    if value in right_symbols:
        
        # --- EQUALS BUTTON (=): Execute calculation ---
        if value == "=":
            # Only calculate if we have complete expression: A [operator] B
            if A is not None and operator is not None:
                B = label["text"]    # Get second number from current display
                numA = float(A)      # Convert string to float for math
                numB = float(B)

                # Perform calculation based on stored operator
                if operator == "+":
                    result = numA + numB
                elif operator == "-":
                    result = numA - numB
                elif operator == "×":
                    result = numA * numB
                elif operator == "÷":
                    # Division by zero protection
                    result = numA / numB if numB != 0 else 0
                
                # Update display with result and clean it up
                label['text'] = remove_zero_decimal(result)
                clear_all()  # Reset for next calculation

        # --- OPERATOR BUTTONS (+, -, ×, ÷): Store first number and operator ---
        elif value in "+-×÷":
            if operator is None:       # First operator pressed (start of expression)
                A = label["text"]      # Save current display as first operand
                label["text"] = "0"    # Clear display for second number input
                B = "0"                # Initialize second operand
            
            operator = value           # Store which operator was pressed


    # === CASE 2: FUNCTION BUTTONS (AC, +/-, %, √) ===
    elif value in top_symbols or value == "√":
        
        # --- AC (All Clear): Reset calculator ---
        if value == 'AC':
            clear_all()             # Reset A, B, operator to initial state
            label["text"] = "0"     # Clear display
        
        # --- +/- (Negate): Flip sign of current number ---
        elif value == "+/-":
            result = float(label["text"]) * -1  # Multiply by -1 (5 → -5, -5 → 5)
            label["text"] = remove_zero_decimal(result)
        
        # --- % (Percent): Convert to percentage ---
        elif value == "%":
            result = float(label["text"]) / 100  # Divide by 100 (50 → 0.5)
            label["text"] = remove_zero_decimal(result)
        
        # --- √ (Square Root): Calculate square root ---
        elif value == "√":
            num = float(label["text"])
            if num >= 0:  # Only calculate for non-negative numbers
                result = math.sqrt(num)  # math.sqrt() from math library
                label["text"] = remove_zero_decimal(result)

    # === CASE 3: DIGIT BUTTONS (0-9) or DECIMAL (.) ===
    else:
        
        # --- DECIMAL POINT (.) ---
        if value == ".":
            # Only add decimal if one doesn't already exist (prevent "5.2.3")
            if value not in label["text"]:
                label["text"] += value   # Append decimal point
        
        # --- DIGIT BUTTONS (0-9) ---
        elif value in "0123456789":
            # Special case: Replace leading "0" to avoid "05", "007"
            if label["text"] == "0":
                label["text"] = value    # Replace "0" with digit
            else:
                label['text'] += value   # Append digit to existing number

# === BUTTON CREATION ===
for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(
            frame, 
            text=value, 
            font=("Arial", 30), 
            width=column_count-1, 
            height=1, 
            command=lambda value=value: button_clicked(value)
        )
        
        if value in top_symbols:
            button.config(foreground=color_black, background=color_light_gray)
        elif value in right_symbols:
            button.config(foreground=color_white, background=color_orange)
        else:
            button.config(foreground=color_white, background=color_dark_gray)
        
        button.grid(row=row+1, column=column)

frame.pack()

# === CENTER WINDOW ===
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

window.mainloop()
