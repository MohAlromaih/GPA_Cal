#----------------------------------------------------------
# NOTE: New V.2.1 , Calculate GPA From 4 and 5 , check if Previose GPA <= 5 or <= 4
# NOTE: Last V.1.6 , Calculate GPA From Just 5
# Auther : Mohammed Alromaih
# Start Date : 14 August 2016
# Last Date : 16 August 2016
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

def Appreciation4(GPA):
    if GPA <= 4 and GPA >= 3.50:    # if 3.5 <= GPA <= 4
        appr = "Excellent"
    elif GPA < 3.50 and GPA >= 2.75:
        appr = "Very Good"
    elif GPA < 2.75 and GPA >= 1.75:
        appr = "Good"
    elif GPA < 1.75 and GPA > 1:
        appr = "Pass"
    else :
        appr = "Fail OR NONE"
    return appr
#____________________________________________________________________________________________________________________________________________________________________

con = True # To control the while loop , if op == 2 the "con" will chinge to False, than while loop finshed.
while con :

    print ("---------------------------------------\n")
    print ("1. Calculate Total GPA From 5")
    print ("2. Calculate Total GPA From 4")
    print ("3. EXIT \n")
    print ("---------------------------------------\n")

    op = input("OPTION: ")
    print ("----------------------------------------\n")
#________________________________________________________GPA From 5________________________________________________________________________________________________
    if op == '1':


        pre_hour = float(input("Enter Your Previous  Houre: ")) # input The Completed hours in all Semesters.
        #----------------------------------------------------------------------
        while True:

            pre_gpa = float(input("Last GPA: "))
            if pre_gpa <= 5 and pre_gpa >= 0:
                break
            print ("Last GPA is not correct.")
        #---------------------------------------------------------------------
        pre_point = pre_hour * pre_gpa # to calculate all points.
        #----------------------------------------------------------------------

        hour = float(input("Current Houre: "))
        total = [] # list to insert all points on it ,
        chick = [] # check all hours in grade hours List is equal the current hour.

        #----------------------------------------------------------------------
        # To Calculate Points and Chick Hours
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
        sums= 0 # Sum all points for current semester.
        for i in total:
            sums = float(sums) + float(i)
        #------------------------------------------
        current_hours = 0 # Sum all hours inserted for grade, to check if semester hours and grades hours is equals.
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
            print ("-------------------------- [Current Semester] -----------------------------------------\n")
            print ("[+] You Complete ", hour , " Hours In This Semester.")
            print ("[+] Your Total Points For this Semester is: ",sums , " Points")
            print ("[+] List of all Grade: ",total)
            print ("[+] GPA For This Semester: ", current_gpa)
            print ("[+] Appreciation: ", Appreciation(current_gpa),"\n")
            print ("-------------------------- [ALL Semesters] -------------------------------------------\n")
            print ("[+] You Complete,  ", all_hours, " Hours in all Semesters.")
            print ("[+] You Get, ", all_points, " POINTS in all Semester.")
            print ("[+] Final GPA: | " , final_gpa , " |")
            print ("[+] Appreciation: ", Appreciation(final_gpa),"\n")



        else:
            print ("Sorry, Grade Hours it not equal Semester Hours")
            print ("Be careful when registering hours and, Try Again")

#________________________________________________________________GPA From 4____________________________________________________________________________________________

    elif op == '2':


        pre_hour4 = float(input("Enter Your Previous Houre: "))
        #----------------------------------------------------------------------
        while True:

            pre_gpa4 = float(input("Last GPA: "))
            if pre_gpa4 <= 4 and pre_gpa4 >= 0:
                break
            print ("Last GPA is not correct.")
        #----------------------------------------------------------------------
        pre_point4 = pre_hour4 * pre_gpa4 # to calculate all points.
        #----------------------------------------------------------------------

        hour4 = float(input("Current Houre: "))
        total4 = [] # list to insert all points on it ,
        chick4 = [] # check all houres in grade List equal the current houre.

        #----------------------------------------------------------------------
        # calculate GPA from 4
        A4 = int(input("How many Houre For A+: "))
        chick4.append(A4)
        total4.append(A4*4)

        a4 = int(input("How many Houre For A: "))
        chick4.append(a4)
        total4.append(a4*3.75)

        B4 = int(input("How many Houre For B+: "))
        chick4.append(B4)
        total4.append(B4*3.50)

        b4 = int(input("How many Houre For B: "))
        chick4.append(b4)
        total4.append(b4*3)

        C4 = int(input("How many Houre For C+: "))
        chick4.append(C4)
        total4.append(C4*2.50)

        c4 = int(input("How many Houre For C: "))
        chick4.append(c4)
        total4.append(c4*2)

        D4 = int(input("How many Houre For D+: "))
        chick4.append(D4)
        total4.append(D4*1.5)

        d4 = int(input("How many Houre For D: "))
        chick4.append(d4)
        total4.append(d4*1)

        F4 = int(input("How many Houre For F: "))
        chick4.append(F4)
        total4.append(F4*0)

        #------------------------------------------------------------------------------
        sums4= 0 # points for current semester.
        for i in total4:
            sums4 = float(sums4) + float(i)
        #------------------------------------------
        current_hours4 = 0 # hours inserted for grade, to check if semester hours and grades hours is equals.
        for i in chick4:
            current_hours4 = int(current_hours4) + int(i)
        #------------------------------------------
        # To calculte final GPA.
        all_hours4 = pre_hour4 + hour4
        all_points4 = pre_point4 + sums4
        final_gpa4 = all_points4/all_hours4
        current_gpa4 = sums4/hour4
        #------------------------------------------------------------------------------

        if current_hours4 == hour4:
            print ("-------------------------- [Current Semester] -----------------------------------------\n")
            print ("[+] You Complete ", hour4 , " Hours In This Semester.")
            print ("[+] Your Total Points For this Semester is: ",sums4 , " Points")
            print ("[+] List of all Grade: ",total4)
            print ("[+] GPA For This Semester: ", current_gpa4)
            print ("[+] Appreciation: ", Appreciation4(current_gpa4),"\n")
            print ("-------------------------- [ALL Semesters] -------------------------------------------\n")
            print ("[+] You Complete ", all_hours4, " Hours in all Semesters.")
            print ("[+] You Get, ", all_points4, " POINTS in all semester.")
            print ("[+] Final GPA: | " , final_gpa4 , " |")
            print ("[+] Appreciation: ", Appreciation4(final_gpa4),"\n")



        else:
            print ("Sorry, Grade Hours it not equal Semester Hours")
            print ("Be careful when registering hours and, Try Again")

#______________________________________________________________ EXIT _____________________________________________________________________________________

    elif op == '3':
        print ("Thank You,")
        print ("EXIT")
        con = False
#__________________________________________________________________________________________________________________________________________________________

    else:
        print ("Option Not Found, Try Again.")
