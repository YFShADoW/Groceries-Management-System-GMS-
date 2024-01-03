#CHOOI YAO FENG
#TP068872

'''
Login interface:
    login()
    admin()
    new_customer()
    registered_customer()

admin system:
    1.admin_menu()
    2.upload_detail()
    3.view_detail()
    4.delete_detail()
    5.find_groc_detail()
    6.find_cus_detail()
    7.view_all_order()
    8.find_cus_order()


new customer system:
    1.view_detail() #same as admin
    2.register_page()
    
registered customer system:
    1.customer_page(user_name,user_password)
    2.view_detail()     #same as admin
    3.place_groc_order(user_name,user_password)
    4.view_cus_order(user_name, user_password)
    5.view_cus_info(user_name,user_password)

'''
#admin system
def admin_menu():           #the admin's menu page after login
    while True:             #repeat (loops)
        print()             #blank line
        print("Hello Admin! Please Select the function.")           #Greeting
        print()                                                     #blank line
        print("1. Upload Grocery Detail")                           #display all the function which can choose
        print("2. View Groceries Detail")                           #by admin
        print("3. Modify Grocery Detail")
        print("4. Delete Grocery Information")
        print("5. Find Specific Groceries Detail")
        print("6. Find Specific Customer Detail")
        print("7. View Customer Orders")
        print("8. Find Specific Customer Orders")
        print("9. Exit")
        print()                                                     #blank line
        
        admin_function=input("Please enter the number: ")           #get input (number) from admin
        if (admin_function=="1"):                                   #if input 1,call save_detail() function
            save_detail()
        elif(admin_function=="2"):                                  #if input 2,call view_detail() function
            view_detail()
        elif(admin_function=="3"):                                  #if input 3,call modify_detai() function
            modify_detail()
        elif(admin_function=="4"):                                  #if input 4,delete_detail() function
            delete_detail()
        elif(admin_function=="5"):                                  #if input 5,call find_groc_detail() function
            find_groc_detail()
        elif(admin_function=="6"):                                  #if input 6,call find_cus_detail( function
            find_cus_detail()
        elif(admin_function=="7"):                                  #if input 7,call view_all_order() function
            view_all_order()
        elif(admin_function=="8"):                                  #if input 8,call find_cus_order() function
            find_cus_order() 
        elif(admin_function=="9"):                                  #if input 9, exit the admin_menu and back to the login page
            print("Thank You!")                                     #display Thank You
            break                                                   #leave the loops of the admin_menu()
        else:                                                       
            print("Invalid Entry")                                  #To prevent the error entry from the admin and let admin enter again
            print("Please Try Again")
            continue

#########################################################################################################################################

def upload_detail():        #generate a function called upload_detail()
    m_list=[]               # generate a masterlist
    try:                    #Use try and except to prevent the error input when converting the input type to integer
        num_groc=int(input("How many groceries that you want to upload: "))     #get numeriec input to know how many times the function need to operate         
        for i in range(num_groc):                                               #repeat (num_groc) times
            groc_list=[]                                                        #generate sublist
            print()                                                             #blank line
            groc_name=input("Enter name of grocery: ")
            groc_list.append((groc_name.upper()))                               #get the details of the grocery and uppercase it
            groc_price=float(input("Enter price of grocery: RM "))              #ensure admin is entering the price with the float type
            groc_list.append("RM"+str(groc_price))                              #automatically help admin to add "RM"
            groc_expdate=input("Enter the expdate(e.g.23MAR): ")
            groc_list.append(groc_expdate.upper())                              #get the details of the grocery and uppercase it
            groc_status=input("Enter the status of the groceries\n1.AVAILABLE\n2.SHORTAGE\nPlease choose the number: ")
            if groc_status=="1":                                                #Let the admin choose the status of the grocery either AVAILABLE or SHORTAGE
                groc_list.append("AVAILABLE")
            elif groc_status=="2":
                groc_list.append("SHORTAGE")       
            m_list.append(groc_list)                                            #add sublist into master list
            print()                                                             #blank line

        print("Done")                                                           #Display Done after finished all the loops
        return m_list                                                           #return the masterlist(m_list) after called this function

    except:
        print("Invalid Entry")                  #Display "Invalid Entry" when admin typing error on above details
        print("Please Try Again")               #Display "Try Again" 
        save_detail()                           #Call out the save_detail() function to redo the upload grocery detail again.

def save_detail():
    try:            #Use try and except to prevent the error when can't find the relevent file.
        file_detail=open("groc_detail.txt","a") #Open "groc_detail.txt" in append mode.
    
    except:
        print("file cannot be openned:")        #Display "file cannot be openned:"
        exit()                                  #if the file cannot be opened, exit the function
    
    mlist=upload_detail() #Start and call the upload_detail() funtion and get masterlist from the upload_detail() function's return

    for groc_list in mlist:                     #get the sublist from the masterlist(mlist) and save in groc_detail                     
        for detail in groc_list:                #get the specific details from the sublist(groc_detail) and save in detail  
            file_detail.write(detail)           #write/append detail into file
            file_detail.write("\t")             #tab
        file_detail.write("\n")                 #new line
    file_detail.close()                         #close the "groc_detail.txt" file.

#########################################################################################################################################

def view_detail():          #generate a function called upload_detail()
    try:                    #Use try and except to prevent the error when can't find the relevent file.               
        file_detail=open("groc_detail.txt","r")     #Open "groc_detail.txt" in read mode.
    
    except:
        print("file cannot be openned")              #Display "file cannot be openned:"
        exit()                                       #if the file cannot be opened, exit the function
    
    for data in file_detail:        #get the every row(data) from the file   
        data=data.strip().split()   #remove the spacing and convert the row(data) into a list
        if len(data)>=4:            #Validation, skip the empty list [] in the file to prevent index error
            detail=data[0]+" "*(30-len(data[0]))+data[1]+" "*(15-len(data[1]))+data[2]+" "*(15-len(data[2]))+data[3]    #show the data in a tidy spacing(spacing formula)
            print(detail)       #Display the data(detail)
    file_detail.close()         #close the "groc_detail.txt" file.

###########################################################################################################################################
    
def modify_detail():    #generate a function called upload_detail()

    view_detail()       #called out the view_detail() function to view the grocery detail

    while True:             #while loops
        mlist=[]            #generate masterlist(mlist)
        modify_list=[]      #generate a modify_list 
        search=input("Please Enter the detail which you want to modify: ")      #get input for searching the grocery which need modify
        search=search.upper()               #uppercase the search input

        try:                                #filter the search result (Name, Price, Expdate,status)
            search=float(search)            #Convert to float
            search="RM"+str(search)         #if run without error, add "RM" at the left side

        except:                             #if above error, means that it is not a price, so str() it to be string                             
            search=str(search)
        
        print("\nSearch Key: ",search,"\n")         #Add "Search Key:" and display the "search" input
        
        file_detail=open("groc_detail.txt","r")     #Open "groc_detail.txt" in read mode.
        count=0                                     #generate a counter

        for line in file_detail:                    #get the every row(line) from the file 
            line=line.strip().split()               #remove the spacing and convert the row(line) into a list
            mlist.append(line)                      #save the previous detail into the mlist(prepare for the replace method)
            if (search in line):
                count+=1                            #count add one if the "search" is in the line, it means the "search" successfully been found
                modify_list.append(line)            #append the search result(line) into the modify_list


        if count==0:                                #if the count no change, it means the "search" is not in the file
            print("Detail not found")               #display detail not found  
            continue                                #contiue the "while True" and ask the admin search again

        file_detail.close()                         #close file

        break                                       #if operate normally, here will break the while loop and go down for printing

#show the search result
    for data in modify_list:    #get search result from the modify_list
        if len(data)>=4:        #to prevent the empty list[] which will provide the index problem
            search_result=data[0]+" "*(30-len(data[0]))+data[1]+" "*(15-len(data[1]))+data[2]+" "*(15-len(data[2]))+data[3]     #spacing formula
            print(search_result)            #display search_result


#process filter of the modify_list


    if len(modify_list)==1:         #when there is only one search result, operate this
        line=modify_list[0]         #e.g.line[a,b]   modify_list[[a,b]], modify_list is the masterlist and the [a,b] is inside the [[a,b]],so we need to get it out
        final_choice=modify_list[0][0]      #in this condition, only have one search_result, so it automatically will be the final_choice
        print("Please continue")            #display "Please continue" ,means that the process is running

    elif len(modify_list)>1:    #if the search result more than 1, operate this
        while True:             #while loops
            count=0             #generate counter
            final_choice=input("Enter the grocery name to select the row: ")#because have more than 1 result.so let the admin enter again to select the row which need to modify
            final_choice=final_choice.upper()                               #uppercase the string
            for line in modify_list:    #e.g. line[a,b]  modify_list[[a,b],[c,d],[e,d]]    #At here the specific detail (a,b) will save on variable "line"        
                if (final_choice == line[0]):       #line[0] is the grocery name, so if the final_choice == line[0],it means successfully choose the specific grocery
                    count+=1                        #counter add 1 , if the condition True

                    print("Please continue")        #display "Please continue" ,means that the process is running
                    break                           #admin want 1 specific result, so here it the result be found, we break the forloops to stop detecting     
            if count==0:        #if the count no change, it means the "final choice" is not in the list(line)
                print("\nInvalid please Enter Again")       #Display Invalid please Enter Again
                continue        #continue the while loops to let admin enter again

            break               #if operate normally, here will break the while loop and go down for printing

#choose and modify the detail
    while True:     #while loop1
        print("\nPlease choose the detail to modify")       #Display the choice
        print("1. Grocery Name")
        print("2. Price")
        print("3. Expdate")
        print("4. Status\n")
        
        while True:     #while loop2
            data_index=input("Enter your choice: ")         #Enter the number to select the choice
            if (data_index=="1"):
                modify=input("What you want to modify: ")   #Enter the detail what the admin want to update
                modify=str(modify)                          #convert the modify to a string
                modify=modify.upper()                       #uppercase
                line[0]=modify                              #line[0] is grocery name, here will be replacing it
                break               #break the while loop2

            elif(data_index=="2"):
                modify=input("What you want to modify: ")
                modify=float(modify)                        #convert the modify to a float
                modify="RM"+str(modify)                     #convert the modify to a string and add "RM"
                line[1]=modify                              #line[1] is price, here will be replacing it
                break               #break the while loop2

            elif(data_index=="3"):
                modify=input("What you want to modify: ")
                modify=str(modify)                          #convert the modify to a string
                modify=modify.upper()     
                line[2]=modify                              #line[2] is Expdate, here will be replacing it
                break               #break the while loop2

            elif(data_index=="4"):
                while True:     #while loop3
                    choice=input("Enter the status of the groceries\n1.AVAILABLE\n2.SHORTAGE\nPlease choose the number: ")
                    if choice=="1":
                        modify="AVAILABLE"
                        line[3]=modify  #line[3] is the status, here will replace it with "AVAILABLE"
                        break           #break the while loop3
                    elif choice=="2":
                        modify="SHORTAGE"
                        line[3]=modify  #line[3] is the status, here will replace it with "SHORTAGE"
                        break           #break the while loop3
                    else:
                        print("Enter Again")    #display try again
                        continue        #continue the whileloop3
                    
                break           #break the while loop2
            else:
                print("\nInvalid Entry\nPlease Enter Again!")    #Display Invalid please Enter Again
                continue        #continue the while loops 1
        break       #break the while loop 1

    #remove the old detail and replace the new detail
    
    #line, the detail already modify
    #mlist, the previous detail save in 
    #final_choice, the grocery detail which admin choose to modify

    mlist.sort()    #rearrange the sublist in the mlist(masterlist) (int,A-Z)

    try:
        file_detail=open("groc_detail.txt","w") #open file with write mode
    
    except:
        print("File not found")
    
    for groc in mlist:
        for i in groc:                      #mlist (masterlist), groc (sublist)
            file_detail.write(i)            #write grocery detail(i) into the file
            file_detail.write("\t")         #tab
        file_detail.write("\n")             #newline
    file_detail.close()                     #close file


###########################################################################################################################################

def delete_detail():   #define a delete detail() function

    view_detail()  #call the view_detail() to show the grocery list to the admin

    while True:         #while loops
        count=0         #generate counter
        try:
            file_detail=open("groc_detail.txt","r")         #open file in read mode

        except:
            print("file cannot be openned")
            exit()

        mlist=[]            #generate a masterlist(mlist)
        print('\nPress "enter" key to get out this page\n')         #Tell the admin press "enter" can exit this page
        del_groc=input("Enter the grocery name which you want to delete: ")     #Get grocrery name which want to delete

        for line in file_detail:
            count+=1            #count add 1
            line=line.strip().split()       #convert the line into a list and remove the spacing
            if del_groc.upper() not in line:        #if the del_groc is not in the list(line),it will reappend the list into the masterlist(mlist)
                mlist.append(line)
                
        if count>len(mlist):    #After delete 1 list(line), the length of mlist must be less than the count(the length of the previous masterlist)
            print("\nDelete successfully\n")
            
        elif(count==len(mlist)):    #if both of them are equalled,means that are not change in the masterlist
            print("\nGrocery not found\nPlease Try Againn")
            break           #break the while loops
            
        mlist.sort()            #rearrange the sublist in the masterlist
        file_detail.close()     #close file
        break           #break the while loops

#rewrite detail
    file_detail=open("groc_detail.txt","w")     #open file in write mode
        
    for groc_list in mlist:                 #masterlist(mlist),groc_list(sublist),detail(element)
        for detail in groc_list:
            file_detail.write(detail)       #write detail in to the file
            file_detail.write("\t")         #tab
        file_detail.write("\n")             #newline
    file_detail.close()                     #close file

#########################################################################################################################

def find_groc_detail(): #Definite find_groc_detail() as a funciton
    while True:         #while loops
        find_result=0   #generate a counter
        file_detail=open("groc_detail.txt","r") #open file in read mode
        search_key=input("Enter what you want to search: ")#get input "search_key"
        for line in file_detail:
            line=line.strip().split()               #convert the file string into a list
            if search_key.upper() not in line:      #if the search_key not in the line,continue the for loops to find.
                continue
            find_result+=1                          #if the search_key in the file,add count+1
            detail=line[0]+" "*(30-len(line[0]))+line[1]+" "*(15-len(line[1]))+line[2]+" "*(15-len(line[2]))+line[3]        #spacing formula
            print(detail)                           #display the detail


        if find_result==0:          #If count==0,it means the search key is not in the file.
            print("Not Found")
            continue                #continue the while loops,and get input again
        file_detail.close()         #close file
        break                       #If operate normally/successfully,while break the while loops and exit this page.

#########################################################################################################################################        

def view_cus_order(user_name, user_password):
    
    user_password=user_password
    user="Username"+" "*(15-len("Username"))+":"+user_name
    print(user)
    
    try:
        file_detail=open("order_detail.txt","r")
    
    except:
        print("file cannot be openned")
        exit()
    
    totalpayment=0
    


    for data in file_detail:    
        data=data.strip().split()
        totalprice=float(data[2][2:])/int(data[3])
        if data[0]==user_name:
            detail=data[0]+" "*(30-len(data[0]))+data[1]+" "*(15-len(data[1]))+data[2]+" "*(15-len(data[2]))+data[3]+"x RM"+str(totalprice)
            print(detail)
            
            totalprice=float(data[2][2:])
            totalpayment=totalpayment+totalprice
    file_detail.close()
    
    print("\n\t\t\tTotal payment: "+"RM "+str(totalpayment))

#####################################################################################################################################
# def find_order():

def find_cus_detail():      #generate find_cus_detail() function
    while True:             #while loops
        find_result=0       #generate counter
        file_detail=open("customer_list.txt","r")#open file in read mode
        search_username=input("Enter the username to search: ")#get input
        for line in file_detail:
            line=line.strip().split()         #remove spacing and convert to list
            if search_username.upper() not in line[4]:  
                continue #continue the for loops
            find_result+=1      #add count +1
            if len(line)>=4:    #validation,prevent the empty list
                data="Name"+" "*(20-len("Name"))+":"+line[0]        #print all the information
                print(data)
                data="Gmail"+" "*(20-len("Gmail"))+":"+line[1]
                print(data)
                data="Contact Number"+" "*(20-len("Contact Number"))+":"+line[2]
                print(data)
                data="Birthday"+" "*(20-len("Birthday"))+":"+line[3]
                print(data)
                data="Username"+" "*(20-len("Username"))+":"+line[4]
                print(data)
                data="Userpassword"+" "*(20-len("Userpassword"))+":"+line[5]
                print(data)

        if find_result==0:      #if the username not in the file,will operate this
            print("Not Found")
            continue            #continue the while loops
        file_detail.close()     #close file
        break                   #break while loops

#########################################################################################################################################

def view_all_order():
    
    try:
        file_detail=open("order_detail.txt","r")
    
    except:
        print("file cannot be openned")
        exit()    

    for data in file_detail:    
        data=data.strip().split()
        totalprice=float(data[2][2:])/int(data[3])
        detail=data[0]+" "*(30-len(data[0]))+data[1]+" "*(15-len(data[1]))+data[2]+" "*(15-len(data[2]))+data[3]+"x RM"+str(totalprice)
        print(detail)
            
    file_detail.close()
    
    print("\nDone\n")



#########################################################################################################################################

def find_cus_order():

    user_name=input("Please Enter the specfic username: ")
    
    user="Username"+" "*(15-len("Username"))+":"+user_name
    print(user)
    
    try:
        file_detail=open("order_detail.txt","r")
    
    except:
        print("file cannot be openned")
        exit()
    
    totalpayment=0

    for data in file_detail:    
        data=data.strip().split()
        price=float(data[2][2:])/int(data[3])
        if data[0]==user_name:
            detail=data[0]+" "*(30-len(data[0]))+data[1]+" "*(15-len(data[1]))+data[2]+" "*(15-len(data[2]))+data[3]+"x RM"+str(price)
            print(detail)
            
            totalprice=float(data[2][2:])
            totalpayment=totalpayment+totalprice
    file_detail.close()
    
    print("\n\t\t\tTotal payment: "+"RM "+str(totalpayment))

#########################################################################################################################################

#registered customer system
def customer_page(user_name,user_password):
    while True:
        print("\nWelcome to FRESHCO")
        print("Choose what you want to do")
        print("1. View Groceries detail.")
        print("2. Place order of Groceries.")
        print("3. View own order.")
        print("4. View personal information.")
        print("5. Exit\n")
        cus_ans=input("Enter the number of choice: ")
        if cus_ans=="1":
            print()
            view_detail()
        elif cus_ans=="2":
            place_groc_order(user_name,user_password)

        elif cus_ans=="3":
            view_cus_order(user_name,user_password)

        elif cus_ans=="4":
            view_cus_info(user_name,user_password)
            continue
        elif cus_ans=="5":
            print("Thank You!")
            break
        else:
            print("Invalid Answer\nPlease Try Again\n")
            continue

#########################################################################################################################################


def place_groc_order(user_name,user_password):     #1.show price 2.connect to the groc detail 3.shows total payment


    view_detail()

    order_list=[]
    total_payment=0
    count=0
    while count==0:
        try:
            file_detail=open("groc_detail.txt","r")
        
        except:
            print("file cannot be openned:")
            exit()
            
        buy_order = input("Please enter which grocery you want to order: ")
        
        for line in file_detail:
            line=line.strip().split()
            if buy_order.upper() == line[0]:
                buy_list=[]
                buy_list.append(user_name)
                buy_list.append(line[0])
                
                while True:
                    try:
                        value= int(input("Enter the value you want to buy: "))
                        break
                    except:
                        print("Invalid Entry")
                        continue
                totalprice=float(line[1][2:])*(value)
                buy_list.append("RM"+str(totalprice))
                buy_list.append(str(value))
                order_list.append(buy_list)
                total_payment=total_payment+totalprice
        file_detail.close()

        print("\nDo you want to continue to order?")
        while count==0:
            cus_ans=input("Enter yes/no: ")
            if cus_ans.lower() == "yes":
                break

            elif cus_ans.lower() == "no":
                print("\nUsername: "+user_name)
                print("Total Payment: "+"RM"+str(total_payment))
                print()
                for data in order_list:
                    price=float(data[2][2:])/int(data[3])    
                    order_result=data[1]+" "*(30-len(data[1]))+data[2]+" "*(15-len(data[2]))+data[3]+"x RM"+str(price)
                    print(order_result)
                print()
                
                while True:
                    confirmation=input("Please Confirm Your Order list(yes/no): ")
                    if confirmation.lower()=="yes":
                        print("Order succesful")
                        count+=1
                        save_order_detail(order_list)
                        break

                    elif confirmation.lower()=="no":
                        print("Please Order Again")
                        place_groc_order(user_name,user_password)
                    
                    else:
                        print("Invalid Entry")
                        continue
                
            else:
                print("\nInvalid Entry\nPlease Try  Again\n")
                continue
        


def save_order_detail (order_list):

    try:
        file_detail=open("order_detail.txt","a")
    
    except:
        print("File connot be found")
        exit()

    for cus_order in order_list:
        for detail in cus_order:
            file_detail.write(detail)
            file_detail.write("\t")
        file_detail.write("\n")
    file_detail.close()
#sort()?

#########################################################################################################################################

def view_cus_info(user_name,user_password):

    try:
        file_detail= open('customer_list.txt','r')
    except:
        print("File cannot be found")
        exit()
    
    for line in file_detail:
        line=line.strip().split()
        if (user_name in line[4]) and (user_password in line[5]):
            if len(line)>=4:
                data="Name"+" "*(20-len("Name"))+":"+line[0]
                print(data)
                data="Gmail"+" "*(20-len("Gmail"))+":"+line[1]
                print(data)
                data="Contact Number"+" "*(20-len("Contact Number"))+":"+line[2]
                print(data)
                data="Birthday"+" "*(20-len("Birthday"))+":"+line[3]
                print(data)
                data="Username"+" "*(20-len("Username"))+":"+line[4]
                print(data)
                data="Userpassword"+" "*(20-len("Userpassword"))+":"+line[5]
                print(data)
                break

    file_detail.close()

#########################################################################################################################################

    
#new_customer_system
def register_page():

    nc_info = []

    print("Enter your information for registration")
    print()
    nc_name=input("Enter your name\n")
    nc_info.append(nc_name.upper())
    nc_email=input("Enter your email\n")
    nc_info.append(nc_email)
    nc_contact=(input("Enter your contact number\n"))
    nc_info.append(nc_contact)
    nc_birthdate=input("Enter your date of birth(e.g.MAR22)\n")
    nc_info.append(nc_birthdate.upper())
    while True:

        file_detail=open("customer_list.txt","r")

        count=0
        nc_username=input("Enter your username\n")
        for line in file_detail:
            line=line.strip().split()
            if nc_username == line[4]:
                count+=1

        if count==0:
            nc_info.append(nc_username)
            print(nc_info)
            file_detail.close()
            break
        
        elif count >0:
            print("\nUsername has been used\nPlease Enter Again\n")
            continue

    while True:
        nc_pwd=input("Enter your password\n")
        nc_repwd =  input("Rewrite the password\n")
        if nc_pwd == nc_repwd:
            nc_info.append(str(nc_pwd))
            break
        else:
            print("Password is not same\nPlease Try Again")
            continue
    
    if (""in nc_info):
        print("Invalid info\nPlease Try Again")
        register_page()

    print()
    data="Name"+" "*(20-len("Name"))+":"+nc_info[0]
    print(data)
    data="Gmail"+" "*(20-len("Gmail"))+":"+nc_info[1]
    print(data)
    data="Contact Number"+" "*(20-len("Contact Number"))+":"+nc_info[2]
    print(data)
    data="Birthday"+" "*(20-len("Birthday"))+":"+nc_info[3]
    print(data)
    data="Username"+" "*(20-len("Username"))+":"+nc_info[4]
    print(data)
    data="Userpassword"+" "*(20-len("Userpassword"))+":"+nc_info[5]
    print(data)
    
    while True:
        confirm=input("Please confirm your infomation\n1.Yes\n2.No\nEnter the number: ")
        if confirm == "1":
            print("All information has been saved")
            save_info(nc_info)
            break

        elif confirm =="2":
            print("Thanks For Participate!\n Registered Failed")
            login()
            exit()
            
        else:
            print("Error Entry")
            continue
    

def save_info(nc_info):
    try:
        file_detail=open("customer_list.txt","a")
    
    except:
        print("file cannot be openned:")
        exit()
    
    mlist=nc_info 

    for info in mlist:
        file_detail.write(info)
        file_detail.write("\t")
    file_detail.write("\n")
    file_detail.close()

#########################################################################################################################################

#login page
def login():        #generate a login() function for the login interface
    while True:     #while loops
        print()
        print("1. Admin") #Display the choice
        print("2. New Customer")
        print("3. Registered Customer")
        print("4. Exit")
        login_as=input("Please choose the number to login or exit: ") # get the choice
        if (login_as=="1"): 
            admin()                  #call admin() function
        
        elif (login_as=="2"):
            new_customer()           #call new_customer() function
        elif(login_as=="3"):
            registered_customer()    #call registered_customer()function
        elif(login_as=="4"):
            print("Thank you!\n")       #exit the login page
            break                       #break the while loops
        else:
            print("Please try again")
            continue                    #invalid entry,continue the while loops

def admin():        #generate admin() function
    admin_name=input("Please enter your username: ")
    if (admin_name=="f"):
        admin_password=input("Please enter your password: ")
        if (admin_password==admin_name+"1234"):
            admin_menu()
        else:
            print("Sorry, Please Try again")
    else:
        print("Sorry, Please Try Again")
        login()

def registered_customer():
    try:
        file_detail=open("customer_list.txt","r")

    except:
        print("Sorry, Please Try Again!")
        exit()

    result_count=0
    user_name=input("Please enter your username: ")
    for line in file_detail:
        check=line.split()#Validation
        if user_name in check[4]:
            result_count+=1
            while True: 
                user_password=input("Please enter your password: ")
                if (user_name in check[4])and(user_password in check[5]):
                    print("Login successful\n")
                    customer_page(user_name,user_password)
                    break
                    
                else:
                    print("Wrong Password\nPlease Try Again")
                    continue
    if result_count==0: 
        print("user not found")
    file_detail.close()


def new_customer():
    while True:
        print("\nPlease Select your choice")
        print()
        print("1. View Groceries Detail")
        print("2. Register as a FRESHCO customer")
        print("3. Exit")
        print()
        nc_ans=input("Please Enter the number: ")

        if (nc_ans=="1"):
            print()
            view_detail()

        elif (nc_ans=="2"):
            register_page()
            print("\nThank You for registation.\nPlease Login\n")
            break
        
        elif (nc_ans=="3"):
            print("Thank You!")
            break

        else:
            print("Invalid Entry3")
            print("Please Try Again")
            continue


login()
