from helper import br, ctitle
# Let's Mix up come color


# User Input
color1 = input('Enter First Color (Red, Blue, Yellow): ').lower()
color2 = input('Enter Second Color (Red, Blue, Yellow): ').lower()
color = [color1, color2]

print ('-'*50)
print(f"🥼 Let's Mix 🧪{color1} + 🧪{color2}\n")


# Calculate New Color
if color1 == color2:
    emoji =None
    if color1 == 'red':
        emoji = '❤️'
    elif color1 == 'blue':
        emoji = '💙'
    elif color1 == 'yellow':
        emoji = '💛'

    print(f'🎨 You are mixing the same color!')
    print(f" 🧪{color1} and 🧪{color2} = {color1} {emoji}")

elif 'red' in color and 'blue' in color:
    print(f" 🧪{color1} and 🧪{color2} = purple 💜")

elif 'red' in color and 'yellow' in color:
    print(f" 🧪{color1} and 🧪{color2} = orange 🧡")

elif 'blue' in color and 'yellow' in color:
    print(f" 🧪{color1} and 🧪{color2} = green 💚")

else:
    print(f'❌ Invalid Color Combination. \nPlease use Red, Blue or Yellow\n\n')

print()
br(50)