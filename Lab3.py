# fragmenty dotyczące rozwiązania poszczególnych zadań proszę oddzielić odpowiednimi komentarzami
#zad 2
'''from array import *
table = array('b')
print("Podaj 5 liczb całkowitych: ")
for x in range(5):
    n = input("")
    table.append(int(n))
print("======================")
for x in range(5):
    print(table.pop())  '''

#zad3
'''import random
from array import *
import numpy as np
def write_to_file(table):
    file = open("result.txt", "a")
    file.write(str(table)+"\n")
    file.close()

table = np.array(random.sample(range(-5, 5), 6))
write_to_file(table)
'''
#zad4
'''import numpy as np
def exponentiation_arrayrow(tab):
    return np.power(tab,2)


A = np.array([[2,3,4,5,6]])
for x in range(4):  
    A = np.vstack([A, exponentiation_arrayrow(A[x])])
print(A)'''
#zad5
'''import string
def create_hist(file):
    with open(file,'r') as f:
        text = f.read().lower()
        result = dict()
        for i in text:
            if i in result.keys():
                result[i] += 1
            elif i.isalpha():
                result[i] = 1
    return result

print(create_hist('tekstzad5.txt'))'''
#zad6
import numpy as np
def deck():
    rank = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A')
    colour = ('c','d','h','s')
    deck = list()
    for x in colour:
        for y in rank:
            deck.append("("+x+","+y+")")
    return deck

def shuffle_deck(deck):
    return np.random.permutation(deck)

def deal(deck, n):
    result = list()
    for x in range(n):
        result.append(deck[:5])
    return result

print(deal(shuffle_deck(deck()),2))

    