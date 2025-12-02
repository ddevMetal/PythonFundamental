def userInput(inputRef):
    return input(f"Enter Color{inputRef}: ").lower()

def getDifferentColor(c1, prompt_num):
    """Ensures the second color is different from the first."""
    c2 = userInput(prompt_num)
    while c1 == c2:
        print("Colors must be different! Please try again.")
        c2 = userInput(prompt_num)
    return c2

def mixColors(c1, c2):
    """Mix two primary colors and return the resulting color."""
    # Define color mixing rules
    color_mix = {
        ('red', 'blue'): 'purple',
        ('blue', 'red'): 'purple',
        ('red', 'yellow'): 'orange',
        ('yellow', 'red'): 'orange',
        ('blue', 'yellow'): 'green',
        ('yellow', 'blue'): 'green'
    }
    
    # Check if colors can be mixed
    result = color_mix.get((c1, c2))
    
    if result:
        return result
    else:
        return f"Cannot mix {c1} and {c2} (only primary colors: red, blue, yellow)"


# Get user input
color1 = userInput(1)
color2 = getDifferentColor(color1, 2)

# Mix the colors
mixed_color = mixColors(color1, color2)

# Display results
print(f"\n{'='*40}")
print(f"Color 1: {color1}")
print(f"Color 2: {color2}")
print(f"Mixed Color: {mixed_color}")
print(f"{'='*40}")
