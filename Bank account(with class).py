class BankAccount:
    def __init__(self,name,surname):
        self.fullName = name + " " + surname
        self.balance = 0


    def withdraw(self):
        withdrawmoney = float(input("How much money do you want to withdraw?"))
        if self.balance < withdrawmoney or withdrawmoney < 0:
            print('Invalid count of money')

        else:
            self.balance -= withdrawmoney
            print(f"Balance: {self.balance}")
    
    def deposit(self):
        depositmoney = float(input("How much money do you want to deposit?"))
        if depositmoney < 1:
            print("Invalid count of money")
        else:
            self.balance += depositmoney
            print(f"Balance: {self.balance}")



class LogIn:
    def __init__(self,accountsArr):
        self.accountsArr = accountsArr

    def LogIn(self):
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        password = input("Enter your password: ")
        for arr in self.accountsArr:
            if arr[0][0] == name and arr[0][1] == surname and arr[0][2] == password:
                return True, arr[1]
        return False,


class Register:
    @staticmethod
    def register():
        name = input("Enter your name: ")
        surname = input("Enter your surname: ")
        while True:
            password = input("Enter your password(LIMIT 6): ")
            if len(password) < 4:
                print("It is not safe code. Write it again! ")
                continue
            break
        arr = [name,surname,password]
        return arr
    
accountsArr = []
while True:
    action = input('What would you want to do (REGISTER or LOGIN or EXIT): ').strip().lower()
    if action == "register":
        user = Register.register()
        BankAccountRegister = BankAccount(user[0], user[1])
        accountsArr.append([user,BankAccountRegister])
    elif action == "login":
        while True:
            checkAccount = LogIn(accountsArr).LogIn()
            if checkAccount[0]:
                option = input("What would like to do? (WITHDRAW,DEPOSIT,BALANCE): ").strip().lower()
                if option == "balance": 
                    print(checkAccount[1].balance)
                elif option == "withdraw":
                    checkAccount[1].withdraw()
                elif option == "deposit":
                    checkAccount[1].deposit()
                else: 
                    print("Invalid option")
                
                exitOption = input("Would you like to exit?:  ").strip().lower()
                if exitOption == "yes":
                    break

    
            else:
                print("There is no any user like that!")
    elif action == "exit":
        break
        

            




