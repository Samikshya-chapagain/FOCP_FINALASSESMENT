print("""Stop! Who would cross the Bridge of Death 
Must answer me these questions three, 'ere the other side he see.\n""")

#asking user for first input which results in string
name = input("What is your name?")     

#checking if the entered name is arthur or not
if name == "Arthur" or name == "arthur":            
    print("My liege! You may pass!")
#if the entered name is other than arthur
else: 
    #asking for another input from user                                              
    my_seek = input("What do you seek?") 
    #changing the input provided by the user into lowercase           
    my_seek1 = my_seek.lower()       
    #using while loop and membership operator for checking if the entered input has got grail or not               
    while "grail" in my_seek1: 
        #again asks for another input                      
        favo = input("What is your favorite colour?")
        #using if statement to check the first letter of name and favo input
        if name[0].lower() == favo[0].lower():       
            print("You may pass!")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")
        #using break statement to stop while loop if this all happens    
        break                                        
    #if there is no grail in input then this else part will run
    else:                                            
        print("Only those who seek the Grail may pass.")

    

    




    