#main.py
import student_calc
import student_input
import student_output

print("Program is start")
student = {}
student_input.my_input(student) #call by Reference
student_calc.calc(student)
student_output.output(student)

print("Program is over...")
