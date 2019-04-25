    
class Account:
	def __init__(self, first_name, second_name,initial_balance):
		self.first_name=first_name
		self.second_name=second_name
		self.initial_balance=initial_balance
		
	
	def	greetings(self):
		greetings="Hello {} {} welcome to your Jamii bank. Your account balance is KSH {}".format(self.first_name,self.second_name,self.initial_balance) 
		return greetings

	
	def deposit(self):
		amount=float(input("Enter amount you want to deposit"))	
		self.initial_balance +=amount
		print("\n Amount deposited:",amount)

	
	def withdraw(self):
		amount =float(input("Key in amount to withdraw: " ))
		if self.initial_balance>=amount:
			self.initial_balance-=amount
			print("\n You withdrawed:", amount)

		else:
			print("\n Sorry, Insufficient balance")
	

	def balance(self):
		print("\n Available balance=",self.initial_balance)
