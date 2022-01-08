# Created by Cyclops!
import time

print ("----------------------------------------------------------------------------")
print (" ")
time.sleep(1)
print("Welcome To Cyclops Bank!")
print(r"""
     _______           _______  _        _______  _______  _______   
    (  ____ \|\     /|(  ____ \( \      (  ___  )(  ____ )(  ____ \  
    | (    \/( \   / )| (    \/| (      | (   ) || (    )|| (    \/  
    | |       \ (_) / | |      | |      | |   | || (____)|| (_____   
    | |        \   /  | |      | |      | |   | ||  _____)(_____  )  
    | |         ) (   | |      | |      | |   | || (            ) |  
    | (____/\   | |   | (____/\| (____/\| (___) || )      /\____) |  
    (_______/   \_/   (_______/(_______/(_______)|/       \_______)  
                                                                """)
                                                                
UserPin = 5836
amount = 13420.69
acc = 589632
time.sleep (1)
         
print ("Please Enter Your Account number :")
acc = int(input(" "))
print ("Please Enter Your 4 digit Pin :")
Pin = int(input(" "))
            
if Pin != UserPin:
    print ("Incorrect account number or pin! you have ")

else:
    print('LOGIN SUCCESFUL')

    print('SELECT FROM FOLLOWING OPTIONS: \n 1. Balance Inquiry \n 2. Withdraw \n 3. Change PIN  \n 4. Quit \n:-')
    response = int(input(' '))
    valid_responses = ['1', '2', '3', '4']
    response = response

    if response == 1:
        print('YOU HAVE ', amount,'USD IN YOUR ACCOUNT.')
    
    elif response == 2:
        print('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW.')
        cash_out = int(input(''))
                        
        if cash_out > amount:
            print ("YOU HAVE INSUFFICIENT BALANCE")
        else:
            amount = amount - cash_out
            print('YOUR NEW BALANCE IS: ', amount, 'USD')
                            
    elif response == 3:
        print('ENTER A NEW PIN')
        new_pin = int(input(' '))
        print('CONFIRM NEW PIN')
        new_ppin = int(input(' '))

        if new_ppin != new_pin:
            print('PIN MISMATCH')
            
        else:
            UserPinn = new_pin
            print('NEW PIN SAVED')
            
    elif response == 4:
        exit()