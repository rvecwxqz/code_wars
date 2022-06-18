"""https://www.codewars.com/kata/55c04b4cc56a697bb0000048"""
from collections import defaultdict
'''
def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True
    '''
#

def scramble(s1, s2):
    d1 = defaultdict(int)
    for letter in s1:
        d1[letter] += 1
    for letter in s2:
        if letter in d1 and d1[letter] > 0:
            d1[letter] -= 1
        else:
            return False
    return True


print(scramble('katas', 'steak'))
