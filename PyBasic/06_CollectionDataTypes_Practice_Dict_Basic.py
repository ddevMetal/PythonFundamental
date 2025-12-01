
# DICTIONARIES

phonebook = {   'Chee Bai' : '+43 4111 5111',
                'Lan Jiao' : '+43 4222 6222',
                'Lam Pa'   : '+43 4333 7333'    }       # Name : 'Number'

# Add More Items
phonebook['Ni Ma Ma']               = '+775 555 5555'
phonebook['Chao Ji Bai']            = '+775 444 4444'
phonebook['Na Bei']                 = '+775 333 3333'


print(phonebook)


number = phonebook['Na Bei']
print(f'📞 Calling Na Bei...  ({number})')

number = phonebook['Lan Jiao']
print(f'📞 Calling Lan Jiao...  ({number})')

number = phonebook['Lam Pa']
print(f'📞 Calling Lam Pa...  ({number})')


