one_letter_words = 0
two_letter_words = 0
three_letter_words = 0
four_letter_words = 0
five_letter_words = 0
six_letter_words = 0
seven_letter_words = 0
eight_letter_words = 0
nine_letter_words = 0
ten_letter_words = 0
eleven_letter_words = 0
twelve_letter_words = 0
thirteen_plus_letter_words = 0
all_words = 0

file = 'romeo_and_juliet.txt'
# f = open(file, 'r')
# or (so we don't have to close the text file at the end)
with open(file, 'r') as f:  # with automatically closes the .txt file at the end

    for line in f:
        for char in list("\\\",.!?;/:][-"):
            line = line.replace(char, " ")
        for char in "'":
            line = line.replace(char, "")
        print(line)
        for word in line.split():
            if len(word) > 12:
                thirteen_plus_letter_words += 1
            elif len(word) > 11:
                twelve_letter_words += 1
            elif len(word) > 10:
                eleven_letter_words += 1
            elif len(word) > 9:
                ten_letter_words += 1
            elif len(word) > 8:
                nine_letter_words += 1
            elif len(word) > 7:
                eight_letter_words += 1
            elif len(word) > 6:
                seven_letter_words += 1
            elif len(word) > 5:
                six_letter_words += 1
            elif len(word) > 4:
                five_letter_words += 1
            elif len(word) > 3:
                four_letter_words += 1
            elif len(word) > 2:
                three_letter_words += 1
            elif len(word) > 1:
                two_letter_words += 1
            elif len(word) == 1:
                one_letter_words += 1

            if len(word) > 0:
                all_words += 1

    print(f'Proportion of 1- letter words: {(one_letter_words / all_words) * 100: <.1f}% ({one_letter_words} words)')
    print(f'Proportion of 2- letter words: {(two_letter_words / all_words) * 100: <.1f}% ({two_letter_words} words)')
    print(f'Proportion of 3- letter words: {(three_letter_words / all_words) * 100: <.1f}% ({three_letter_words} words)')
    print(f'Proportion of 4- letter words: {(four_letter_words / all_words) * 100: <.1f}% ({four_letter_words} words)')
    print(f'Proportion of 5- letter words: {(five_letter_words / all_words) * 100: <.1f}% ({five_letter_words} words)')
    print(f'Proportion of 6- letter words: {(six_letter_words / all_words) * 100: <.1f}% ({six_letter_words} words)')
    print(f'Proportion of 7- letter words: {(seven_letter_words / all_words) * 100: <.1f}% ({seven_letter_words} words)')
    print(f'Proportion of 8- letter words: {(eight_letter_words / all_words) * 100: <.1f}% ({eight_letter_words} words)')
    print(f'Proportion of 9- letter words: {(nine_letter_words / all_words) * 100: <.1f}% ({nine_letter_words} words)')
    print(f'Proportion of 10- letter words: {(ten_letter_words / all_words) * 100: <.1f}% ({ten_letter_words} words)')
    print(f'Proportion of 11- letter words: {(eleven_letter_words / all_words) * 100: <.1f}% ({eleven_letter_words} words)')
    print(f'Proportion of 12- letter words: {(twelve_letter_words / all_words) * 100: <.1f}% ({twelve_letter_words} words)')
    print(f'Proportion of 13- (or more) letter words: {(thirteen_plus_letter_words / all_words) * 100: <.1f}% '
          f'({thirteen_plus_letter_words} words)')
