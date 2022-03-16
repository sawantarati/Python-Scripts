import datetime
user_input = input("Please enter your goal and deadline seperated by colon\n")
user_input_list = user_input.split(":")
goal = user_input_list[0]
deadline = user_input_list[1]
print (user_input_list)

deadline_to_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")

today_date = datetime.datetime.today()

no_of_days_to_deadline = deadline_to_date - today_date

print(f"Dear studer no of day remaining to your {goal}  deadline is {no_of_days_to_deadline} hours")
