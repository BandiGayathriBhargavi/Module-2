import json #It saves student records as text
import csv #For CSV files
import os #If the file is in downloads, to access it
class StudentManagementSystem:
    def __init__(self, filename="students", storage_type="json"):
        self.storage_type = storage_type.lower() #It makes your code case-insensitive
        if self.storage_type == "csv":
            self.filename = f"{filename}.csv" #To store the data in CSV format
            self.fields = ["roll_no", "name", "age", "grade"]
        else:
            self.filename = f"{filename}.json"
            self.storage_type = "json" #Works same as above, but for JSON format
            self.students = {}  # In-memory dictionary database: {roll_no: {details}}
        self.load_data() # For saving purposes
    def load_data(self): # self to access variables
        if not os.path.exists(self.filename):
            self.students = {}
            return
        try:
            if self.storage_type == "json": # If the file is JSON
                with open(self.filename, 'r') as f:
                    self.students = json.load(f)
            elif self.storage_type == "csv": # If the file is CSV
                with open(self.filename, 'r', newline='') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        self.students[row["roll_no"]] = {
                            "name": row["name"],
                            "age": int(row["age"]),
                            "grade": row["grade"]
                        }
        except (json.JSONDecodeError, KeyError, ValueError):
            print(f"[Warning] Error reading {self.filename}. Starting with empty data.") # If there are no records
            self.students = {}
    def save_data(self):
        try:
            if self.storage_type == "json":
                with open(self.filename, 'w') as f:
                    json.dump(self.students, f, indent=4) # To save the data in JSON format Why only indent=4 (Clean, structured, and easy to read)
            elif self.storage_type == "csv":
                with open(self.filename, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=self.fields) # DictWriter is to write data into a CSV (Comma-Separated Values) file
                    writer.writeheader() # Ensures the CSV file has clear column headers at the very top
                    for roll_no, info in self.students.items(): #Loops through every single student in the dictionary
                        writer.writerow({ # Method that takes a piece of data and writes it as a single, new row
                            "roll_no": roll_no,
                            "name": info["name"],
                            "age": info["age"],
                            "grade": info["grade"]
                        })
        except IOError as e:
            print(f"[Error] Failed to write data to storage file: {e}")
    def create_student(self, roll_no, name, age, grade): # Create a new student record
        if roll_no in self.students: # For already existed students
            print(f"\n[Error] Student with Roll Number {roll_no} already exists.")
            return False
        self.students[roll_no] = { # For new roll numbers, it will create a new record
            "name": name,
            "age": int(age),
            "grade": grade.upper() # For grads only in uppercase letters
        }
        self.save_data() # For saving the data in the file
        print(f"\n[Success] Student '{name}' added successfully!")
        return True
    def update_student(self, roll_no, name=None, age=None, grade=None): # UPDATE: Modifies an existing student record
            if roll_no not in self.students:
                print(f"\n[Error] Student with Roll Number {roll_no} not found.") # If the roll number is not found, it will display an error message
                return False
            if name:
                self.students[roll_no]["name"] = name
            if age:
                self.students[roll_no]["age"] = int(age)
            if grade:
                self.students[roll_no]["grade"] = grade.upper() # allows you to update only the fields you want to change while leaving the other fields 
                                                                # exactly as they were.If you press Enter without typing anything for a field, that field is 
                                                                # skipped and stays unchanged.
            self.save_data()
            print(f"\n[Success] Record for Roll Number {roll_no} updated successfully!")
            return True
    def read_all_students(self): # For displaying all the records in a table format
        if not self.students: # Empty dictionary, meaning no records
            print("\n[Info] No student records found.")
            return
        print("\n" + "="*50)
        print(f"{'ROLL NO':<12} {'NAME':<20} {'AGE':<8} {'GRADE':<5}")
        print("="*50)
        for roll_no, info in self.students.items():
            print(f"{roll_no:<12} {info['name']:<20} {info['age']:<8} {info['grade']:<5}")
        print("="*50)
        # prints student records on the screen in a clean, perfectly aligned table format—just like a spreadsheet.
        return True
    def delete_student(self, roll_no): # DELETE: Removes a student record completely.
        if roll_no in self.students:
            deleted_student = self.students.pop(roll_no) # Here pop is used to remove the student record
            # Here pop function is used to delete then why not push function was not used to create new records?
            # pop() is a standard dictionary tool in Python, but Python dictionaries do not have a function named push(). 
            self.save_data()
            print(f"\n[Success] Student '{deleted_student['name']}' removed from records.")
            return True
        else:
            print(f"\n[Error] Student with Roll Number {roll_no} not found.") # If the roll number is not found, it will display an error message
            return False
def main():
    print("--- Student Record Management System ---")
    storage_choice = input("Select storage engine (1 for JSON, 2 for CSV) [Default: JSON]: ").strip() # Any blank spaces from the beginning and the very end of 
                                                                                                      # a user's input
    storage_type = "csv" if storage_choice == "2" else "json"
    sms = StudentManagementSystem(storage_type=storage_type)
    print(f"\n[System Loaded] Storage backend active: {storage_type.upper()} format.\n")
    # Initialize core backend engine and print a confirmation message in the terminal. They tell you exactly which database file format is currently running.
    while True:
        print("\n===== MENU =====")
        print("1. Register New Student (Create)")
        print("2. Modify Student Record (Update)")
        print("3. Display All Records (Read)")
        # print("3. Search Student by Roll No (Read)")
        print("4. Remove Student Record (Delete)")
        print("5. Exit Application")
        choice = int(input("Select an option (1-5): ").strip())
        if choice == 1:
            print("\n--- Add Student Record ---")
            roll = input("Enter Roll Number: ").strip()
            if not roll:
                print("[Error] Roll number cannot be empty.")
                continue
            name = input("Enter Full Name: ").strip()
            try:
                age = int(input("Enter Age: ").strip())
            except ValueError:
                print("[Error] Age must be an integer.")
                continue
            grade = input("Enter Grade (e.g., A, B, C): ").strip()
            sms.create_student(roll, name, age, grade)
        elif choice == 2:
            print("\n--- Update Student Record ---")
            roll = input("Enter Roll Number: ").strip()
            if roll in sms.students:
                print("(Press Enter directly without typing to keep the current value unchanged)")
                name = input(f"New Name [{sms.students[roll]['name']}]: ").strip() # [{sms.students[roll]['name']}] for displaying the current value of the name 
                                                                                   # field for the student.
                age_input = input(f"New Age [{sms.students[roll]['age']}]: ").strip()
                grade = input(f"New Grade [{sms.students[roll]['grade']}]: ").strip()
                age = int(age_input) if age_input.isdigit() else None # If the user enters a valid integer for age, it will be converted to an integer; otherwise, 
                                                                      # it will be set to None
                sms.update_student(roll, name=name or None, age=age, grade=grade or None) # Why only for name and grade None which are words other are number?
                # A Text field becomes an empty string: ""
                # A Number field cannot be an empty string, because you cannot do math with "". 
                # Python will crash if it tries to treat text spaces as a number.
                # Why can't we update roll number itself only we can update name, age, grade?
                # Roll Number acts as the Primary Key. Allowing a user to change a Roll Number introduces significant risks that can corrupt the database.
            else:
                print(f"[Error] Roll Number {roll} not found.") # If the roll number is not found, it will display an error message
        elif choice == 3:
                    sms.read_all_students()
        elif choice == 4:
            print("\n--- Delete Student Record ---")
            roll = input("Enter Roll Number: ").strip()
            confirm = input(f"Are you sure you want to delete {roll}? (y/n): ").strip().lower() # Double confirmation protection
            if confirm == 'y':
                sms.delete_student(roll)
            else:
                print("[Cancelled] Deletion canceled.")
        elif choice == 5:
            print("\nThank you for using Student Record Management System")
            break
        else:
            print("\n[Invalid Selection] Please choose a digit from 1 to 5.")
if __name__ == "__main__":
    main()
