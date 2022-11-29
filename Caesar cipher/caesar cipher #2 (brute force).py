# for cracking open Caesar ciphered messages
# Author:   The Spoon Bandit

def brute_force(message):
    list_11 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    list_12 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    list_3 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']
    list_4 = []

    for shift in range(26):
        empty_str = ''
        for x in message:  # iterates through the txt
                if x not in list_11 and x not in list_12:
                    empty_str += x
                    continue
                try:
                    y = list_11.index(x)  # indexes the letters, based on list_11
                except ValueError:
                    y = list_12.index(x)
                
                # y = list_12.index(x)
                y += shift  # applies shift
                while y > 25:
                    y = y - 26
                while y < 0:
                    y += 26
                j = list_3[y]
                empty_str += j

        yield f'{empty_str}                shift size: {shift}'


# with open('the secret message on khan academy crypto challenge.txt', 'r') as f:
#     mes = f.read()
# for x in brute_force(mes):
#     print(x, end="\n============================================\n")

mess = 'cvpbPGS{arkg_gvzr_V\'yy_gel_2_ebhaqf_bs_ebg13_nSkgmDJE}'
for x in brute_force(mess):
    print(x.lower(), end="\n============================================\n")
