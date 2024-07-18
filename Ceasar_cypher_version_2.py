alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def ceasar(message,key,cypher):
    # alphabetlenght = len(alphabet)
    cyphtext = ""
    if cypher == "decode":
       key *= -1
    for letter in text:
        if letter in alphabet:
           letter = alphabet.index(letter)
        #    if cypher == "encode":
           cyphlet = letter + key
              
            #   if cyphlet >= alphabetlenght:
            #      cyphlet = cyphlet - alphabetlenght
           cyphtext += alphabet[cyphlet]
            #   else:
            #        cyphtext += alphabet[cyphlet]
        #    elif cypher == "decode":
        #         cyphlet = letter - key
        #             #  if cyphlet < 0:
        #             #     cyphlet = cyphlet + alphabetlenght
        #             #     cyphtext += alphabet[cyphlet]
        #             #  else:
        #         cyphtext += alphabet[cyphlet]
        else:
            cyphtext += letter


    print(f"This your encrypted message\n\n{cyphtext}\n\n")

print('''  
 ██████╗ █████╗ ███████╗███████╗ █████╗ ██████╗      ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗    ██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗
██║     ███████║█████╗  ███████╗███████║██████╔╝    ██║     ██║██████╔╝███████║█████╗  ██████╔╝
██║     ██╔══██║██╔══╝  ╚════██║██╔══██║██╔══██╗    ██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
╚██████╗██║  ██║███████╗███████║██║  ██║██║  ██║    ╚██████╗██║██║     ██║  ██║███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                                               ''')
over = False
while not over:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # shift = int(input("Type the shift number:\n"))
    if direction == "encode" or direction == "decode":
        text = input("Type your message:\n").lower()
        while True:
            try:
                shift = int(input("Type the shift number:\n"))
                break
            except ValueError:
                print("Please input integer only...")  
                continue
        # shift = int(input("Type the shift number:\n"))
        # try: 
        #     val = int(shift)
        # except ValueError:
        #     print("Only integers are allowed!!")
        shift = shift % len(alphabet)
        


    # def ceasar(message,key):
    #     # alphabetlenght = len(alphabet)
    #     cyphtext = ""
    #     for letter in text:
    #         if letter in alphabet:
    #             letter = alphabet.index(letter)
    #             if direction == "decode":
    #                 cyphlet = letter + key
    #                     # if cyphlet >= alphabetlenght:
    #                     #     cyphlet = cyphlet - alphabetlenght
    #                     #     cyphtext += alphabet[cyphlet]
    #                     # else:
    #                 cyphtext += alphabet[cyphlet]
    #             elif direction == "encode":
    #                 cyphlet = letter - key
    #                     #  if cyphlet < 0:
    #                     #     cyphlet = cyphlet + alphabetlenght
    #                     #     cyphtext += alphabet[cyphlet]
    #                     #  else:
    #                 cyphtext += alphabet[cyphlet]
    #         else:
    #             cyphtext += letter
    

    #     print(f"This your encrypted message\n\n{cyphtext}\n\n")

# def decrypt(message,key):
#     alphabetlenght = len(alphabet)
    
#     cyphtext = ""
#     for letter in text:
#         if letter in alphabet:
#            letter = alphabet.index(letter)
#            cyphlet = letter - key
#            if cyphlet < 0:
#                cyphlet = cyphlet + alphabetlenght
#                cyphtext += alphabet[cyphlet]
#            else:
#                cyphtext += alphabet[cyphlet]
#         else:
#             cyphtext += letter

#     print(f"This your decrypted message\n\n{cyphtext}\n\n")
    

         
        ceasar(message=text,key=shift,cypher=direction)
        restart = input(f"Do you want to encode or decode another word? Type 'yes' or 'no'.\n\n")
        if restart == "yes":
            over = False
        elif restart == "no":
            over = True
        elif restart != "no" and restart != "yes":
            print("Invalid input")
        
            
    

    else:
        print("Invalid input. You can only type 'encode' or 'decode'.")
