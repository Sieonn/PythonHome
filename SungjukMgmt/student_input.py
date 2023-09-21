#student_input.py

def my_input(student) :
    name = input("Enter your name:")
    kor = int(input("Enter your Korean:"))
    eng = int(input("Enter your English:"))
    math = int(input("Enter your math:"))
    
    student["name"] = name
    student["eng"] = eng 
    student["kor"] = kor
    student["math"] = math
    
    