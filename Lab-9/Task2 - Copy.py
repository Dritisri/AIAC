class SRUStudent:
    def __init__(self, name, roll_no, hostel_status):
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fee_paid = False
    def fee_update(self, fee_status):
        self.fee_paid = fee_status
        if fee_status:
            print(f"Fee payment confirmed for {self.name}")
        else:
            print(f"Fee payment pending for {self.name}")
    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Roll Number: {self.roll_no}")
        print(f"Hostel Status: {self.hostel_status}")
        print(f"Fee Status: {'Paid' if self.fee_paid else 'Pending'}")
        print("-" * 30)
def get_student_input():
    print("Enter Student Details:")
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    hostel_status = input("Enter hostel status (Yes/No): ")
    student = SRUStudent(name, roll_no, hostel_status)
    fee_input = input("Is fee paid? (y/n): ").lower()
    fee_paid = fee_input in ['y', 'yes']
    student.fee_update(fee_paid)
    return student
if __name__ == "__main__":
    student = get_student_input()
    print("\nStudent Information:")
    student.display_details()
    update_fee = input("\nDo you want to update fee status? (y/n): ").lower()
    if update_fee in ['y', 'yes']:
        new_fee_status = input("Is fee paid now? (y/n): ").lower()
        student.fee_update(new_fee_status in ['y', 'yes'])
        print("\nUpdated Student Information:")
        student.display_details()

