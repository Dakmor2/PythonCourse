import sys
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['?', '!', '.', ';', ' ', ':', '(', ')']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if direction != "encode" and direction != "decode":
   print("You can only type 'encode' or 'decode'.")
   sys.exit()
else:
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    




def ceasar(message,key):
    alphabetlenght = len(alphabet)
    cyphtext = ""
    for letter in text:
        if letter in symbols:
           cyphtext += letter
        elif direction == "encode":           
             cyphlet = letter + key
            #  if cyphlet >= alphabetlenght:
            #     cyphlet = int(cyphlet % alphabetlenght)
            #     cyphtext += alphabet[cyphlet]
            #  else:
             cyphtext += alphabet[cyphlet]
            # elif letter in symbols:
            #      cyphtext += letter

        elif direction == "decode":
             cyphlet = letter - key
            #  if cyphlet < 0:
            #     cyphlet = int(cyphlet % alphabetlenght)
            #     cyphtext += alphabet[cyphlet]
            #  else:
             cyphtext += alphabet[cyphlet]
              

    print(f"This your encrypted message\n\n{cyphtext}\n\n")

# def decrypt(message,key):
#     alphabetlenght = len(alphabet)
    
#     cyphtext = ""
#     for letter in text:
#         if letter in symbols:
#            cyphtext += letter
#         else:
#             letter = alphabet.index(letter)
#             cyphlet = letter - key
#             if cyphlet < 0:
#                cyphlet = cyphlet + alphabetlenght
#                cyphtext += alphabet[cyphlet]
#             else:
#                cyphtext += alphabet[cyphlet]

#     print(f"This your decrypted message\n\n{cyphtext}\n\n")
shift = shift % 26
ceasar(message=text,key=shift)


