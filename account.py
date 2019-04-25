    
class Account:
	def __init__(self,first_name,last_name,balance):
		self.first_name = first_name
		self.last_name = last_name
		self.balance = balance

	def welcome(self):
		return "Hello {} {} your account balance is {}".format(self.first_name,self.last_name,self.balance)


	def deposit(self, h):
		deposit = h
		self.balance = self.balance + h

		Text = "Dear {} {} deposit of kes {} was successful current balance is {}".format(self.first_name,self.last_name,h,self.balance)
		return text
		

	def withdraw(self, m):
		withdraw = m
		if m>self.balance:
			return "Sorry insufficient balance to process your request"
		else:
			self.balance = self.balance - m
			message = "Dear {} {} withdrawal of Ksh {} was successful, current balance is {}".format(self.first_name,self.last_name,m,self.balance)
			return message

	def show_balance(self):
		show_balance = self.balance
		text = "Dear {} {} your current balance is {}".format(self.first_name,self.last_name,self.balance)
		return text