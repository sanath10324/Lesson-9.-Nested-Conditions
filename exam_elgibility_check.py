medical_cause = input("Do you have a Medical Cause? Yes or No:")
attendance = int(input("Enter your attendance:"))

if medical_cause == "Yes":
    print("You are allowed to write the Exam.")
else:
    if attendance >= 75:
        print ("You are allowed to write the Exam.")
    else:
        print("You are not allowed to write the Exam.")