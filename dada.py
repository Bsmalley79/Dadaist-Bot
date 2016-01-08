import random

from letter_frequency import *


# The following function was stolen from Stack Overflow Q: 3679694
def weighted_choice(choices):
    # choices: any iterateable with 2 items each. choice and weight
    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w > r:
            return c
        upto += w
    assert False, "Shouldn't get here"


def how_long():  # Returns word length from 1 to 13 letters
    chance = random.random()
    upto = 0
    letters = 0
    while chance > upto and letters < 13:
        letters += 1
        upto += (11.74 * letters**3 * 0.4**letters) / 100
    # letters is limited to 13 because upto = 1 at letters = inf
    return letters

    
def long_word(numb_letters):
    word = ""

    word += weighted_choice(first_letter)
    if word in vowel_set:
        vcount = 1
        ccount = 0
    else:
        vcount = 0
        ccount = 1

    word += weighted_choice(general_letter)
    if word[-1] in vowel_set:
        vcount += 1
        ccount = 0
    else:
        vcount = 0
        ccount += 1

# Can't think of any word that starts with a triple consonant
    if ccount == 2:
        word += weighted_choice(vowel_letter)
        vcount = 1
        ccount = 0
    else:
        word += weighted_choice(general_letter)
        if word[-1] in vowel_set:
            vcount += 1
            ccount = 0
        else:
            vcount = 0
            ccount += 1
 
    if numb_letters == 3:
        return word
# Research indicates maximum of 3 vowels in a row, and max 4 consonants.
    else:  # Does this else need to be here? -BSmalley79
        for k in range(4, numb_letters + 1):
            if vcount == 3:
                word += weighted_choice(consonant_letter)
                vcount = 0
                ccount = 1
            elif ccount == 4:
                word += weighted_choice(vowel_letter)
                vcount = 1
                ccount = 0
            else:
                tempchar = weighted_choice(general_letter)
# Re-roll in the case of triple letters.
                while word[-1] == word[-2] == tempchar:
                    tempchar = weighted_choice(general_letter)
                word += tempchar
                
                if word[-1] in vowel_set:
                    vcount += 1
                    ccount = 0
                else:
                    vcount = 0
                    ccount += 1
        return word


def dada(chars_in_tweet = 0):
    word_lengths = []  
    tweet = ""  

    while True: # Character counter so it stays a tweet and not a book
        length = how_long()
        word_lengths.append(length)
        chars_in_tweet += (length + 1)  # 1 for the space
        if chars_in_tweet >= 140: 
            word_lengths.pop()
            break

    for i in range(len(word_lengths)):
        if i == len(word_lengths) - 1 and word_lengths[i] > 1:
            tweet += '#'

        if word_lengths[i] == 1:
            if random.random() <= .6486:
                # Research indicates 64.68% of one letter words are a
                a_or_i = 'a'
            else:  # The rest are I
                a_or_i = 'I'
            tweet += (a_or_i + ' ')
        elif word_lengths[i] == 2:
            tweet += (weighted_choice(two_letter) + ' ')
        else:
            tweet += (long_word(word_lengths[i]) + ' ')
    return tweet
