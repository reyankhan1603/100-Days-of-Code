#Caesar Cipher

def encode(sent,shift):
    c = ''
    for letter in sent:
        i = alphabet.index(letter)
        c = c + alphabet[i+shift]
    
    return c

def decode(sent,shift):
    c = ''
    for letter in sent:
        i = alphabet.index(letter)
        c = c + alphabet[i-shift]
    
    return c

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z']
sent = input('Enter the message: ').lower()
shift=int(input('Enter the shift value: ').lower())

code = input('encode or decode?: ').lower()

if code == 'encode':
    final = encode(sent,shift)
    print(final)

if code == 'decode':
    final = decode(sent,shift)
    print(final)