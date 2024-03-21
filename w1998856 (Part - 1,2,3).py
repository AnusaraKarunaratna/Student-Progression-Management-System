# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.

# Student ID: 20220547
# Date: 2023/04/16


#Assign variables to get inputs
pass_credits=0
defer_credits=0 
fail_credits=0


#Creating lists for part 2
exclude_list =[]
retriever_list =[]
trailer_list =[]
progress_list =[]
credit_list = []

#Assign variables to get count
progress_total = 0
retriever_total = 0
exclude_total = 0
trailer_total = 0

#Function to check the level according to the given credits
    
def get_status(pass_credits, defer_credits, fail_credits):
        
    if pass_credits == 120:
        return "Progress"
        
    elif pass_credits == 100 and (defer_credits == 20 or fail_credits == 20):
        return "Progress (module trailer)"
        
    elif pass_credits in range(0, 81) and defer_credits in range(0, 121) and fail_credits in range(0, 61):
        return "Do not Progress - module retriever"
        
    elif pass_credits in range(20, 41) and defer_credits in range(20, 41) and fail_credits in range(80, 121):
        return "Exclude"

    else:
        return ""


#################  Function for part 2  ##########################


def part2(progress_list,trailer_list,retriever_list,exclude_list):
    print("\n----------------------------------------------------------------------------")
    print("\nPART 2\n")

        
#To print the given inputs and corresponding level using list
        
    for i in range(0,len(progress_list)): 
        print('Progress - ',end='')
        print(progress_list[i][0],end=', ')
        print(progress_list[i][1],end=', ')
        print(progress_list[i][2])

    for i in range(0,len(trailer_list)):
        print('Progress (module trailer) - ',end='')
        print(trailer_list[i][0],end=', ')
        print(trailer_list[i][1],end=', ')
        print(trailer_list[i][2])

    for i in range(0,len(retriever_list)):
        print("Module retriever - ",end='')
        print(retriever_list[i][0],end=', ')
        print(retriever_list[i][1],end=', ')
        print(retriever_list[i][2])

    for i in range(0,len(exclude_list)):
        print('Exclude - ',end='')
        print(exclude_list[i][0],end=', ')
        print(exclude_list[i][1],end=', ')
        print(exclude_list[i][2])
        print(" ")


################# Function for part 3  ############################


def part3(progress_list,trailer_list,retriever_list,exclude_list):
# To open text file
    
    txtfile = open("Part - 3 .txt", "w") 
    txtfile.write("---PART 3---\n\n")


#To write the outcomes in the opened text file

    for item in range(0,len(progress_list)): 
        txtfile.write('Progress - ')
        txtfile.write(str(progress_list[item][0]) + ', ')
        txtfile.write(str(progress_list[item][1]) + ', ')
        txtfile.write(str(progress_list[item][2]) + '\n')

    for item in range(0,len(trailer_list)):
        txtfile.write('Progress (module trailer) - ')
        txtfile.write(str(trailer_list[item][0]) + ', ')
        txtfile.write(str(trailer_list[item][1]) + ', ')
        txtfile.write(str(trailer_list[item][2]) + '\n')

    for item in range(0,len(retriever_list)):
        txtfile.write("Module retriever - ")
        txtfile.write(str(retriever_list[item][0]) + ', ')
        txtfile.write(str(retriever_list[item][1]) + ', ')
        txtfile.write(str(retriever_list[item][2]) + '\n')
        
    for item in range(0,len(exclude_list)):
        txtfile.write('Exclude - ')
        txtfile.write(str(exclude_list[item][0]) + ', ')
        txtfile.write(str(exclude_list[item][1]) + ', ')
        txtfile.write(str(exclude_list[item][2]) + '\n')

    txtfile.close() 
    
    for i in range(0,len(progress_list)): 
        print('Progress - ',end='')
        print(progress_list[i][0],end=', ')
        print(progress_list[i][1],end=', ')
        print(progress_list[i][2])

    for i in range(0,len(trailer_list)):
        print('Progress (module trailer) - ',end='')
        print(trailer_list[i][0],end=', ')
        print(trailer_list[i][1],end=', ')
        print(trailer_list[i][2])

    for i in range(0,len(retriever_list)):
        print("Module retriever - ",end='')
        print(retriever_list[i][0],end=', ')
        print(retriever_list[i][1],end=', ')
        print(retriever_list[i][2])

    for i in range(0,len(exclude_list)):
        print('Exclude - ',end='')
        print(exclude_list[i][0],end=', ')
        print(exclude_list[i][1],end=', ')
        print(exclude_list[i][2])
        print(" ")

    print("\nOpen the text file named 'Part-3' to view text file results")

#Creating the list with numbers that can be taken as values.
values = [0,20,40,60,80,100,120]


######################   Part 1  #################################


#To get user inputs 

while True:
    try:
    
        pass_credits = int(input("\nPlease enter your credits at pass :"))
        if pass_credits not in values:
            print("Out of range")
            continue

        defer_credits = int(input("Please enter your credits at defer :"))
        if defer_credits not in values:
            print("Out of range")
            continue

        fail_credits = int(input("Please enter your credits at fail :"))
        if fail_credits not in values:
            print("Out of range") 
            continue

        total_credits = pass_credits + defer_credits + fail_credits
        if (total_credits != 120):
            print("\nTotal incorrect") #To inform about incorrect input
            continue
        

    except ValueError:
        print("\nInteger required") #To inform about incorrect input
        continue


    try:

        status = get_status(pass_credits, defer_credits, fail_credits)
        print(status)#Calling the function to check the level according to the given credits
        

#To append lists according to the level and to get coount of each level
        
        if status == "Progress":
            progress_total += 1
            credit_list =[pass_credits,defer_credits,fail_credits]
            progress_list.append(credit_list)
            
        elif status == "Progress (module trailer)":
            trailer_total += 1
            credit_list =[pass_credits,defer_credits,fail_credits]
            trailer_list.append(credit_list)
            
        elif status == "Do not Progress - module retriever":
            retriever_total += 1
            credit_list =[pass_credits,defer_credits,fail_credits]
            retriever_list.append(credit_list)
            
        elif status == "Exclude":
            exclude_total += 1
            credit_list =[pass_credits,defer_credits,fail_credits]
            exclude_list.append(credit_list)
            

#To repeat the program 
            
        user_pref = input("\nWould you like to enter another set of data? Enter 'y' for yes or 'q' to quit and view results: ")
        if user_pref.lower() == 'y':
            continue


#To print histogram
        
        elif user_pref.lower() == 'q':
            print("\n----------------------------------------------------------------------------")
            print("Histogram\n")
            
            print("Progress",progress_total,"      :",progress_total*"*" )   
            
            print("Trailer",trailer_total,"       :",trailer_total*"*")
            
            print("Retriever",retriever_total,"     :",retriever_total*"*")
            
            print("Exclude",exclude_total,"       : ",exclude_total*"*")

            print()
            total_outcome=progress_total+trailer_total+retriever_total+exclude_total
            print(total_outcome,"outcomes in total.\n")
            print("----------------------------------------------------------------------\n")
                
        else:
            print("Invalid input")
            
            
            
        part2(progress_list,trailer_list,retriever_list,exclude_list)#Calling the function to execute part 2
        break
    
    
    except ValueError as e:
        print(e)
        
print("\n----------------------------------------------------------------------------")
print("\nPART 3\n")        
part3(progress_list,trailer_list,retriever_list,exclude_list)#Calling the function to execute part 3
