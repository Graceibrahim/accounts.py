from datetime import datetime

class Account:
		
	def __init__(self,first_name,last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.balance = 0
		self.deposits=[]
		self.withdrawals=[]
		self.loan=0


	def welcome(self):
		return "Hey {} {} your account balance is {}".format(self.first_name,self.last_name,self.balance)


	def deposit(self,amount):
		time=datetime.now()
		object={"time":time,"amount":amount}
		self.deposits.append(object)
		deposit = amount
		self.balance = self.balance + amount
		
		
		deposit = "Dear {} {} your deposit of ksh {} was successful ".format(self.first_name,self.last_name,amount,self.balance)
		return deposit

	

	def withdraw(self,amount):
		time=datetime.now()
		object={"time":time,"amount":amount}
		self.withdrawals.append(object)  
		withdraw = amount
		if amount>self.balance:
			return "can't withdraw"
		else:
			self.balance = self.balance - amount
			text = "Dear {} {} withdrawal of ksh {} was successful ".format(self.first_name,self.last_name,amount,self.balance)
		return text

	def show_deposits(self):
		for deposit in self.deposits:
			time=deposit["time"]
			formated_time=time.strftime("%c")
			amount=deposit["amount"]
			print("On{} you deposited {}".format(formated_time,amount))


	def show_withdrawals(self):
		for withdrawal in self.withdrawals:
			time=withdrawal["time"]
			formated_time=time.strftime("%c")
			amount=withdrawal["amount"]
			print("On {} you withdrew {}".format(formated_time,amount))


	def show_balance(self):
		show_balance = self.balance
		text = "Dear {} {} your current balance is {}".format(self.first_name,self.last_name,self.balance)
		return text

	def give_loans(self,amount):
		total=0
		for deposit in self.deposits:
			amount=deposit["amount"]
			total+=amount
		if len (self.deposits)>=5 and amount<total/3 and self.loan==0:
			self.loan=self.loan+amount
			print("Hello {},the loan of {} is successful ".format(self.first_name,amount))
		else:
			print("Hello {},the loan limit is unsuccessful".format(self.name))
 
	def pay_loan(self,amount):
		if self.loan==0:
			print("You do not have an existing loan ")
		elif amount<self.loan:
			self.loan=self.loan-amount
			print("Hello {} you have cleared part of your loan,{}. /n your remaining loan balance is {}".format(self.first_name,amount,self.loan))
		elif amount ==self.loan:
			self.loan=self.loan-amount
			print("Your loan has been fully repaid")
		elif amount>self.loan:
			excess=amount-self.loan
			self.balance=excess+self.balance
			self.loan=amount-self.loan-excess
			print("Hello {} you have paid in excess of your loan. Your excess amount has been deposited in your account and you new balance is {}".format(self.first_name,self.balance))
