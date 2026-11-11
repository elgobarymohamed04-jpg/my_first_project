def Mini_hr_System():
    d = {}
    number_of_employee = int(input("Enter number of employees: "))

    for a in range(0, number_of_employee):
        name = input("Enter your name: ")
        name = name.lower().strip()
        iD = int(input("Enter your ID: "))
        dept = input("Enter your dept: ").lower().strip() 
        base_salary = int(input("Enter your base salary: "))
        absence_days = int(input("Enter your absence days: "))
        bonus = int(input("Enter your bonus: "))

        d[iD] = {
            "name": name,
            "dept": dept,
            "base_salary": base_salary,
            "absence_days": absence_days,
            "bonus": bonus
        }
        print("_" * 50)


    def Calculate_Net_Salary(iD): 
        if iD not in d:
            return "The employee not found"
        
        net = (d[iD]["base_salary"] + d[iD]["bonus"]) - (d[iD]["absence_days"] * 500 + (d[iD]["base_salary"] / 10))
        return net      


    def Update_Employee_Profiles(iD, new_salary): 
        if iD not in d:
            print("The employee not found")
            return
        
        d[iD]["base_salary"] = new_salary
        print(f"Employee salary updated, now = {new_salary}")


    def Search_by_Department(dept): 
        dept = dept.lower().strip()
        found = False
        for i in d:
            if dept == d[i]["dept"]:
                print(i, d[i], "\n")
                found = True
        if not found:
            print("No employees found in this department.")




    def Monthly_Salary_Slips(iD):
        if iD not in d:
            print("The employee not found")
            return

        net_salary = Calculate_Net_Salary(iD)

        print("\n" + "="*30)
        print("      MONTHLY SALARY SLIP      ")
        print("="*30)
        print(f'Name=>              :{d[iD]["name"]}') 
        print(f'ID=>                :{iD}') 
        print(f'Department=>        :{d[iD]["dept"]}')   
        print(f'Base Salary=>       :{d[iD]["base_salary"]}') 
        print(f'Bonuses=>           :{d[iD]["bonus"]}') 
        print(f'Absence Days=>      :{d[iD]["absence_days"]}')   
        print(f'NET SALARY=>        :{net_salary}')
    



    def Print_Attendance_Report(iD): 
        if iD not in d:
            print("The employee not found")
            return
            
        print("--- Company Attendance Report ---")      
        print(f'Employee: {d[iD]["name"]}, Absence days: {d[iD]["absence_days"]}')  


    while True:
        print("_"*50)
        print("          HR SYSTEM MENU          \n","*"*40,"\n")
        print("1. Search employees by department")
        print("2. Print Monthly Salary Slip")
        print("3. Print Attendance Report")
        print("4. Update employee salary")
        print("5. Exit System")
        print("_"*50)


        choice = input("Enter your choice (1-5): ").strip()
        if choice =="1":
            dep = input("Enter the dept where you want to search: ").lower().strip()
            Search_by_Department(dep)
        elif choice=="2":
            t_iD = int(input("Enter the ID of the employee for salary slip: "))
            Monthly_Salary_Slips(t_iD)
        elif choice == '3':
            t_iD = int(input("Enter the ID of the employee for attendance report: "))
            Print_Attendance_Report(t_iD)
            
        elif choice == '4':
            u_iD = int(input("Enter the ID of the employee to update: "))
            new_sa = int(input("Enter new salary: "))
            Update_Employee_Profiles(u_iD, new_sa)
            
        elif choice == '5':
            print("Exiting the HR System. Goodbye!")
            break 
            
        else:
            print("Invalid choice! Please try again.")    



Mini_hr_System()
