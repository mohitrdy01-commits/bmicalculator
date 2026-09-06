from calculations import (
    bmi_records,
    inserting_bmi_user,
    deleting_user,
    updating_user,
    search_user,
    add_bmi_history,
    view_bmi_history
)


while True:

    print()
    print("====================================")
    print("       BMI MANAGEMENT SYSTEM")
    print("====================================")

    print("1. View all BMI records")
    print("2. Insert BMI user")
    print("3. Delete user")
    print("4. Update user")
    print("5. Search user")
    print("6. Add BMI history")
    print("7. View BMI history")
    print("8. Exit")

    print("====================================")

    try:

        choice = int(input("Enter your option: "))

        if choice == 1:

            bmi_records()

        elif choice == 2:

            inserting_bmi_user()

        elif choice == 3:

            user_id = int(input("Enter user ID: "))

            deleting_user(user_id)

        elif choice == 4:

            updating_user()

        elif choice == 5:

            search_user()

        elif choice == 6:

            add_bmi_history()

        elif choice == 7:

            view_bmi_history()

        elif choice == 8:

            print("Thank you for using BMI Management System!")
            break

        else:

            print("Please select a valid option.")

    except ValueError:

        print("Please enter a number.")
        
        

