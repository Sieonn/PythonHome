import man_input

def my_calc(man):
    급여 = 0
    for i in range(1,6):
        if man["grade"] == int(1) and man["호"] == i:
            급여 = 95000 - 3000*(i-1)
        elif man["grade"] == int(2) and man["호"] == i:
            급여 = 80000 - 5000*(i - 1)
        else:
            None
    zi = 급여 + man["수당"]
# def my_tax(man):
    se = 0
    sel = 0
    zo = 0
    if zi < 70000:
        sel = int(0)
        zo = 0
        se = 0
    elif 70000 <= zi < 80000:
            sel = 0.005
            zo = 300
            se = (int(zi)*sel) - zo
    elif 80000 <= zi < 89999:
        sel = 0.007
        zo = int(500)
        se = (int(zi)*sel) - zo
    else:
        sel = 0.012
        zo = int(1000)
        se = (int(zi)*sel) - zo
        
    cha = int(zi) - se 
                       
    man["se"] = se
    man["zi"] = zi
    man["cha"] = cha