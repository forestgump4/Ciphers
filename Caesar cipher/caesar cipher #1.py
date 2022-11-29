# the following code ciphers a text using the Caesar cipher
# Caesar cipher is a method of hiding messages by shifting the alphabet
# it will work for the English alphabet (A-Z) but not for numbers and
# other characters
# the spaces and punctuations will be preserved
# drop them on the comment section if you find any bugs

# the out put is in all caps, regardless of the input format

import time


def shift_generator(text, shift):  #

    # the list of the alphabet
    list_11 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    list_12 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    list_3 = []  # to collect the indexing

    # finding the position of letters in the alphabet for
    # each of the input text
    # it also shifts the index and stores it for future use

    for x in text:  # iterates through the txt

        if x not in list_11 and x not in list_12:
            y = x
            list_3.append(y)
            continue
        try:
            y = list_11.index(x)  # indexes the letters, based on list_11
        except ValueError:
            y = list_12.index(x)

        # y = list_12.index(x)
        y += shift  # applies shift
        list_3.append(y)  # appends the shifted index to an empty list

    return list_3  # returns the list of shifted indices


# noinspection PyUnreachableCode
def shift_evaluation(generator):
    list_21 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']

    final = []
    for c in generator:

        if type(c) == str:
            fin = c
            final.append(fin)
            continue

        try:
            int(c)
        except ValueError:
            fin = c
            final.append(fin)
            continue

        # to keep the range of indexes in range of 26
        # and avoid IndexOutOfRange errors
        while c > 25:
            c = c - 26
        while c < 0:
            c += 26
        fin = list_21[c]
        final.append(fin)
    final = (''.join(final))

    return final


def caesar(text, shift=5):
    if text == '':
        return 'no input detected'

    if type(shift) != int:
        shift = 5
        print('the input is not an integer, the cipher will be calculated using shift size as 5')
        time.sleep(2)

    l = shift_evaluation(shift_generator(text, shift))
    return l


def de_caesar(text, original_shift_val):
    l = shift_evaluation(shift_generator(text, -original_shift_val))
    return l


# inn_txt = input("input the valuable text you want to cipher:  ")
# time.sleep(0.52)
# inn_shift = int(input("enter the shift size(integer value):  "))
# x = caesar(inn_txt, inn_shift)
#
# print(x)
#


''''if you want to cipher whole of a text file, uncomment the ones below'''
with open('aosp_license.txt', 'r') as f:
    f.fileno()
    l = f.read()
    j = caesar(l, -3)
    print(j)
    print(caesar(j, -3))
    time.sleep(3)
    inn_val = input("do you want to decipher it?(y/n)  ")

    if inn_val == 'y' or inn_val == 'Y':
        new_name = input('input the new filename here:  ')
        inn_org = int(input("input original shift size:  "))
        print(de_caesar(l, inn_org))
        time.sleep(3)
        inn_val_2 = input("do you want to save it as a text file?(y/n)  ")

        if inn_val_2 == 'y' or inn_val == 'Y':
            with open(f'{new_name}encrypted.txt', 'w') as s:
                s = s.write(l)
        else:
            print("alright then, keep your secrets")
    else:
        print("alright then, keep your secrets")
# for when you want to save it as a text file


