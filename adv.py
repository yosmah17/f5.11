alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' , 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text = input("Type your message: ")
shift = int(input("Type the shift number: "))
def encrypt(texth, shifth):
    newt=""
    
    for i in texth:
        if i in alphabet:
            num=alphabet.index(i)
            newt+=alphabet[num+shift]
    return newt
print(encrypt(text, shift))