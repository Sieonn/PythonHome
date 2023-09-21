#main.py
import  man_input
import  man_output
import  man_calc

# print("Program is start")
man = {}
man_input.my_input(man) #call by Reference
man_calc.my_calc(man)
man_output.output(man)
