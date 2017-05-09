class Account():
  def balance():
    pass
  
  def balance():
    pass
  
class SavingsAccount(Account):
  def __init__(self):
    self.deposit = 1000
    
  
  def balance(self,balance):
    if type(balance) == int and balance !="":
      if balance >= 0:
        self.deposit += balance
        return self.deposit

      else:
        return 'Invalid Amount'

    else:
      raise ValueError()

  def withdraw(self,amount):
    if type(amount) == int and amount != "":
      if amount > 0:
        if (self.balance-amount) > 0:
          if (self.balance -amount) > 1000:
            self.balance-=amount
            return self.balance
          else:
            return 'Insufficient funds in Account'
        else:
          return 'Enter Amount below Actual balance'
      else:
        return 'Invalid Amount'
    else:
      raise ValueError()
      
class CurrentAccount(Account):
  def __init__(self):
    self.balance = 0
    
  
  def deposit(self,deposit):
    if type(deposit) == int and deposit !="":
      if deposit >= 0:
        self.balance += deposit
        return self.balance

      else:
        return 'Invalid deposit amount'

    else:
      raise ValueError()

  def withdraw(self,amount):
    if type(amount) ==  int and amount != "":
      if amount > 0:
        if (self.balance-amount) > 0:

          self.balance-=amount
          return self.balance

        else:
          return 'Enter Amount below Actual balance'
      else:
        return 'Invalid withdraw amount'
    else:
      raise ValueError()