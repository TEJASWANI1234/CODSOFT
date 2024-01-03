class Cal:
    def __init__(self):
        self.operations={
            '+':self.add,
            '-':self.subtract,
            '*':self.multiply,
            '/':self.division,
            '%':self.modulus,
            }
        
    def add(self,x, y):
        return x + y

    def subtract(self,x, y):
        return x - y

    def multiply(self,x, y):
        return x * y

    def division(self,x, y):
    
        if y != 0:
            return x / y
        else :
            return "cannot divide by zero"
    def modulus(self,x,y):
        if y!=0:
            return x%y
        else:
            return "Cannot divide by zero."

class calculationhistory:
    def __init__(self):
        self.history=[]
        
    def add_to_history(self,x,y,operation,res):
        entry={'x':x,'y':y,'operation':operation,'res':res}
        self.history.append(entry)
        
    def display_history(self):
        print("calculator history:")
        for entry in self.history:
            print(f"{entry['x']} {entry['operation']} {entry['res']}")

def get_user_input():
    x=float(input("enter first number"))
    y=float(input("enter second number"))
    operation=input("enter the operation(+ ,-, *,/):")
    return x,y,operation

def main():
    calculator=Cal()
    history=calculationhistory()

    while True :
        try:
            x,y,operation=get_user_input()
            if operation in calculator.operations:
                res=calculator.operations[operation](x,y)
                print(f"result :{res}")

                history.add_to_history(x,y,operation,res)
            else:
                print("invalid operation.please enter =,-,*,/ or %.")
        except ValueError as e:
            print(f"Error :{e}")

        another_cal=input("Do youwant perform another operation(yes/no):")
        if another_cal.lower()!="yes":
            history.dispay_history()
            print("Exiting calculator")
            break

if __name__ == "__main__":
    main()

