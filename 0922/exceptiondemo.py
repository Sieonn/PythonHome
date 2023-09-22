#exception은 예외처리라고 생각한다. 예외는 이벤트이다.
first = int(input("Enter a first number : "))
second = int(input("Enter a second number : "))

try: #오류가 발생할 가능성이 높은 부분, 좀 더 주의
    print(f'{first}/{second} = {first/second}')


#except:
#   print("Invaild")
except Exception as err: #이렇게 사용하면 에러에 대한 메시지가 뜬다.
    print(err)
    
# else:
#     print("program is over")  #except가 발생하지 않았을때: 정상적으로 처리 됐을때 실행된다. except의 else이다.
finally :#파일처리나 디비 처리는 반드시 파이널리를 사용해줘야한다.
    print("Program is Over")