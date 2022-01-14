from random import choice                   #imported choice from random module

#function named checking 
def checking():
    """The interactive online chat system for e University of Poppleton."""
    #creating the different list which will be needed in further operation of program
    names = ["Arthur","fiona","Jim","Janice"]
    exiting = ["goodbye","bye","exit","see you","thank you"]
    responses = ["Hmmm.","Oh, yes, I see","Tell me more","yes","Mmmm.","That is interesting","Oh Yay!"]
    forlibrary = ["library","books","study","information"]
    forwifi = ["wifi","internet","network","net"]
    fordead = ["deadline","submission","due date","work"]
    foreca = ["eca","sports","games","playground"]
    forcanteen = ["canteen","food","coffee","lunch","eat","tea"]
    forteachers = ["teachers","tutors","instructor","professor"]
    erros_1 = [1,1,1,0,1,1,1,1,1,1]
    my_error = choice(erros_1)

    print("\nWelcome to Pop Chat\nOne of our operators will be pleased to help you today.\n")

    #asks user to enter email address
    email = input("Please enter your Poppleton email address:")
    #checking if the email provided by the user has got @ to check the validity
    if "@" in email:
        a = email.count("@")
        #if @ is more than one it gets invalid too
        if a > 1:
            print("Wrong! The @ in the email address cannot be more than 1")
            #gets exit from whole program if there is more than one @
            exit()
        #if @ is equal to 1
        else:
            #getting the position of @ using index() and storing it in position variable
            position = email.index("@")
            #slicing the name from email address from 0 position to the position where @ is and storing in variable now
            now = email[0:position]
            #slicing the domain name of emailaddress from email  and storing in again variable
            again = email[position+1:]
            
            #checking for the validity there should be atleast 2 character before @ appears
            if len(now) >= 2:
                #checking if domain name is pop.ac.uk as it should be that only 
                if again == "pop.ac.uk":
                    print(f"Hi,{now.capitalize()}! Thank you, and welcome to PopChat!")
                    print(f"My name is {choice(names)}, and it will be pleasure to help you.")
                    if my_error == 0:
                        print("\n***NETWORK ERROR***\n")
                        print(f"Thanks {now.capitalize()}, for using PopChat, See you again soon!")
                        exit()
                    #used while loop which should iterate until user wants to exit from the chat system
                    while True:
                        #asks user to ask anything
                        question = input("---> ")
                        #changing the asked input into lowercase
                        change = question.lower()
                        #created an empty dictionary
                        my_dict = {}
                        #used for loop in list forlibrary
                        for l in forlibrary:
                            #stored those list item as keys in my_dict and used choice method give response accordingly
                            my_dict[l] = choice(["the library is closed.","the library reopens tomorrow"])
                        for w in forwifi:
                            my_dict[w] = choice(["Wifi is excellent across the campus.","Wifi could be dowm sometimes."])
                        for d in fordead:
                            my_dict[d] = choice(["Your dealine has been extended by two working days.",
                                        "You can take your time as your deadline has been extended."])
                        for e in foreca:
                            my_dict[e] = choice(["Welcome to game zone.","You are free to play here."])
                        for c in forcanteen:
                            my_dict[c] = choice(["Come when you are hungry.","Canteen is beside your college building."])
                        for t in forteachers:
                            my_dict[t] = choice(["Teachers are very helpful.","Teachers are available whenever you need."])
                        
                        #getting the keys of dictionary using keys() method
                        a = my_dict.keys()
                        #iterating over keys of the dictionary
                        for i in a:
                            #checking if those items in keys were entered by user or not
                            if i in change:
                                #if yes it shows the values of particular keys using get method
                                forvalues = my_dict.get(i)
                                print(forvalues)
                                break
                        #if i is not keys then it checks if user wants more information or just want to get out of chat    
                        if i not in change:
                            #iterating over existing named list
                            for j in exiting:
                                #checks if j is inputed
                                if j in change:
                                    print(f"\nThanks, {now.capitalize()}, for using PopChat. See you again soon!\n")
                                    exit()
                            #if j is not inpute the these random reposnes will be provided to user
                            print(choice(responses))

                #if the domain was not equal to user inputed then this message will be displayed and get of program            
                else:
                    print("Domain name and name should be same.")
                    exit()
            #less than 2 charcter are not allowed as we have checked email before and dgets exits from the program
            else:
                print("Less than 2 characters are not allowed before @.")
                exit()
    #if no @ was provided than gives this message            
    else:
        print(email,"invalid at pop.ac.uk.")

#checking if the file is script or it was imported
if __name__ == "__main__":
    #if it is script then function named checking is called
    checking()