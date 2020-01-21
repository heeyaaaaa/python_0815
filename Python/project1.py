import sys

if len(sys.argv)==1 or sys.argv[1] == "students.txt":
    file = open("students.txt","r")
    
else:
    arg = sys.argv[1]
    file = open(arg, "r")
    
stu_dict={}


for stu in file.readlines():
    info = stu[:-1].split('\t')
    ID = info[0]
    stu_dict[ID] = info[1:]
    stu_dict[ID][1] = int(stu_dict[ID][1])
    stu_dict[ID][2] = int(stu_dict[ID][2])
    
def Grade_df(Avg):
    if Avg >=90 :
        Grade = "A"
    elif Avg >=80 and Avg <90 :
        Grade = "B"
    elif Avg >=70 and Avg <80 :
        Grade = "C"
    elif Avg >=60 and Avg <70 :
        Grade = "D"
    else:
        Grade = "F"
    return Grade

for ID,info  in stu_dict.items():
    Mid = info[1]
    Final = info[2]
    Avg = (Mid+Final)/2
    stu_dict[ID].append(Avg)
    Grade = Grade_df(Avg)
    stu_dict[ID].append(Grade)
    
    
def sort(stu_dict):
    sort_st = sorted(stu_dict.items(), key = lambda a : a [1][3], reverse = True)
    return sort_st
sort_st = sort(stu_dict)

print("Student \t Name \t  Midterm \tFinal \t Average \tGrade")
print("-"*70)
for stu in sort_st:
    ID = stu[0]
    Name = stu[1][0]
    Mid = stu[1][1]
    Final = stu[1][2]
    Avg = stu[1][3]
    Grade = stu[1][4] 
    
    print("%s\t%s\t%s\t%s\t%.1f \t%s" %(ID, Name, Mid, Final, Avg, Grade))
    
do_list = ['show', 'search', 'changescore', 'searchgrade', 'add', 'remove', 'quit']



def show(stu_dict):        
    print("Student \t Name \t  Midterm \tFinal \t Average \tGrade")
    print("-"*70)
    sort_st = sort(stu_dict)

    for stu in sort_st:
        ID = stu[0]
        Name = stu[1][0]
        Mid = stu[1][1]
        Final = stu[1][2]
        Avg = stu[1][3]
        Grade = stu[1][4] 

        print("%s\t%s\t%s\t%s\t%.1f \t%s" %(ID, Name, Mid, Final, Avg, Grade))
        
def search(ID, stu_dict):
    if ID not in stu_dict:
        print("NO SUCH PERSON.")
    else:
        print("Student \t Name \t  Midterm \tFinal \t Average \tGrade")
        print("-"*70)
        Name = stu_dict[ID][0]
        Mid = stu_dict[ID][1]
        Final = stu_dict[ID][2]
        Avg = stu_dict[ID][3]
        Grade = stu_dict[ID][4] 
        print("%s\t%s\t%s\t%s\t%.1f \t%s" %(ID, Name, Mid, Final, Avg, Grade))        
        
        
        
def update(ID, score, mid = 1):
    if score in range(101):
        print("Student \t Name \t  Midterm \tFinal \t Average \tGrade")
        print("-"*70)
        ID = str(ID)
        Name = stu_dict[ID][0]
        Mid = stu_dict[ID][1]
        Final = stu_dict[ID][2]
        Avg = stu_dict[ID][3]
        Grade = stu_dict[ID][4] 
        print("%s\t%s\t%s\t%s\t%.1f \t%s" %(ID, Name, Mid, Final, Avg, Grade))
        print("Score changed.")
        stu_dict[ID][mid] = score
        Mid = stu_dict[ID][1]
        Final = stu_dict[ID][2]
        stu_dict[ID][3] = Avg = (Mid+Final)/2
        stu_dict[ID][4] = Grade = Grade_df(Avg)                 
        print("%s\t%s\t%s\t%s\t%.1f \t%s" %(ID, Name, Mid, Final, Avg, Grade))
        sort_st = sort(stu_dict)
        
        
def changescore(ID, stu_dict):
    if ID not in stu_dict:
        print("NO SUCH PERSON.")
    else:
        Q = input("Mid/Final? ")
        A_ls = ['MID','FINAL']
        if Q.upper() not in A_ls:
            pass
        elif Q.upper() == "MID":
                mid_update = input("Input new score: ")
                update(ID, int(mid_update))
        else:
            final_update = input("Input new score: ")
            update(ID, int(final_update), 2)
                

                
def add(ID, stu_dict):
    if ID in stu_dict:
        print("ALREADY EXISTS.")
    else:
        Name = input("Name: ")
        Mid = int(input("Midterm Score: "))
        Final = int(input("Final Score: "))
        Avg = (Mid + Final)/2
        Grade = Grade_df(Avg)
        st_info = list([Name, Mid, Final, Avg, Grade])
        stu_dict[ID] = st_info
        print("Student added.")
        
        
        
def searchGrade(Grade, stu_dict):
    stu_Grade_ls = []
    for i in stu_dict.values():
        stu_Grade_ls.append(i[4])


    if Grade not in list(['A','B','C','D','F']):
        pass
    else:
        if Grade not in stu_Grade_ls:
            print("NO RESULTS.")
        else:
            print("Student \t Name \t  Midterm \tFinal \t Average \tGrade")
            print("-"*70)
            for ID, info in stu_dict.items():
                for g in info[4]:
                    if g == Grade:
                        Name = stu_dict[ID][0]
                        Mid = stu_dict[ID][1]
                        Final = stu_dict[ID][2]
                        Avg = stu_dict[ID][3]
                        print("%s\t%s\t%s\t%s\t%.1f \t\t%s" %(ID, Name, Mid, Final, Avg, Grade))
    

def remove(stu_dict):
    if stu_dict == {}:
        print("List is empty")
    else:
        ID = input("Student ID: ")
        if ID not in stu_dict:
            print("NO SUCH PERSON.")
        else:
            del stu_dict[ID]
            print("Student removed")

def quit(Q, stu_dict):
    if Q.upper() == "YES":
        f_name = input("File name: ")
        f = open(f_name, 'w')
        sort_st = sort(stu_dict)
        for stu in sort_st:
            ID = stu[0]
            Name = stu[1][0]
            Mid = stu[1][1]
            Final = stu[1][2]
            data = "%s\t%s\t%s\t%s\n" %(ID, Name, Mid, Final)
            f.write(data)
        f.close()
        print("$")    


while True:

    do = ''
    while do not in do_list :
        do = input("#")


    if do.upper() == 'SHOW':
        show(stu_dict)
     


    if do.upper() == 'SEARCH':
        ID = input("Student ID: ")
        search(ID, stu_dict)
            


    if do.upper() == "CHANGESCORE":
        ID = input("Student ID: ")
        changescore(ID, stu_dict)

                
                
    if do.upper() == "ADD":
        ID = input("Student ID: ")
        add(ID, stu_dict)

                
                
    
    if do.upper() == "SEARCHGRADE":
        Grade = input("Grade to search: ")
        searchGrade(Grade, stu_dict)
        

    if do.upper() == "REMOVE":
        remove(stu_dict)

            
            
    if do.upper() == "QUIT":
        Q = input("Save data?[yes/no] ")
        quit(Q, stu_dict)

        break


