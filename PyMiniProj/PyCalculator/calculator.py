import tkinter  # Import tkinter library for GUI creation

'''
https://www.youtube.com/watch?v=28tj-IBfGH4

14:40
24:10 <-- last

'''

# === DATA SETUP ===
# Define calculator button layout (5 rows × 4 columns)
button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

# Categorize buttons by position/function
right_symbols = ["÷", "×", "-", "+", "="]  # Operator buttons (right column)
top_symbols = ["AC", "+/-", "%"]           # Function buttons (top row)

row_count = len(button_values)      # 5 rows
column_count = len(button_values[0]) # 4 columns

# === COLOR SCHEME ===
color_light_gray = "#D4D4D2"  # For top function buttons
color_black = "#1C1C1C"       # Display background
color_dark_gray = "#505050"   # Number buttons
color_white = "white"         # Text color
color_orange = "#FF9500"      # Operator buttons

# === WINDOW SETUP ===
window = tkinter.Tk()  # Create main window object
window.title("Calculator")  # Set window title in title bar
window.resizable(False, False)  # Disable window resizing (width, height)

# === DISPLAY SCREEN ===
# Create container frame for all widgets
frame = tkinter.Frame(window)  # Frame holds label + buttons

# Create display label (calculator screen)
label = tkinter.Label(
    frame,                      # Parent container
    text="0",                   # Initial display text
    font=("Arial", 45),         # Font (family, size)
    background=color_black,     # Background color
    foreground=color_white,     # Text color
    anchor="e",                 # Text alignment: "e" = east (right-aligned)
    width=column_count          # Width in characters
)

# Position label in grid
label.grid(
    row=0,                      # First row (top)
    column=0,                   # Start at first column
    columnspan=column_count,    # Span across all 4 columns
    sticky="we"                 # Stretch west-east (left-right)
)

# === BUTTON CREATION ===
# Loop through all button positions
for row in range(row_count):              # 0 to 4 (5 rows)
    for column in range(column_count):    # 0 to 3 (4 columns)
        value = button_values[row][column]  # Get button text (e.g., "7", "+")
        
        # Create button widget
        button = tkinter.Button(
            frame,                          # Parent container
            text=value,                     # Button label
            font=("Arial", 30),             # Font size
            width=column_count-1,           # Button width (3 characters)
            height=1,                       # Button height (1 line)
            command=lambda value=value: button_clicked(value)  # Click handler
            # Lambda captures current 'value' and passes it to button_clicked()
        )
        
        # Apply color scheme based on button type
        if value in top_symbols:           # AC, +/-, %
            button.config(foreground=color_black, background=color_light_gray)
        elif value in right_symbols:       # ÷, ×, -, +, =
            button.config(foreground=color_white, background=color_orange)
        else:                              # Numbers 0-9 and decimal
            button.config(foreground=color_white, background=color_dark_gray)
        
        # Position button in grid (row+1 because row 0 is for label)
        button.grid(row=row+1, column=column)

# Pack the frame into the window (makes it visible)
frame.pack()

# === CALCULATOR STATE VARIABLES ===
# Format: A [operator] B = Result
A = "0"          # First operand (stored as string)
operator = None  # Current operator: +, -, ×, ÷ (or None)
B = None         # Second operand (stored as string)

# === HELPER FUNCTIONS ===

def clear_all():
    """Reset calculator state to initial values"""
    global A, B, operator
    A = "0"          # Reset first operand
    operator = None  # Clear operator
    B = None         # Clear second operand

def remove_zero_decimal(num):
    """
    Remove unnecessary decimal point from whole numbers
    Example: 5.0 → 5, but 5.5 stays 5.5
    Logic: If num % 1 == 0, it means no decimal part (e.g., 5.0 % 1 = 0)
    """
    if num % 1 == 0:      # Check if decimal part is zero
        num = int(num)    # Convert to integer (removes .0)
    return str(num)       # Return as string for display


# === BUTTON CLICK HANDLER ===
def button_clicked(value):
    """
    Handle all button clicks
    Parameter: value (str) - The text of the button that was clicked
    Flow:
      1. Check if value is an operator (÷, ×, -, +, =)
      2. Check if value is a function (AC, +/-, %)
      3. Otherwise, it's a digit (0-9) or decimal (.)
    """
    global right_symbols, top_symbols, label, A, B, operator

    # === CASE 1: OPERATOR BUTTONS (÷, ×, -, +, =) ===
    if value in right_symbols:
        
        # --- EQUALS BUTTON: Calculate result ---
        if value == "=":
            # Only calculate if we have both operands and an operator
            if A is not None and operator is not None:
                B = label["text"]    # Get second number from display
                numA = float(A)      # Convert strings to floats for math
                numB = float(B)

                # Perform calculation based on operator
                if operator == "+":
                    label['text'] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label['text'] = remove_zero_decimal(numA - numB)
                elif operator == "×":
                    label['text'] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    label['text'] = remove_zero_decimal(numA / numB)
                
                clear_all()  # Reset calculator state after calculation

        # --- OPERATOR BUTTONS: Store first number and operator ---
        elif value in "+-×÷":
            if operator is None:       # First operator pressed
                A = label["text"]      # Save current display as first operand
                label["text"] = "0"    # Reset display for second number
                B = "0"                # Initialize second operand
            
            operator = value           # Store which operator was pressed


    # === CASE 2: FUNCTION BUTTONS (AC, +/-, %) ===
    elif value in top_symbols:
        
        # --- AC (All Clear): Reset everything ---
        if value == 'AC':
            clear_all()             # Reset A, B, operator
            label["text"] = "0"     # Reset display to "0"
        
        # --- +/- (Negate): Flip sign of current number ---
        elif value == "+/-":
            result = float(label["text"]) * -1  # Multiply by -1 to flip sign
            label["text"] = remove_zero_decimal(result)
        
        # --- % (Percent): Divide by 100 ---
        elif value == "%":
            result = float(label["text"]) / 100  # Convert to percentage
            label["text"] = remove_zero_decimal(result)
    
    
    # === CASE 3: DIGIT BUTTONS (0-9) or DECIMAL (.) ===
    else:
        
        # --- DECIMAL POINT ---
        if value == ".":
            # Only add decimal if one doesn't already exist
            if value not in label["text"]:
                label["text"] += value   # Append decimal point
        
        # --- DIGIT BUTTONS (0-9) ---
        elif value in "0123456789":
            # Special case: If display shows "0", replace it
            if label["text"] == "0":
                label["text"] = value    # Replace "0" with digit (avoid "05")
            else:
                label['text'] += value   # Append digit to existing number

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
