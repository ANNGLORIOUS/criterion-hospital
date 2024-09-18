from helpers import (
    create_patient,
    delete_patient,
    list_patients,
    view_patient,
    create_doctor,
    delete_doctor,
    list_doctors,
    view_doctor,
    create_appointment,
    delete_appointment,
    list_appointments,
    view_appointment
)

def main():
    print("\n")
    print("==================================")
    print("          CRITERION HOSPTAL       ")
    print("    (c) 2024. All rights reserved.")
    print("==================================")

    
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            create_patient()
        elif choice == "2":
            delete_patient()
        elif choice == "3":
            list_patients()
        elif choice == "4":
            view_patient()
        elif choice == "5":
            create_doctor()
        elif choice == "6":
            delete_doctor()
        elif choice == "7":
            list_doctors()
        elif choice == "8":
            view_doctor()
        elif choice == "9":
            create_appointment()
        elif choice == "10":
            delete_appointment()
        elif choice == "11":
            list_appointments()
        elif choice == "12":
            view_appointment()
        else:
            print("Invalid choice")

def menu():
    print("\033[31m=====CRITERION HOSPITAL =====\033[0m")
    print("Please select an option:")
    print("0. Exit the program")
    print("\n")
    print("PATIENT'S RECORDS")
    print("......")
    print("\n")
    print("1. Create a patient")
    print("2. Delete a patient")
    print("3. List all patients")
    print("4. View patient details")
    print("\n")
    print("DOCTOR'S RECORDS")
    print("......")
    print("\n")
    print("5. Create a doctor")
    print("6. Delete a doctor")
    print("7. List all doctors")
    print("8. View doctor details")
    print("\n")
    print("APPOINTMENT'S RECORDS")
    print("......")
    print("\n")
    print("9. Create an appointment")
    print("10. Delete an appointment")
    print("11. List all appointments")
    print("12. View appointment details")

if __name__ == "__main__":
    main()