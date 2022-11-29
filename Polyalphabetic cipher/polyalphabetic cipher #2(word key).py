

def text_to_number(text):  # for changing the keyword to a sequence pf numbers
    list_ = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

    text = text.upper()  # so that the program has to look adn index using one list
    out = ''
    for letter in text:
        try:
            y = list_.index(letter) + 1  # so that A will be one, keywords are for humans, humans start counting from 1
        except ValueError:  # to keep the non-alphabetic characters uncounted
            continue
        out += str(y)

    return out  # returns a string of indices


def poly_cipher_keyword(text, shift_seq):
    """the format correctness checking section"""
    try:
        shift_seq = int(shift_seq)
    except ValueError:
        shift_seq = text_to_number(shift_seq)

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


def poly_decipher_keyword(text, shift_seq):
    """the format correctness checking section"""
    try:
        shift_seq = int(shift_seq)
    except ValueError:
        shift_seq = text_to_number(shift_seq)

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

        shifted_index = calculated_index - shift  # applies shift
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


messsage = input('input here:  ')
keyword = input('input the keyword here:  ')

sec = poly_cipher_keyword(messsage, keyword)
print(sec)
print(poly_decipher_keyword(sec, keyword))
