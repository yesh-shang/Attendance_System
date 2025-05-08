import csv
import os
from datetime import datetime

# Predefined student list
students = [
    {"Student ID": "USTP2023-001", "Name": "Aira Monique Precillas"},
    {"Student ID": "USTP2023-002", "Name": "Gretsin Indus"},
    {"Student ID": "USTP2023-003", "Name": "Erich E. Poliran"},
    {"Student ID": "USTP2023-004", "Name": "Ralph Allen B. Calib"},
    {"Student ID": "USTP2023-005", "Name": "Anjen U. Penalte"},
    {"Student ID": "USTP2023-006", "Name": "Yesha Mae Amores"}
]

ATTENDANCE_FILE = "attendance.csv"

# Ensure the CSV file exists and has headers
def initialize_file():
    if not os.path.exists(ATTENDANCE_FILE):
        with open(ATTENDANCE_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Student ID", "Name", "Status"])

def mark_attendance():
    date = input("📅 Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')

    print(f"\n📋 Taking attendance for {date}\n")
    attendance_records = []

    for student in students:
        while True:
            status = input(f"{student['Name']} ({student['Student ID']}) - Present (P) / Absent (A): ").strip().upper()
            if status in ['P', 'A']:
                attendance_records.append([
                    date,
                    student["Student ID"],
                    student["Name"],
                    "Present" if status == 'P' else "Absent"
                ])
                break
            else:
                print("❌ Invalid input. Enter 'P' or 'A'.")

    with open(ATTENDANCE_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(attendance_records)

    print("\n✅ Attendance recorded successfully!\n")

def view_attendance():
    if not os.path.exists(ATTENDANCE_FILE):
        print("⚠️ No attendance records found.\n")
        return

    print("\n📊 Attendance Records:\n")
    with open(ATTENDANCE_FILE, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(", ".join(row))
    print()

def main():
    initialize_file()
    while True:
        print("==== USTP Manual Attendance System ====")
        print("1. Mark Attendance")
        print("2. View Attendance Records")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == '1':
            mark_attendance()
        elif choice == '2':
            view_attendance()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
