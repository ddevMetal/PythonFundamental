from helper import br, ctitle

random_words = ["Lighthouse", "Cat", "Umbrella", "Giraffe",
                "Success", "Volcano", "Balloon", "Butterfly",
                "Mississippi", "Strawberry"]




# Functions
#-----------------------------------------------------
def most_frequent_letters(word):
    br(50)
    print(f'Checking word: {word}')

    # count letters
    dict_count = {}
    word = word.lower()

    for letter in word:
        if letter  not in dict_count:
            count = word.count(letter)
            dict_count[letter] = count 

    # print report
    for k, v in dict_count.items():
        if v > 1:  # ✅ Check 'v' not 'count'
            print(f'{k} used {v} times.')
        else: 
            print(f'{k} used {v} time.')  # ✅ Singular for count = 1
        

    # find max count letters
    max_count = max(dict_count.values())
    max_letters = []

    for k,v in dict_count.items():
        if v == max_count:
            max_letters.append(k)


    #report result
    print(f'The Most Frequent Letter {max_letters}. ' f'Used {max_count} times.')

    return max_letters,max_count



# Main
#---------------------------------------------------------
for word in random_words:
    results = most_frequent_letters(word)
    letters = results[0]
    count = results[1]
    print(f'{letters}, --> {count}')