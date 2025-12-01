# Play Backpack Game to Practice COllection Datatypes


# 0 start Backpack Game
#---------------------------------------------------

backpack = []           # empty list
print('0. Starting Journey with Empty BackPackk!')

print('🎒',backpack)
print('-'*50)

#1️⃣ Pick up StarterKit Items
#---------------------------------------------------
print('1. 📦 Picking Up StarterKit (Armour, Shield, Sword, Potion).')
backpack.append('Armour')
backpack.append('Shield')
backpack.append('Sword')
backpack.append('Potion')

print('🎒',backpack)
print('-'*50)
 
#2️⃣ Loot a Treasure Chest
#---------------------------------------------------
# both method 1 and 2 will get same output
#method 1 
# backpack.extend(chest)
#method 2
chest  = ['Map', 'Potion', 'Compass', 'Potion']
backpack += chest 

print ('2. 🎁Looitng Treasure Cheest !')
print(f'Chest : {chest}')

print('🎒',backpack)
print('-'*50)

#3️⃣ Visit Merchent
#--------------------------------------------------- 
print('3. 🧙‍♂️ Visiting Merchent')
print('- Selling the Shield')
print('- Upgrading Sword -> Magic GreatSword')

backpack.remove('Shield')

# #example1: remove sword <--- this method will change the position/ index of the sword .
# backpack.remove('Sword')
# backpack.append('Magic-GreatSword')

# # example2: <--- the the index is adjusted, and sword not in index 1, this will have double sword .
# backpack[1] = 'Magic-GreatSword'

# example 3:
inx = backpack.index('Sword')
backpack[inx] = 'Magic-GreatSword'

print('🎒',backpack)
print('-'*50)


#4️⃣ Check Inventory
#--------------------------------------------------- 
print('4. 🔎Checking Backpack: ')
print('🎒',backpack)

total_count = len(backpack)
unique_count = len(set(backpack))
potions_count = backpack.count('Potion')

print(f'There are {total_count} Itmes in Total.')
print(f'There are {unique_count} Unique Items')
print(f'Th9ere are {potions_count} Potions.')
print('-'*50)

#5️⃣ Dropped the Backpack
#--------------------------------------------------- 
print('5. 😑Droppped the Backpack Upside-Down...')

# #method 1 : <--- same as method 2
# backpack = backpack[::-1]

#method 2
backpack.reverse()

print('🎒',backpack)
print('-'*50)

#6️⃣ Soorting Items
#--------------------------------------------------- 
print('6. ➡ Sorting Items')

#Method 1: <-- Sort by alphabetical orders
backpack.sort() 

# #Method 2:
# backpack.sort(key=len)

print('🎒',backpack)
print('-'*50)


#7️⃣ 3 ITems Stolen During Sleep
#--------------------------------------------------- 
print('7. 💤Sleeping...')

a               = backpack.pop()
b               = backpack.pop(2)
c               = backpack.pop()

stolen_items    = [a, b, c]

print(f'Stolen items: {stolen_items}.')
print('🎒',backpack)
print('-'*50)


#8️⃣ Found Magic-Ring
#--------------------------------------------------- 
print('8.   💍Found Magic Ring and Coin Pouch')
ring            ='Magic Ring'
coin_pouch      =['Gold Coin', 'Silver Coin']

backpack.insert(0, ring)
backpack.append(coin_pouch)

print('🎒',backpack)
print('-'*50)

#9️⃣ Half Backpack Contents Have Teleported
#--------------------------------------------------- 
print('9. 💥Half Items Magically Disappeared. Damn You Magic Ring....')

count       = len(backpack)

# #method 1: type casting
# half        = int(count/2)

#method 2: use // flooring down
half        = count//2

#method 1: use slicing method
backpack    = backpack[:half]

print('🎒',backpack)
print('-'*50)

#🔟 Bandits Stole Empty Backpack
#--------------------------------------------------- 
print('10. 🧞‍♂️Bandits Attacked.')
print('Backpack Stolen...')


# #method 1: clearing up the list
# backpack.clear()

#method 2:
backpack = None # this is how to use none <--- means u dont even have anything unless .clear() 

print('🎒',backpack)
print('-'*50)