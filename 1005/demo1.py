from django.conf import settings

conn = pymysql.connect(port=port, user=user, host=host, password=passward, database=database)

cursor = conn.cursor()
sql = "SELECET EMPNO, ENAME, JOB, SAL, DEPTNO FROM EMP WHERE DEPTNO = 20"
cursor.excute(sql)
result = cursor.fetchall()
for emp in result:
    print(emp[1], emp[3], sep = ',')
cursor.close()
conn.close()