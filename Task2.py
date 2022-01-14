from statistics import mean                                         #imported mean from statistics module

print("Swallow Speed Analysis: Version 1.0\n")

my_list = []                                                           #created an empty list to store data
while True:                                                            #used while loop and it runs until it is false
    ask = input("Enter next reading:")                                 #asking for an input
    ask_a = ask.lower()                                                #changing the asked input in lowercase so that lower as well as uppercase case can be calculated
    if ask_a:                                                          #using if condition if ask_a has got something entered
        print("Reading Saved.")
        my_list.append(ask_a)                                          #appending entered input in empty list named as my_list
    else:                                                              #if nothing was entered then this part runs
        if not my_list:                                                #checks if the list is empty or not
            print("No readings entered.Nothing to do.")
            exit()                                                     #exits from entire program
        break                                                          #if user just presses enter but list has just some inputs then it just breaks out of the loop only
    
print("\nResults Summary\n")                                   
finding = len(my_list)                                                 #counting the length of my_list using len function
if finding == 1:                                                       #checking if length of list is only one
    print(finding,"Reading Analysed.\n")
elif finding > 1:                                                      #checking length of list is more than one
    print(finding,"Readings Analysed.\n")

new_list = []                                                          #creating an empty list to store value of U removed items
new_list1 = []                                                         #creating an empty list too store value of E removed items
my_final = []                                                          #creating an empty to store both of these typecasted list to float version

for i in my_list:                                                      #using for loop in inputed all values list
    if "u" in i:                                                       #checking of my_list has got any items that has u in it
        a = i.lstrip("u")                                              #removing u from certain items using lstrip method
        new_list.append(a)
    elif "e" in i:                                                      #checking list has got e in it
        b = i.lstrip("e")
        new_list1.append(b)

for items in new_list:                                                 #iterating over new_list which has all u string removed values
    mph_1 = float(items)                                               #typecasting items into float from string
    my_final.append(mph_1)                                             #adding those typecasted values in my_final list

for elements in new_list1:
    mph_2 = float(elements)/1.61
    my_final.append(mph_2)

if my_final != []:                                                  #checking if my_final list is empty or not
    maximum = max(my_final)                                         #checking maximum value using max function
    minimum = min(my_final)                                         #checking minimum value using min function
    average = mean(my_final)                                        #checking avearge using mean function which is imported

    print(f"Max Speed:{maximum:.2f},MPH, {maximum*1.61:.2f},KPH")   #used precision to avoid the besides unwanted value
    print(f"Min Speed:{minimum:.2f},MPH, {minimum*1.61:.2f},KPH")
    print(f"Avg Speed:{average:.2f},MPH, {average*1.61:.2f},KPH")


    
