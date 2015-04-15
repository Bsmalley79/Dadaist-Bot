import random

first_letter = (('a', 0.11602), ('b', 0.04702), ('c', 0.03511),
 ('d', 0.0267), ('e', 0.02), ('f', 0.03779), ('g', 0.0195),
 ('h', 0.07232), ('i', 0.06286),  ('j', 0.00631), ('k', 0.0069),
 ('l', 0.02705), ('m', 0.04374), ('n', 0.02365), ('o', 0.06264),
 ('p', 0.02545), ('q', 0.00173), ('r', 0.01653), ('s', 0.07755),
 ('t', 0.16671), ('u', 0.01487), ('v', 0.00619), ('w', 0.06661),
 ('x', 5e-05),  ('y', 0.0162), ('z', 0.0005))
 
two_letter = (('ad', 0.01463), ('ah', 0.02396), ('ai', 0.0005263),
 ('al', 0.01384), ('am', 0.008277), ('an', 0.02321), 
 ('as', 0.02176), ('at', 0.03115), ('aw', 0.008119), ('ax', 0.0005161),
 ('ba', 0.01138), ('be', 0.01771), ('bi', 0.009712),
 ('bo', 0.01046), ('by', 0.002752), ('do', 0.005943),
 ('ed', 0.002522), ('ef', 0.001321), ('eh', 0.003614), 
 ('er', 0.003551), ('ex', 8.896e-05),
 ('go', 0.004341), ('ha', 0.01751), ('he', 0.02723), ('hi', 0.01493),
 ('ho', 0.01609), ('id', 0.007927), ('if', 0.004153),
 ('im', 0.004484), ('in', 0.01258), ('is', 0.01179), ('it', 0.01688),
 ('jo', 0.001404), ('la', 0.006551),
 ('lo', 0.006021), ('ma', 0.01059), ('me', 0.01647),
 ('mi', 0.009035), ('mo', 0.009736), 
 ('my', 0.00256), ('na', 0.005727), ('no', 0.005264),
 ('od', 0.007899), ('of', 0.004138),
 ('oh', 0.01131), ('oi', 0.01293), ('om', 0.004469), ('on', 0.01253),
 ('op', 0.003583), ('or', 0.01112), ('os', 0.01175), ('ow', 0.004383),
 ('ox', 0.0002786), ('oy', 0.003666), ('pa', 0.006163), 
 ('pi', 0.005257), ('re', 0.006226), ('sh', 0.01401), ('so', 0.01726), 
 ('to', 0.03711), ('uh', 0.002687), ('um', 0.001061), ('un', 0.002976),
 ('up', 0.0008505), ('us', 0.002789), ('we', 0.02509),
 ('ya', 0.003923), ('ye', 0.006101), ('yo', 0.003606))
 
general_letter = (('a', 0.08167), ('b', 0.01492), ('c', 0.02782),
 ('d', 0.04253), ('e', 0.12702), ('f', 0.02228), ('g', 0.02015), 
 ('h', 0.06094), ('i', 0.06966), ('j', 0.00153), ('k', 0.00772),
 ('l', 0.04025), ('m', 0.02406), ('n', 0.06749), ('o', 0.07507),
 ('p', 0.01929), ('q', 0.00095), ('r', 0.05987), ('s', 0.06327),
 ('t', 0.09056), ('u', 0.02758), ('v', 0.00978), ('w', 0.0236),
 ('x', 0.0015), ('y', 0.01974), ('z', 0.00074))

vowel_set = ('a', 'e', 'i', 'o', 'u', 'y')

vowel_letter = (('a', 0.2038), ('e', 0.3169), ('i', 0.1738), ('o', 0.1873),
                ('u', 0.06882), ('y', 0.04926))

consonant_letter = (('b', 0.02489), ('c', 0.04642), ('d', 0.07097),
 ('f', 0.03718), ('g', 0.03362), ('h', 0.1017), ('j', 0.002553), 
 ('k', 0.01288), ('l', 0.06717), ('m', 0.04015), ('n', 0.1126),
 ('p', 0.03219), ('q', 0.001585), ('r', 0.09991), ('s', 0.1056),
 ('t', 0.1511), ('v', 0.01632), ('w', 0.03938), ('x', 0.002503),
 ('z', 0.001235))

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

        
"""
Function no longer needed.  Probability tables hard coded as tuples.
def fill_table(source): # Reads probability tables and sets type
    target = []
    with open(source, 'rtm') as f:
        reader = csv.reader(f)
        for row in reader:
            target.append(row)
            target[-1][1] = float(target[-1][1])
    return target
"""


def dada():
    word_lengths = []  
    tweet = ""  
    chars_in_tweet = 0  # Character counter so it stays a tweet and not a book

    while chars_in_tweet < 140:
        length = how_long()
        word_lengths.append(length)
        chars_in_tweet += (length + 1)  # 1 for the space
        # Can't call how_long() twice because it uses random.random()

    if chars_in_tweet > 140: # To do, more elegant solution
        word_lengths.pop()

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
