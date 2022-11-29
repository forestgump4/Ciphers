# the main point of this is to make the
# shift value of the Caesar cipher variable
# this will be helpful in the Enigma project that is coming up

import time


def poly_cipher(text, shift_seq):
    """the format correctness checking section"""
    try:
        shift_seq = int(shift_seq)
    except ValueError:
        print('the shift sequence is not a number')

    try:
        if type(text) != str:
            raise TypeError
        text = text.upper()
    except TypeError:
        print('your input is not a text, allegedly')

    shift_seq = str(shift_seq)
    shift_seq = shift_seq.strip()  # removes trailing whitespace
    shift_seq = ''.join(shift_seq.split())  # removes spaces between numbers

    # the section of indexing and tracking
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    list_3 = []  # to collect the indexing

    """indexing and iteration section section"""
    # iterates through the txt
    index_tracker = 0  # to index through the shift values
    for letter in text:
        if letter not in alphabet:
            list_3.append(letter)
            continue

        calculated_index = alphabet.index(letter)  # indexes the letters, based on uppercase alphabet list

        # shift applying section
        try:
            shift = shift_seq[index_tracker]
        except IndexError:  # so that the index repeats when the shift sequence gets to the end
            index_tracker = 0  # resets it to zero when the list index reaches an end
            shift = shift_seq[0]
        try:
            shift = int(shift)
        except TypeError:
            print('the shift value input is not a number')

        shifted_index = calculated_index + shift  # applies shift
        list_3.append(shifted_index)  # appends the shifted index to an empty list
        index_tracker += 1

    """translation area"""
    # it changes the sequence of numbers generated to letters
    final = []
    for c in list_3:  # iterates through the indices

        # to make sure that the formatting is not lost in translation
        if type(c) == str:  # it keeps the non-translatables
            fin = c  # intact and in the same format
            final.append(fin)
            continue

        try:  # for when the values cannot be changed to an integer
            int(c)  # same to the above part but it captures those that might escape
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
        fin = alphabet[c]
        final.append(fin)

    final = (''.join(final))  # it joins all the translated figures into one

    return final


def poly_decipher(text, shift_seq):
    """the format correctness checking section"""
    try:
        if type(text) != str:
            raise TypeError
        shift_seq = str(shift_seq)
        shift_seq = shift_seq.strip()  # removes trailing whitespace
        shift_seq = ''.join(shift_seq.split())  # removes spaces between numbers
        shift_seq = str(shift_seq)

    except TypeError:
        print('your input is not a text, allegedly')
    except AssertionError:
        print('the shift sequence is not a number')

    # the section of indexing and tracking
    list_11 = [
    ]
    list_112 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    list_12 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    list_3 = []  # to collect the indexing

    """indexing and iteration and shifting section section"""
    # iterates through the txt
    index_tracker = 0  # to index through the shift values
    for letter in text:
        if letter not in list_112 and letter not in list_12:
            list_3.append(letter)
            continue
        try:
            calculated_index = list_112.index(letter)  # indexes the letters, based on list_11, uppercase list
        except ValueError:
            calculated_index = list_12.index(letter)  # if it is not in list_11 it looks in the lowercase list, list_12
        list_11.append(calculated_index)
        # shift applying section
        try:
            shift = shift_seq[index_tracker]
        except IndexError:  # so that the index repeats when the shift sequence gets to the end
            index_tracker = 0  # resets it to zero when the list index reaches an end
            shift = shift_seq[0]
        try:
            shift = int(shift)
        except TypeError:
            print('the shift value input is not a number')

        shifted_index = (calculated_index - shift)  # applies shift # the minus sign is what differs it from poly_cipher
        list_3.append(shifted_index)  # appends the shifted index to an empty list
        index_tracker += 1

    """translation area"""
    # it changes the sequence of numbers generated to letters
    final = []
    for c in list_3:  # iterates through the indices

        # to make sure that the formatting is not lost in translation
        if type(c) == str:  # it keeps the non-translatables
            fin = c  # intact and in the same format
            final.append(fin)
            continue

        try:  # for when the values cannot be changed to an integer
            int(c)  # same to the above part but it captures those that might escape
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
        fin = list_112[c]
        final.append(fin)

    final = (''.join(final))  # it joins all the translated figures into one

    return final, shift_seq, shift_nums, list_3, list_11


message = input('input the message you want to hide here:  ')
shift_nums = str(input('input the sequence if shift here:  '))

print(poly_cipher(message, shift_nums))

#     time.sleep(3)
#     inn_val_2 = input("do you want to save it as a text file?(y/n)  ")
#     if inn_val_2 == 'y' or inn_val == 'Y':
#         new_name = input('input the new filename here:  ')
#         with open(f'{new_name}encrypted.txt', 'w') as s:
#             s = s.write(j)
#     else:
#         print("alright then, keep your secrets")

"""printing press section"""
time.sleep(5)
print(
    '''
    
    
    
    
    
    ========================================================================================================
                                                The Spoon Bandit
    ========================================================================================================
    '''
)
