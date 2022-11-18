########################## SUPPORTING FUNCTIONS ###################################################
    
def greetings (n):
    if n == 1: #hi
        breaker ("=")
        print ("\nHello how may we help you today? ")
        
    elif n == 2: #bye
        breaker("=")
        print ("\nThank you and stay safe! ")
        breaker("=")
        
    elif n == 3: #error handling
        breaker("=")
        print ("\nI'm sorry your command is not recognized, please try again.\n")
        
    elif n == 4:
        return "Please enter the number from the options to continue: \n"
    
    elif n == 5:
        return "Are you sure you want to leave?"
    
    elif n == 6:
        return "Sorry, no data to show."
    
    elif n == 7:
        print ("No.\t| Name\t\t| Manufacturer\t| Type\t|",
                "Amount\t| SKU\t|")
        
def key_fetcher(key):
    for item in stock: 
        if item["SKU"] == key:
            breaker ("=")
            print ("ITEM FOUND\n")
            greetings(7)
            print(f"{1}.\t| {item['Name']}\t \t|",
                f"{item['Manufacturer']} \t|",
                f"{item['Type']} \t|",
                f"{item['Amount']} \t\t|",
                f"{item['SKU']} \t|",)
            

def program_menu_list(n):
    #Main Menu
    if n == 1: 
        programs = ["View Items", "Add Items", "Update Stock", "Remove Stock"]
        for i in range(len(programs)):
            print (f"{i+1}. {programs[i]}\t|")
        print ("0. Exit\t\t|\n")
        
    #Read Sub Menu    
    elif n == 2: 
        print ("VIEW ITEMS MENU\n")
        programs = ["Show All", "Find Item"]
        for i in range(len(programs)):
            print (f"{i+1}. {programs[i]}\t|")
        print ("0. Exit\t\t|\n")
        
    #Create Sub Menu
    elif n == 3:
        print ("ADD ITEMS MENU\n")
        programs = ["Add Data"]
        for i in range(len(programs)):
            print (f"{i+1}. {programs[i]}\t|")
        print ("0. Exit\t\t|\n")
    
    #Update Sub Menu    
    elif n == 4:
        print ("UPDATE ITEMS MENU\n")
        programs = ["Update"]
        for i in range(len(programs)):
            print (f"{i+1}. {programs[i]}\t|")
        print ("0. Exit\t\t|\n")
    
    #Remove Sub Menu    
    elif n == 5:
        print ("DELETE ITEMS MENU\n")
        programs = ["Delete"]
        for i in range(len(programs)):
            print (f"{i+1}. {programs[i]}\t|")
        print ("0. Exit\t\t|\n")
        
def key_check(key): #Primkey Check
    if any(d["SKU"] == key for d in stock):
        return 1
        
    else:
        return 0


def breaker (n):
    print (n *100)
    
def confirmation(): #Loop for confirmation + loop flag breaker
    while True:
        
        try:
            print(greetings (5))
            answer2 = input ("Y/N:\n").lower()
            if answer2 == "y":
                return 1
            
            elif answer2 == "n":
                return  0
            
        except ValueError: pass
        
def data_check(x):
    if len (x) == 0:
        return 0
    else:
        return 1
    
def column_check(col):
    for i in stock:
        if col in i:
            return 1
            
            
        elif col not in i:
            return 0   

def full_stock():
    greetings (7)
    for i in range(len(stock)):
        print(f"{i+1}.\t| {stock[i]['Name']}\t \t|",
                f"{stock[i]['Manufacturer']} \t|",
                f"{stock[i]['Type']} \t|",
                f"{stock[i]['Amount']} \t\t|",
                f"{stock[i]['SKU']} \t|",)
    print (f"\nTotal amount of items registered: {len(stock)}")
    breaker ("=")  


def data_updater(key1):
    while True:
        nukey = input ("Please enter column to update: ")
        if column_check(nukey) == 1:
            break
        
        elif column_check(nukey) == 0:
            print ("No column exists, try again.")
            continue
        
    nuval = input ("Please enter update value: ")
    item_index = next((index for (index, d) in enumerate(stock) if d["SKU"] == key1))
    return stock[item_index].update({nukey:nuval})

def data_adder(a,b,c,d,e):
    return stock.append({
        "Name" : a,
        "Manufacturer" : b,
        "Type" : c,
        "Amount" : d,
        "SKU" : e
    })
    
def data_deleter(a):
    while True:
        print ("\nARE YOU SURE YOU WISH TO DELETE THIS DATA?",
                "\nDELETED DATA WILL BE GONE FOREVER!")
        yes_no = input ("\nY/N: ").lower()
        if yes_no == "n":
            break
    
        elif yes_no =="y":
            for i in range (len(stock)):
                if stock[i]["SKU"] == a:
                     del stock[i]
                     return
        else:
            greetings(3)


################################### MAIN #######################################################

stock = [{"Name" : "M4A1",
          "Manufacturer" : "COLT ",
          "Type" : "AR",
          "Amount": 5 ,
          "SKU" : 1
          },
         
         {"Name" : "M4A1",
          "Manufacturer" : "NORINCO",
          "Type" : "AR",
          "Amount": 25 ,
          "SKU" : 2
          },
         
         {"Name" : "MP 5",
          "Manufacturer" : "H & K",
          "Type" : "SMG",
          "Amount": 30 ,
          "SKU" : 3},
        
        {"Name" : "P 90",
          "Manufacturer" : "FN HERSTAL",
          "Type" : "SMG",
          "Amount": 92 ,
          "SKU" : 4}]

def main():

    while True:
        greetings (1)
        breaker ("=")

        
        while True:
            try:
                program_menu_list(1)
                opt_num = int (input(greetings(4)))
                if opt_num == 1:
                    breaker("=")
                    
                    while True:
                        try:
                            program_menu_list(2)
                            print(greetings(4)) #Input Instruction
                            answer = int(input(""))
                            if answer == 1:
                                
                                if data_check(stock) == 0:
                                    print (greetings(6))
                                    break
                            
                                elif data_check(stock)== 1:
                                    breaker ("=")
                                    print("Items List\n")
                                    full_stock()
                                    
                                
                            elif answer == 2:
                                
                                key = int(input("Please enter SKU Key: "))
                                if key_check(key) == 0:
                                    print (greetings(6))
                                    break
                                    
                                elif key_check(key) == 1:
                                    key_fetcher(key)
                                    breaker ("=")
                                    print ("")
                                    
                            elif answer == 0:
                                
                                if confirmation() == 1:
                                    break
                                
                                else:    
                                    continue
                                    
                            else:
                                greetings (3) #error handling
                                
                        except ValueError: greetings(3)
                    break
                    
                elif opt_num == 2:
                    breaker("=")
                    while True:
                        try:
                            program_menu_list(3)
                            print (greetings(4))
                            answer = int(input(""))
                            if answer == 1:
                                key = int(input("Please input SKU: "))
                                if key_check(key) == 1:
                                    print ("\nSKU already exists")
                                    breaker("=")
                                    
                                
                                elif key_check(key) == 0:
                                    
                                    while True: #error handling
                                        try:                                   
                                            print ("Please input the following data:")
                                            an = input ("Name: ").upper()
                                            am = input ("Manufacturer: ").upper()
                                            at = input ("Type: ").upper()
                                            aa = int(input ("Amount: "))
                                            greetings (7)
                                            print (f"1.\t|{an}\t \t|",
                                                f"{am}\t|",
                                                f"{at}\t|", f"{aa}\t\t|", f"{key}\t|")
                                            
                                            breaker ("=")
                                            print("IS THE INFORMATION CORRECT?")
                                            yes_no_1 = input ("Y/N: ").lower()
                                            if yes_no_1 == "y":
                                                data_adder(an,am,at,aa,key)
                                                print ("DATA HAS BEEN ADDED")
                                                breaker("=")
                                                break
                                                
                                            else:
                                                continue
                                            
                                        except ValueError: 
                                            breaker("=")
                                            print ("Wrong value entered, please try again.")
                                            

                            elif answer == 0:
                                loop_layer_breaker = 0 # To leave and go back to previous while loop, because for some reason return breaks all loop wtf
                                if loop_layer_breaker + confirmation() == 1:
                                    print ("")
                                    break
                                
                                else:    
                                    continue
                                
                        except ValueError: greetings(3)
                    break
                    
                elif opt_num == 3:
                    breaker("=")
                    while True:
                        try:
                            program_menu_list(4) 
                            print (greetings(4))
                            answer = int(input(""))
                            if answer == 1:
                                key1 = int(input("Please enter SKU Key: "))
                                if key_check(key1) == 0:
                                    print (greetings(6))
                                    break
                                    
                                elif key_check(key1) == 1:
                                    key_fetcher(key1)
                                    breaker ("=")
                                    print ("\nWOULD YOU LIKE TO PROCEED WITH THIS DATA?")
                                    yes_no_2 = input ("Y/N: ").lower()
                                    if yes_no_2 == "y":
                                        data_updater(key1)
                                        breaker ("=")
                                        print ("DATA HAS BEEN UPDATED")
                                        breaker ("=")
                                        break

                                    else:
                                        break
                                    
                                    
                                
                            elif answer == 0:
                                loop_layer_breaker = 0 # To leave and go back to previous while loop, because for some reason return breaks all loop wtf
                                if loop_layer_breaker + confirmation() == 1:
                                    print ("")
                                    break
                                
                                else:
                                    continue
                                
                        except ValueError: greetings(3)
                    break
                    
                elif opt_num == 4:
                    breaker("=")
                    while True:  
                        try:
                            program_menu_list(5) 
                            print (greetings(4))
                            answer = int(input(""))
                            if answer == 1:
                                keydel = int (input("Please enter SKU key: "))
                                if key_check(keydel) == 1:
                                    key_fetcher(keydel)
                                    data_deleter(keydel)
                                    print("\nITEM HAS BEEN TERMINATED")
                                    breaker("=")
                                        
                                            
                                else:
                                    breaker("=")
                                    print(greetings (6))
                                    breaker("=")
                                    
                               
                                
                            elif answer == 0:
                                if confirmation() == 1:
                                    print ("")
                                    break
                                
                                else:
                                    continue
                        
                        except ValueError: greetings(3)
                    break
                    
                elif opt_num == 0:
                    greetings (2)
                    return
                
                else:
                    greetings (3)

                    
            except ValueError: greetings (3)
                                   
        print ("\nDo you need help with anything else?")
        yes_no = input ("Y/N:\n").lower()        
        
        if yes_no == "y":
            continue
        
        elif yes_no == "n":
            greetings (2)
            break
        
        else:
            print ("Please type in Y / N: ")
            
            
        
    

main()