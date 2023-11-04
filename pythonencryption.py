import time
import sys

def printype(text, delay = 0.07):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

def numshiften(Letters, key):
    chipher = ''
    for Letter in Letters:
        if Letter == ' ':
            chipher = chipher + Letter
        elif chipher.isupper():
            chipher = chipher + chr((ord(Letter) + key - 65) % 26 + 65)
        else:
            chipher = chipher + chr((ord(Letter) + key - 97) % 26 + 97)
    return chipher	
def numshiftde(Letters, key):
    chipher = ''
    for Letter in Letters:
        if Letter == ' ':
            chipher = chipher + Letter
        elif chipher.isupper():
            chipher = chipher + chr((ord(Letter) + -abs(key) - 65) % 26 + 65)
        else:
            chipher = chipher + chr((ord(Letter) + -abs(key) - 97) % 26 + 97)
    return chipher
while True:
    printype('What would you like to do?\n')
    printype('1 |  Encrypt\n')
    printype('2 |  Decrpyt\n')
    printype('q to quit\n')
    choice = input('')
    if choice == '1':
        printype('Please input the text you like to encrypt(Ceaser Cypher)\n')
        inp = input('')
        printype('What is the delimiter?(1 - 26)\n')
        inpu = int(input(''))
        encrypted = numshiften(inp, inpu)
        printype(f'The message is now encrypted:\n')
        printype(f'{encrypted}\n')
    if choice == '2':
        printype('Please input the text you like to decrypt(Ceaser Cypher)\n')
        inp = input('')
        printype('What is the delimiter?(1 - 26)\n')
        inpu = int(input(''))
        encrypted = numshiftde(inp, inpu)
        printype(f'The message is now decrypted:\n')
        printype(f'{encrypted}\n')
    printype('Would you like to go again? (Y/N) \n')
    choice2 = input('')
    if choice2 == 'N':
        break
    if choice2 == 'n':
        break
