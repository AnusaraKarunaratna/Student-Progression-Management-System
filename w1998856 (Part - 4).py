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
results ={}


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

#Function to save student marks to dict
def save_dic(status,pass_credits,defer_credits,fail_credits):
    studentr ={}
    studentr[status] =[pass_credits,defer_credits,fail_credits]
    return studentr

#Function to print student results 
def print_dic(results):
    outcome = ""
    for key,value in results.items():
        for status,marks in value.items():
            outcome = status+" - "+str(marks[0])+" , "+str(marks[1])+" , "+str(marks[2])
        print(key,':',outcome)


#Creating the list with numbers that can be taken as values.
values = [0,20,40,60,80,100,120]


######################   Part 1  #################################


#To get user inputs 

while True:
    try:
        studentid = input("Enter your student ID :")
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

 
#To call functions
    try:

        status = get_status(pass_credits, defer_credits, fail_credits)
        print(status) #To get the status of credits
 
        studentr = save_dic(status,pass_credits,defer_credits,fail_credits) #To save student marks to dict
        results[studentid] = studentr 
        
       
            
#To repeat the program    
        user_pref = input("\nWould you like to enter another set of data? Enter 'y' for yes or 'q' to quit and view results: ")
        print("\n")
        if user_pref.lower() == 'y':
            continue
        if user_pref.lower() == 'q':
            print_dic(results) #To print student results
            break


            
    except ValueError as e:
        print(e)
