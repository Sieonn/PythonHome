def my_input(man):
    code = int(input("사원번호 :"))
    grade = int(input("급 :"))
    ho = int(input("호 :"))
    su = int(input("수당:"))

    
    man["code"] = code
    man["grade"] = grade
    man["호"] = ho
    man["수당"] = su
    