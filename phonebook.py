i=1
print ('\n------------------------- PHONE BOOK -------------------------')
data ={}
while i!=0:
    print("\n\t\t1 -> Create\n\t\t2 -> View\n\t\t3 -> Edit\n\t\t4 -> Delete person\n\t\t5 -> Exit (all data will be deleted)")
    n = int(input("\nEnter your choice : "))
    if n==1:
        print ('\n------------------------- ENTER THE DETAILS -------------------------')
        name = input("\nEnter the name : ")
        email = input("Enter the email : ")
        ph = int(input("Enter the number of phone number user have : "))
        phone_number =[]
        for k in range(ph):
            phno = input("Enter the phone number "+str(k+1)+" : ")
            phone_number.append(phno)
        print('\n--- New user '+name+' added ---')
        data[name]={'Name':name,'Email':email,'Phone number':phone_number}
        print(data[name])
    elif n==2:
        print ('\n------------------------- CURRENT PHONE BOOK -------------------------')
        # print(data)
        for j,k in data.items():
            print("\n   Name : "+k['Name'])
            print("   Email : "+k['Email'])
            print("   Phone no : ",end='')
            print(k['Phone number'])
        print("\n-----------------------------------------------------------------------")
    elif n==3:
        print('\n------------------------- EDIT MODE ACTIVATED -------------------------\n')
        u=1
        while u!=0:
            edit_name = input("Enter the name that needs editing (enter \'exit\' for exiting): ")
            if edit_name=='exit':
                print ('\n------------------------- EDIT MODE DEACTIVATED -------------------------\n')
                u=0
            elif edit_name in data.keys():
                c = 1
                while c!=0:
                    print("\n\t\t1 -> Edit Name {"+edit_name+"}\n\t\t2 -> Edit Email {"+data[edit_name]['Email']+"}\n\t\t3 -> Edit existing Phone number {"+str(data[edit_name]['Phone number'])+"}\n\t\t4 -> Add a new Phone number\n\t\t5 -> Remove existing Phone number\n\t\t6 -> Exit from current name")
                    y = int(input("Enter your choice for editing : "))
                    if y==1:
                        new_name = input("Enter the new name : ")
                        data[edit_name]['Name'] = new_name
                        data[new_name]=data.pop(edit_name)
                        edit_name = new_name
                        print("\n ===== NAME UPDATED SUCCESSFULLY =====")
                    elif y==2:
                        new_email = input("Enter the new email : ")
                        data[edit_name]['Email']=new_email
                        print("\n ===== EMAIL UPDATED SUCCESSFULLY =====")
                    elif y==3:
                        existing_phno = input("Enter the existing phone number : ")
                        h = data[edit_name]['Phone number']
                        if existing_phno in h:
                            new_phno = input("Enter the updated phone number : ")
                            temp_ph = data[edit_name]['Phone number']
                            h.pop(h.index(existing_phno))
                            h.append(new_phno)
                            print("\n ===== PHONE NUMBER UPDATED SUCCESSFULLY =====")
                        else:
                            print("\n ===== PHONE NUMBER UPDATION FAILED , NOT FOUND IN LIST =====")
                            continue
                    elif y==4:
                        new_phno = input("Enter the new phone number : ")
                        h= data[edit_name]['Phone number']
                        h.append(new_phno)
                        print("\n ===== PHONE NUMBER ADDED SUCCESSFULLY =====")
                    elif y==5:
                        existing_phno = input("Enter the phone number need to be removed : ")
                        h=data[edit_name]['Phone number']
                        if existing_phno in h:
                            h.pop(h.index(existing_phno))
                            print("\n ===== PHONE NUMBER REMOVED SUCCESSFULLY =====")
                        else:
                            print("\n ===== PHONE NUMBER REMOVING FAILED , NOT FOUND IN LIST =====")
                            continue
                    elif y==6:
                        print("\n ===== UPDATED "+edit_name+" SUCCESSFULLY AND EXITED =====\n")
                        c=0
                    elif 1<y>6:
                        print("\n\n!!!!! \t INVALID OPTION FOUND {ENTER A VALID OPTION}  \t!!!!!!")
                        continue
                    else:
                        continue
            else:
                print("\n\n!!!!! \t ENTERED NAME IS NOT IN THE DATABASE (INVALID) \t!!!!!!")
                continue
    elif n==4:
        temp_key = input("Enter the name that need to be removed from the database : ")
        if temp_key in data.keys():
            data.pop(temp_key)
            print("\n ===== PERSON REMOVED SUCCESSFULLY =====")
        else:
            print("\n\n!!!!! \t ENTERED NAME IS NOT IN THE DATABASE (INVALID) \t!!!!!!")
            continue
    elif n==5:
        print ('\n------------------------- EXITED SUCCESSFULLY !!! -------------------------\n')
        i=0
    elif 1<n>5:
        print("\n\n!!!!! \t INVALID OPTION FOUND {ENTER A VALID OPTION}  \t!!!!!!")
        continue
    else:
        continue