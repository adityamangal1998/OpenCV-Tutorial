import os
for i in range(0,3):
    print("--------------------------------------------------------------------------------")
print()
print("\t\t\tFace Recognition Project")
print()
for i in range(0,3):
    print("--------------------------------------------------------------------------------")


while True:
    print("Enter 1 for storing your face")
    print("Enter 2 for train your face")
    print("Enter 3 for testing your project")
    print("Enter 0 for Exit")
    n=int(input())
    if n==1:
        os.system("face_dataset.py")
    elif n==2:
        os.system("face_training.py")
    elif n==3:
        os.system("face_recognition.py")
    elif n==0:
        print("Have a good day")
        break
    else:
        print("Invalid Input")
    print()



