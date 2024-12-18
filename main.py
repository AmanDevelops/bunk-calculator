from utils import Attendance

print("         Bunk Calculator\n")


# For Secure ID - see readme.MD

secure_id = input("Enter the secure ID from MSERP: ")

c = Attendance(secure_id)

data = c.fetch()

c.calculate(data)