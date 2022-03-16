no_of_unit = 24
no_of_unit1 = 'hour'

def no_of_day_unit_calculation(num_of_days):
	return f"number of days in {num_of_days} are {num_of_days * no_of_unit} {no_of_unit1}"
	
def validate_and_execute():
	if User_Input.isdigit():
	   int_User_Input = (int(User_Input)
	   if int_User_Input > 0:
				result = no_of_day_unit_calculation(int_User_Input)
				print (result)
			elif int_User_Input == 0:
				:print ("you have enter zero, please enter a positive number")
	
	else:
		print ("your input in wrong, Dont ruin my program")

while True:
User_Input = input("Hey User, Please enter a no to be calculated\n")
validate_and_execute()
