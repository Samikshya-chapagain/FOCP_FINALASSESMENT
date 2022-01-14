#imoorted the csv module
import csv

#created the class league
class league:
    #created two different list to store list of country name and details extracted from csv files
    forcountry = []
    allcontents = []
    #intializing every counters to 0
    p=w=l=d=f=a=gd=pts=0
    #init method or constructor
    def __init__(self):
        #opening the csv file which contains the names of country 
        with open("Teams.csv","r") as file:
            for line in file:
                #removing \n from the each string and storing those string in forcountry named list
                league.forcountry.append(line.rstrip())
            print(league.forcountry)

        #opening the csv file which contains the data 
        with open("Results.csv","r") as second:
            #reading the file as a list
            reader = csv.reader(second)  
            for r in reader:
                #storing the each data to a list
                league.allcontents.append(r)
            print(league.allcontents)
    #static method decorater
    @staticmethod
    #created a function named mycalc
    def mycalc():
        calc = []
        #checking whether in the list of all details there is country name or not
        for c in league.forcountry:
            for result in league.allcontents:
                if c in result:
                    #if yes incrementing the match played variable
                    league.p += 1
                    
                    #comparing the second index and fourth as these both contains value which will be needed 
                    if (int(result[1]) > int(result[3])):
                        league.w += 1
                        league.f += int(result[1])
                        league.a += int(result[3])
                        league.pts += (league.w *3) + (league.d*1)

                    #comparing the indexes and incrementing the variable simultaneously
                    elif (int(result[3]) > int(result[1])):
                        league.l += 1
                        league.f += int(result[1])
                        league.a += int(result[3])

                    else:
                        league.d += 1
                        league.f += int(result[1])
                        league.a += int(result[3])
                        league.pts += 1
            #asining and calculating the difference 
            league.gd = league.f - league.a

            #adding country name matched played and different other variable in a list named calc using append method
            calc.append([c,league.p,league.w,league.d,league.f,league.a,league.gd,league.pts])
            return calc
 
#creating an instance of a class
name = league()
#printing the mycalc function through instance
print(name.mycalc())




