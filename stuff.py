print "Welcome to USAA"
print "Please Enter Your User Name and Password."
Username = raw_input("Username >")
Password = raw_input("Password >")

if Password == "Tree" and Username == "Green":
	print "Welcome to your USAA account Charles"
else:
	print "Password  or Username does not match our records, try again."
	
print "Which account would you like to access?"
print "1. Checkings"
print "2. Saving"
print "3. Credit Cards"

account = raw_input("Account")

if account == "1":
	print "You checkings account holds $23,000"
elif account == "2":
	print "You Savings account holds $53,000"
else:
	print "You credit card has a -$900 balance"
	
print "Do you wish to log out?"
log_out = raw_input("> ")

if log_out == "yes":
	print "GoodBye!"
else:
	print "Continue"