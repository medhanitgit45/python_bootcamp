def calculator():
    print("standard calculeter")
    try:
        while True:
            op=input("enter the operator [/,*,-,+,** and exit ]")
            if op.lower().strip()=="exit":
                print("exiting calculator")
                break
            list_op=['+','-','/','**','*']
            if op not in list_op:
                print("invalid operator")
                continue
            number=[]
            while True:
                number=input("please enter the correct operator")
                if number=="=":
                    if len(number)<2:
                        print("please enter ar least 2 number")
                        continue
                    break
                try:
                    num = float(number)
                    number.append(num)
                except ValueError:
                    print("please enter only number")
                    continue
            """performing different arthimetic operations
            after performing arthimetic
            operations we have to store the result on some variable"""
            if op =="+":
                result = number[0]
                for item in number[1:]:
                    result = result + item
                print(" + ".join(map(str, number)) + f" = {result}")
            elif op == "*":
                result = number[0]
                for item in number[1:]:
                    result = result * item
                print("*".join(map(str, number)) + f" ={result}")
            elif op == "/":
                result = number[0]
                for item in number[1:]:
                    try:
                        if item ==0:
                            raise ZeroDivisionError()
                        result = result / item
                    except ZeroDivisionError:
                        print("Denominator can't be zero")
                        continue
                    print(" /".join(map(str, number)) + f" ={result}")
            elif op == "=":
                    result = number [0]
                    for item in number[1:]:
                        result =result = item
                    print(" = ".join(map(str, number)) + f" ={result}")
            elif op == "**":
                    result = number[0]
                    for item in number[1:]:
                        result = result ** item
                    print(" ** ".join(map(str, number)) + f" ={result}")
    except Exception as e:
     print(f"oprration failed! {e}")
    print("develop By: fire")      
    
calculator()
# by medhanit
