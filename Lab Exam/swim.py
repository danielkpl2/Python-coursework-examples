from string import *

def menu():
    option=""
    while option!="q":
        option=raw_input("Choose from the following options:\n\
l: load results from a file\n\
s: save results to a file\n\
p: print results\n\
c: check and add a new personal best\n\n\
q: quit\n\
Enter your choice: ")
        
        if option=="l":
            data=load()
        elif option=="s":
            save(data)
        elif option=="p":
            results(data)
        elif option=="c":
            check(data)
        
def load():
    f_name=raw_input("Enter the name of the file to load: ")
    f=open(f_name,"r")

    data_list=split(f.read(),"\n")
    f.close()
    error=False

    while error!=True:
        try:
            data_list.remove("")
        except(ValueError):
            error=True
    #print data_list
    
    for i in range(len(data_list)):
        data_list[i]=split(data_list[i],":")
    

    temp_list=map(lambda x:[x[0],x[1],x[2],x[4]],data_list)
    #print temp_list
    for i in range(len(temp_list)):
        #print temp_list.count(temp_list[i])
        #if temp_list.count(temp_list[i])>1:
        
        while temp_list.count(temp_list[i])>1:
            print "Multiple record detected. Can't have the same event",temp_list[i][0],", gender",temp_list[i][1],", age",temp_list[i][2],"and name",temp_list[i][3],". Only a combination of those 3 is possible. Enter a different name: ",
            temp_list[i][3]=raw_input()
            data_list[i][4]=temp_list[i][3]
    #print temp_list
    
    #print data_list

    #dictionary syntax:
    #{EVENT:{GENDER:{AGE:{NAME:TIME}}}}
    
    data={}
    
    for i in range(len(data_list)):
        #print data_list[i]
        data[data_list[i][0]]={}    #EVENT

    for i in range(len(data_list)):
        data[data_list[i][0]][data_list[i][1]]={}   #GENDER

    for i in range(len(data_list)):
        data[data_list[i][0]][data_list[i][1]][int(data_list[i][2])]={}  #AGE

    for i in range(len(data_list)):
        data[data_list[i][0]][data_list[i][1]][int(data_list[i][2])][data_list[i][4]]=float(data_list[i][3])  #NAME:TIME
    #print data
    
    return data

def save(data):
    f_name=raw_input("Enter the name of the file to save to: ")
    f=open(f_name,"w")

    for event in data:
        for gender in data[event]:
            for age in data[event][gender]:
                for name in data[event][gender][age]:
                    f.write(event+":"+gender+":"+str(age)+":"+str(data[event][gender][age][name])+":"+name+"\n")
    f.close()
    #f.write()

def results(data):
    #print data
    for event in data:
        
        for gender in data[event]:
            print
            print "Time   Event   Gender   Age   Name"
            print
            #print data[event][gender]
            ages_sorted=sorted(data[event][gender])
            
            for age in ages_sorted:
                #print data[event][gender][age]
                #print age
                
                names_sorted=sorted(data[event][gender][age],key=lambda x:data[event][gender][age][x])
                #print names_sorted
                
                for name in names_sorted:
                    
                    #print gender,name,data[event][gender][age][name]
                    
                    print data[event][gender][age][name],"  ",event,"   ",gender,"      ",age,"   ",name
        print
def check(data):
    #{EVENT:{GENDER:{AGE:{NAME:TIME}}}}
    option=""
    while option!="q":
        
        option=raw_input("\n    Choose from the following options:\n\
    c: Check personal best\n\
    a: Add personal best\n\n\
    q: Back to main menu\n\
    Enter your choice: ")
        
        if option=="c":
            name=raw_input("Enter name: ")

            ega=event_gender_age(data,name)
            
            print_names(data,ega,name,False)
            
        elif option=="a":
            name=raw_input("Enter name: ")
            
            ega=event_gender_age(data,name)
            
            n=0
            
            if len(ega)>1:
                print_names(data,ega,name,True)
                n=input("Enter the number of the record you want to amend: ")
                n=n-1
                
            print "Current best time: ", data[ega[n][0]][ega[n][1]][ega[n][2]][name]
            new_best=float(raw_input("Enter new best time: "))



            for names in data[ega[n][0]][ega[n][1]][ega[n][2]]:
##                print "current best time > new best", data[ega[n][0]][ega[n][1]][ega[n][2]][name]>new_best
##                print "new best time == others best time", new_best==data[ega[n][0]][ega[n][1]][ega[n][2]][names]
##                print "name != names", name!=name
##                print
##                print "new best time < others best time", new_best <data[ega[n][0]][ega[n][1]][ega[n][2]][names]
##                print data[ega[n][0]][ega[n][1]][ega[n][2]][name]>new_best
##                print "name != names"name!=name
                
                if data[ega[n][0]][ega[n][1]][ega[n][2]][name]>new_best and new_best==data[ega[n][0]][ega[n][1]][ega[n][2]][names] and name!=names:
                    print "Congratulations! You are now head in head with", names

                if new_best <data[ega[n][0]][ega[n][1]][ega[n][2]][names] and data[ega[n][0]][ega[n][1]][ega[n][2]][name]>new_best and name!=names and data[ega[n][0]][ega[n][1]][ega[n][2]][name]>data[ega[n][0]][ega[n][1]][ega[n][2]][names]:
                    print "Congratulations! You have beaten", names

            if new_best<data[ega[n][0]][ega[n][1]][ega[n][2]][name]:
                print "Congratulations! You achieved a new personal best!"
                data[ega[n][0]][ega[n][1]][ega[n][2]][name]=new_best
            else:
                print "Sorry, You didn't achieve a new personal best"
            
def print_names(data,ega,name,add):
    print
    print "Time   Event   Gender   Age   Name"
    print
            
##    for event in data:
##        for gender in data[event]:
##            for age in data[event][gender]:
##                for names in data[event][gender][age]:
##                    if names==name:
    for i in range(len(ega)):
        print data[ega[i][0]][ega[i][1]][ega[i][2]][name],"  ",ega[i][0],"   ",ega[i][1],"      ",ega[i][2],"   ",name,
                                
                        #print data[event][gender][age][name],"  ",event,"   ",gender,"      ",age,"   ",name,

        if add==True:
            print "----"+str(i+1)
        elif add==False:
            print
                            

def event_gender_age(data,name):     #event, gender and age retrieval function for a given name
    ega=[]
    for event in data:
        for gender in data[event]:
            for age in data[event][gender]:
                for names in data[event][gender][age]:
                    if name==names:
                        ega+=[[event,gender,age]]
    #print ega
    return ega
menu()
