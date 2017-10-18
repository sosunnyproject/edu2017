#coding=utf-8
#python2

class Account:

    #attributes
    number = '000-000-0000'
    balance = 0
    rate = 1.0
    num_acc = 0

    #methods
    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        self.balance -= money

    def obtain_interest(self):
        self.balance += self.balance*(self.rate/100)

    def get_balance (self):
        return self.balance

    def set_balance(self, amnt):
        self.balance = amnt

    #default constructor - 인스턴스 생성 시 자동으로 호출되는 특수 메소드.
    def __init__(self, num='000-000-0000', amnt=0, rate=1.0):
        self.number = num
        self.balance = amnt
        self.rate = rate
        Account.num_acc += 1 #Account의 클래스 변수 값 변경

class MinBalanceAccount(Account):
    def __init__(self, min_balance, num='000-000-0000', amnt = 0, rate = 1.0):
        Account.__init__(self, num = num, amnt = amnt, rate = rate)
        self.minimum_balance = min_balance
        self.bonus_rate = 1.0

    def withdraw(self, amnt):
        if self.balance - amnt < self.minimum_balance:
            print('sorry, minimum balance must be maintained')
        else:
            Account.withdraw(self, amnt)

    def obtain_interest(self):
        self.balance += (self.balance)*((self.rate + self.bonus_rate)/100.0)

    def __add__(self, another):
        new = MinBalanceAccount(min_balance=0)
        new.balance = self.balance + another.balance
        #self.balance += another.balance
        #if no new, and just self += another, self value changes
        return new

    def transfer(self, another, amnt):
        self.balance = self.balance - amnt
        another.balance = another.balance + amnt


acc1 = Account()
acc2 = Account()
acc3 = Account()

acc1.deposit(100)
acc2.deposit(10000)

print(acc1.balance)
print(acc2.balance)
print(acc3.balance)
print(Account.num_acc)
print(acc1.num_acc)

minacc1 = MinBalanceAccount(min_balance=0)
minacc1.set_balance(500)
minacc2 = MinBalanceAccount(min_balance = 0)
minacc2.set_balance(1000)

minacc3 = minacc1 + minacc2
print("added:", minacc3.get_balance())

minacc1.transfer(minacc2, 100)
print(minacc1.get_balance())
print(minacc2.get_balance())

