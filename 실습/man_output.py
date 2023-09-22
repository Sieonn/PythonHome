import pandas as pd
import numpy as np

def output(man):
    print(f'{"사번"}\t{"급수"}\t{"호"}\t{"수당"}\t{"지급액"}\t{"세금"}\t{"차인금액"}')
    print(f'{man["code"]}\t{man["grade"]}\t{man["호"]}\t{man["수당"]}\t{man["zi"]}\t{int(man["se"])}\t{int(man["cha"])}')
    
data = []