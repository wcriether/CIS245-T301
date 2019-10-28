class BankingAccount:
    """Estblishing Parent Class within the program"""
    
    def __init__(self):
        """Defining these attributes within '__init__' function due to other functions needing a reference. Aside from, the account number"""
        self.accnt_num = float(input("Hello User. Please enter your account number: "))
        self.accnt_bal = float(input("Thank You. Please enter the account balance: "))

    def withdrawl(self):
        withdraw_amnt = float(input("Please enter the amount that you wish to withdraw from this acocunt: "))
        if withdraw_amnt > self.accnt_bal:
            print("ERROR. Due to insufficent funds, the amount you are requesting is denied.")
        else:
            self.accnt_bal = self.accnt_bal - withdraw_amnt
            print("Thank you. The following ammount has been subtracted from your account:", self.accnt_bal)
    
    def deposit(self):
        deposit_amnt = float(input("Please enter the amount that you wish to deposit into this account: "))
        self.accnt_bal = self.accnt_bal + deposit_amnt
        print("Thank you. The following amount has been added into your account:", deposit_amnt)
        print("Your new balance in this account is:", self.accnt_bal)

    def get_bal(self):
         print("Your current balance within this account is:", self.accnt_bal)


class CheckingAccount(BankingAccount):
    def deduct_fee(self, fee=5):
        self.fee=fee
        if self.fee <= self.accnt_bal:
            self.accnt_bal = self.accnt_bal - 5
            print("A fee of $5.00 has been applied to your account.")
            print("Your current balance in this account is:", self.accnt_bal)
        else:
            print("ERROR. Fees cannot be deducted from this account due to insufficient funds.")

    def mini_bal(self, mini_bal=50):
            self.mini_bal = mini_bal
            if self.accnt_bal > self.mini_bal:
                print("\n Your account is above the minimum balance requirement.")
                print("\n Your current balance in this account is:", self.accnt_bal)
            else:
                print("\n ERROR. Your account is below the minimum balance requirement.")
                print("\n Your current balance in this account is:", self.accnt_bal)
                        

class SavingsAccount(CheckingAccount):
    def addInterest(self, interestRate=2):
        interest_amnt = (self.accnt_bal*2)/100;
        self.accnt_bal = self.accnt_bal + interest_amnt
        print("Your new balance after adding the bank's interest rate is:", self.accnt_bal)


b = SavingsAccount()
while(1):
    print("=============================================")
    print("1.Log Into Another Account\n2.Withdraw\n3.Deposit\n4.View Current Balance\n5.Apply Fees\n6.Minimum Balance\n7.Apply Interest Rate\n8.Log Off")
    ch = float(input("Enter the choice:"))
    if(ch==1):
        b.__init__()
    elif(ch==2):
        b.withdrawl()
    elif(ch==3):
        b.deposit()
    elif(ch==4):
        b.get_bal()
    elif(ch==5):
        b.deduct_fee()
    elif(ch==6):
        b.mini_bal()
    elif(ch==7):
        b.addInterest()
    elif(ch==0):
        exit(0)
    else:
        print("ERROR")
    print("=============================================")
