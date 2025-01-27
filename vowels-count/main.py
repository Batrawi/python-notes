""" Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces. """

def get_number_of_vowels(str):
    vowels_list = {'a', 'e', 'i', 'o', 'u'} #hash insted of list
    return sum(1 for letter in str.lower() if letter in vowels_list)