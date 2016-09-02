
#----------------------------------------------------------
# NOTE: V.1.6
# Auther : Mohammed Alromaih
#----------------------------------------------------------

def Appreciation(GPA):
    if GPA <= 5 and GPA >= 4.50:    # if 4.5 <= GPA <= 5
        appr = "Excellent"
    elif GPA < 4.50 and GPA >= 3.75:
        appr = "Very Good"
    elif GPA < 3.75 and GPA >= 2.75:
        appr = "Good"
    elif GPA < 2.75 and GPA > 2:
        appr = "Pass"
    else :
        appr = "Fail OR NONE"
    return appr



con = True # To control the while loop , if op == 2 the "con" will chinge to False, than while loop finshed.
while con :

    print ("---------------------------------------\n")
    print ("1. Calculate total GPA")
    print ("2. EXIT \n")
    print ("---------------------------------------\n")

    op = input("OPTION: ")
    print ("----------------------------------------\n")
    if op == '1':


        pre_hour = float(input("Enter Your Previose Houre: ")) # G = 124
        pre_gpa = float(input("Previose GPA: ")) # G = 2.88
        pre_point = pre_hour * pre_gpa # to calculate all points.
        #----------------------------------------------------------------------

        hour = float(input("Carrent Houre: ")) # Gusse  = 14
        total = [] # list to insert all points on it ,
        chick = [] # chick all houres in grade List equal the current houre.

        #----------------------------------------------------------------------

        A = int(input("How many Houre For A+: "))
        chick.append(A)
        total.append(A*5)

        a = int(input("How many Houre For A: "))
        chick.append(a)
        total.append(a*4.75)

        B = int(input("How many Houre For B+: "))
        chick.append(B)
        total.append(B*4.50)

        b = int(input("How many Houre For B: "))
        chick.append(b)
        total.append(b*4)

        C = int(input("How many Houre For C+: "))
        chick.append(C)
        total.append(C*3.50)

        c = int(input("How many Houre For C: "))
        chick.append(c)
        total.append(c*3)

        D = int(input("How many Houre For D+: "))
        chick.append(D)
        total.append(D*2.5)

        d = int(input("How many Houre For D: "))
        chick.append(d)
        total.append(d*2)

        F = int(input("How many Houre For F: "))
        chick.append(F)
        total.append(F*1)

        #------------------------------------------------------------------------------
        sums= 0 # points for current semester.
        for i in total:
            sums = float(sums) + float(i)
        #------------------------------------------
        current_hours = 0 # hours inserted for grade, to chick if semester hours and grades hours is equals.
        for i in chick:
            current_hours = int(current_hours) + int(i)
        #------------------------------------------
        # To calculte final GPA.
        all_hours = pre_hour + hour
        all_points = pre_point + sums
        final_gpa = all_points/all_hours
        current_gpa = sums/hour
        #------------------------------------------------------------------------------

        if current_hours == hour:
            print ("--------------------------------------------------------------------------------------\n")
            print ("[+] Your Complite, ", hour , " Hours In This Semester.")
            print ("[+] Your Total Points For this Semester is: ",sums , " Points")
            print ("[+] List of all Grade: ",total)
            print ("[+] GPA For This Semester: ", current_gpa)
            print ("[+] Appreciation: ", Appreciation(current_gpa),"\n")
            print ("--------------------------------------------------------------------------------------\n")
            print ("[+] You Complite,  ", all_hours, " Hours in all Semesters.")
            print ("[+] You Get, ", all_points, " POINTS in all semester.\n")
            print ("--------------------------------------------------------------------------------------\n")
            print ("[+] Final GPA: | " , final_gpa , " |")
            print ("[+] Appreciation: ", Appreciation(final_gpa),"\n")



        else:
            print ("Sorry, Grade Hours not equal Semester Hours")
            print ("Be careful when registering hours and, Try Again")

    elif op == '2':
        print ("Thank You,")
        print ("EXIT")
        con = False

    else:
        print ("Option Not Found, Try Again.")
