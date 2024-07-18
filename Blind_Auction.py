import os
def clear():
       os.system('cls')
auction_list = []  
counter = 0
total = []
                           

def blind_auction(name,bid):
    auction = {}
    auction["name"] = name
    auction["bid"] = bid
    print(auction_list)
    auction_list.append(auction)

last_person = False
while not last_person:
        
    name = input("What is your name?\n\n")
    bid = input("What is your bid?\n\n")
    restarto = False
    blind_auction(name,bid)
    while not restarto:
          restart = input("Is there another person?\n\n").lower()
          if restart == "yes":
               restarto = True
               counter += 1
               clear()
          if restart == "no":
               last_person = True
               restarto = True
               for i in range(counter+1):
                    mn = auction_list[i]['bid']
                    total.append(mn)
                    
               highestbid = max(auction_list, key=lambda x:x['bid'])
               print(f"The winner is {highestbid['name']} with a bid of {highestbid['bid']}")
                              
          elif restart != "no" and restart != "yes":
               print("Invalid input.")
         
        




