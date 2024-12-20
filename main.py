import requests

class Attendance:
    def __init__(self, secure_id):
        self.secure_id = secure_id
        self.criteria = 0.75 # 75 percent
    
    def fetch(self):
        cookies = {
            '_Secure-SID': self.secure_id,
        }
        response = requests.post('https://mserp.kiet.edu/StudeHome.aspx/ShowAttendance', cookies=cookies, json={})
        return response.json().get('d').get('AttendList')
    
    def calculate(self, data):
        for i in data:
            attended = int(i.get('Attendance').split("/")[0])
            total = int(i.get('Attendance').split("/")[1])

            print(f"You can bunk {self.calculate_max_leaves(attended, total)} classes in {i['CourseName']}")

    def calculate_max_leaves(self,attended, total):
        if attended / total < self.criteria:
            return 0
        max_leaves = (attended - self.criteria * total) / self.criteria
        max_leaves = int(max_leaves)
        return max_leaves


if __name__ == "__main__":

    print("\tBunk Calculator\n")

    # For Secure ID - see readme.MD

    secure_id = input("Enter the secure ID from MSERP: ")

    c = Attendance(secure_id)

    data = c.fetch()

    c.calculate(data)

    input("\n\nPlease enter any key to exit...")