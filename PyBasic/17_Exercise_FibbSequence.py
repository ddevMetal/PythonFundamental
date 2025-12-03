from helper import br, ctitle

number_names = [
    "",                 #10^3
    "thousand",         #10^3
    "million",          #10^6
    "billion",          #10^9
    "trillion",         #10^12
    "quadrillion",      #10^15
    "quintillion",      #10^18
    "sextillion",       #10^21 
    "septillion",       #10^24
    "octillion",        #10^27
    "nonillion",        #10^30
    "decillion",        #10^33
    "Bajillion",        #10^~
]

a = 0
b = 1

for i in range(100):
    
    num = (f'{a: ,d}')
    count_commas = num.count(',')
    large_num = number_names[(count_commas)]
    print(large_num, num)

    c = a + b
    a = b
    b = c


