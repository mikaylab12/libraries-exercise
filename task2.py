# task 2 from handout
# user input for name and surname
name = input("Enter name and surname: ")
# user inputs for marks
mark1 = int(input("Please enter your first mark: "))
mark2 = int(input("Please enter your second mark: "))
mark3 = int(input("Please enter your third mark: "))
average = (mark1+mark2+mark3)//3
if average > 50:
    print("Congratulations,", name, "your mark is", average, "%\nYou have passed!" )
elif average < 50:
    print("Unfortunately,", name, "your mark is", average, "%\nYou have failed.")

# second function - calculate ten dates , 2 weeks apart from current date
from datetime import datetime, timedelta
# today's time
dt = datetime.today()
print(dt.strftime("%Y-%m-%d"))
# to receive ten dates each 2 weeks part
for i in range(1, 10):
    add_dt = dt + timedelta(days=14)
    dt = add_dt
    print(add_dt.strftime("%Y-%m-%d"))