# Play pack Game to Practice COllection Datatypes

dashes = '-'*100


# 0 start pack Game
#---------------------------------------------------

pack = []           # empty list
print('0. Starting Journey with Empty packk!')

print('🎒',pack)
print(dashes)

#1️⃣ Pick up StarterKit Items
#---------------------------------------------------
print('1. 📦 Picking Up StarterKit (Armour, Shield, Sword, Potion).')
pack.append('Armour')
pack.append('Shield')
pack.append('Sword')
pack.append('Potion')

print('🎒',pack)
print(dashes)
 
#2️⃣ Loot a Treasure Chest
#---------------------------------------------------
# both method 1 and 2 will get same output
#method 1 
# pack.extend(chest)
#method 2
chest  = ['Map', 'Potion', 'Compass', 'Potion']
pack += chest 

print ('2. 🎁Looitng Treasure Cheest !')
print(f'Chest : {chest}')

print('🎒',pack)
print(dashes)

#3️⃣ Visit Merchent
#--------------------------------------------------- 
print('3. 🧙‍♂️ Visiting Merchent')
print('- Selling the Shield')
print('- Upgrading Sword -> Magic GreatSword')

pack.remove('Shield')

# #example1: remove sword <--- this method will change the position/ index of the sword .
# pack.remove('Sword')
# pack.append('Magic-GreatSword')

# # example2: <--- the the index is adjusted, and sword not in index 1, this will have double sword .
# pack[1] = 'Magic-GreatSword'

# example 3:
inx = pack.index('Sword')
pack[inx] = 'Magic-GreatSword'

print('🎒',pack)
print(dashes)


#4️⃣ Check Inventory
#--------------------------------------------------- 
print('4. 🔎Checking pack: ')
print('🎒',pack)

total_count = len(pack)
unique_count = len(set(pack))
potions_count = pack.count('Potion')

print(f'There are {total_count} Itmes in Total.')
print(f'There are {unique_count} Unique Items')
print(f'Th9ere are {potions_count} Potions.')
print(dashes)

#5️⃣ Dropped the pack
#--------------------------------------------------- 
print('5. 😑Droppped the pack Upside-Down...')

# #method 1 : <--- same as method 2
# pack = pack[::-1]

#method 2
pack.reverse()

print('🎒',pack)
print(dashes)

#6️⃣ Soorting Items
#--------------------------------------------------- 
print('6. ➡ Sorting Items')

#Method 1: <-- Sort by alphabetical orders
pack.sort() 

# #Method 2:
# pack.sort(key=len)

print('🎒',pack)
print(dashes)


#7️⃣ 3 ITems Stolen During Sleep
#--------------------------------------------------- 
print('7. 💤Sleeping...')

a               = pack.pop()
b               = pack.pop(2)
c               = pack.pop()

stolen_items    = [a, b, c]

print(f'Stolen items: {stolen_items}.')
print('🎒',pack)
print(dashes)


#8️⃣ Found Magic-Ring
#--------------------------------------------------- 
print('8.   💍Found Magic Ring and Coin Pouch')
ring            ='Magic Ring'
coin_pouch      =['Gold Coin', 'Silver Coin']

pack.insert(0, ring)
pack.append(coin_pouch)

print('🎒',pack)
print(dashes)

#9️⃣ Half pack Contents Have Teleported
#--------------------------------------------------- 
print('9. 💥Half Items Magically Disappeared. Damn You Magic Ring....')

count       = len(pack)

# #method 1: type casting
# half        = int(count/2)

#method 2: use // flooring down
half        = count//2

#method 1: use slicing method
pack    = pack[:half]

print('🎒',pack)
print(dashes)

#🔟 Bandits Stole Empty pack
#--------------------------------------------------- 
print('10. 🧞‍♂️Bandits Attacked.')
print('pack Stolen...')


# #method 1: clearing up the list
# pack.clear()

#method 2:
pack = None # this is how to use none <--- means u dont even have anything unless .clear() 

print('🎒',pack)
print(dashes)