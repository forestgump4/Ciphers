"""
this is an improved and well-organized version of the cipher projects
i.e. caesar cipher and polyalphabetic cipher, enigma is coming soon

the following content has external modules in that do a specific job
like take inputs. they are in Handcrafted Modules library, feel free
to drop by anytime and admire the works of art.
"""


class Caesar:  # basically a copy of the caesar cipher #1 with some modifications so it can be efficient and class-y

    list_du_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                        'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                        'v', 'w', 'x', 'y', 'z']
    list_du_empyt = []

    def __init__(self, text, key=5):
        self.text = text
        self.key = key

    def cipherize_generator(self):
        for x in self.text:  # iterates through the txt

            if x not in Caesar.list_du_alphabet:
                yield x
                continue
                # y = x
                # Caesar.list_du_empyt.append(y)
                # continue
            self.y = Caesar.list_du_alphabet.index(x)
            # y = list_12.index(x)
            self.y += self.key  # applies shift
            yield Caesar.list_du_alphabet[self.y]  # appends the shifted index to an empty list

        # return Caesar.list_du_empyt  # returns the list of shifted indices
    def cipherize(self):
        for a in self.cipherize_generator():
            print(a, end='')


"""or not, i will do it later, or redo it"""

print(Caesar("AAA  aaZ", key=1).cipherize(), end=None)
