def sonant_vowel(letter):
    if letter == 'y':
        print('sonant and vowel')
    elif letter in ('a', 'e', 'i', 'o', 'u'):
        print('vowel')
    else:
        print('sonant')


l = str(input("Enter the letter "))
print(sonant_vowel(l))
