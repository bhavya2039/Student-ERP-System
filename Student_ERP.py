class StudentInformation:
    """
    Base class holding student personal/academic-record data
    and basic CRUD-style operations (add, view, search, delete, update).
    """

    def __init__(
        self,
        university_name,
        college_name,
        student_name,
        father_name,
        roll_number,
        course,
        course_duration,
        year_of_admission,
        current_year,
        month
    ):
        self.university_name = university_name
        self.college_name = college_name
        self.student_name = student_name
        self.father_name = father_name
        self.roll_number = roll_number
        self.course = course
        self.course_duration = course_duration
        self.year_of_admission = year_of_admission
        self.current_year = current_year
        self.month = month

        self.end_duration = self.year_of_admission + self.course_duration
        self.current_course_year = self.current_year - self.year_of_admission

        if self.month < 7:
            self.current_sem = (2 * self.current_course_year) - 1
        else:
            self.current_sem = 2 * self.current_course_year

    # ---------------------------------------
    # Display One Student
    # ---------------------------------------
    def add_students(self):
        print("\n========== STUDENT INFORMATION ==========")
        print(f"University Name : {self.university_name}")
        print(f"College Name    : {self.college_name}")
        print(f"Student Name    : {self.student_name}")
        print(f"Father Name     : {self.father_name}")
        print(f"Roll Number     : {self.roll_number}")
        print(f"Course          : {self.course}")
        print(f"Course Duration : {self.course_duration} Years")
        print(f"Admission Year  : {self.year_of_admission}")
        print(f"Course End Year : {self.end_duration}")
        print(f"Current Year    : {self.current_course_year}")
        print(f"Current Semester: {self.current_sem}")
        print("=========================================")

    # ---------------------------------------
    # View All Students
    # ---------------------------------------
    def view_all_students(self, students_list):
        print("\n============= ALL STUDENTS =============")

        if len(students_list) == 0:
            print("No students available.")
            return

        for student in students_list:
            student.add_students()

    # ---------------------------------------
    # Search Student
    # ---------------------------------------
    def search_any_student(self, students_list, searched_rollno):
        found = False

        for student in students_list:
            if searched_rollno == student.roll_number:
                student.add_students()
                found = True
                break

        if found == False:
            print(f"\nRoll Number {searched_rollno} not found.")

    # ---------------------------------------
    # Delete Student
    # ---------------------------------------
    def delete_any_student(self, students_list, searched_rollno, deleted_student_list):
        found = False

        for student in students_list:
            if searched_rollno == student.roll_number:
                students_list.remove(student)
                deleted_student_list.append(student)
                print("\nStudent Deleted Successfully!")
                found = True
                break

        if found == False:
            print(f"\nRoll Number {searched_rollno} not found.")

    # ---------------------------------------
    # View Deleted Students
    # ---------------------------------------
    def view_deleted_students(self, deleted_student_list):
        print("\n========== DELETED STUDENTS ==========")

        if len(deleted_student_list) == 0:
            print("No deleted students available.")
            return

        for student in deleted_student_list:
            student.add_students()

    # ---------------------------------------
    # Update Student Data
    # ---------------------------------------
    def update_student(self, students_list, searched_rollno):
        found = False
        for student in students_list:
            if searched_rollno == student.roll_number:
                student.university_name = input("Enter University Name: ")
                student.college_name = input("Enter College Name: ")
                student.student_name = input("Enter Student Name: ")
                student.father_name = input("Enter Father Name: ")
                student.roll_number = input("Enter Roll Number: ")
                student.course = input("Enter Course Name: ")
                student.course_duration = int(input("Enter Course Duration (Years): "))
                student.year_of_admission = int(input("Enter Admission Year: "))
                student.current_year = int(input("Enter Current Year: "))
                student.month = int(input("Enter Current Month (1-12): "))
                print("\nStudent Updated Successfully!")
                student.add_students()
                found = True
                break

        if found == False:
            print("Student Not Found.")


class Academics(StudentInformation):
    """
    Adds marks-related operations: add/update/view marks,
    totals, percentage, average, topper/lowest.
    """

    # ---------------------------------------
    # Add Marks
    # ---------------------------------------
    def add_marks(self, searched_rollno, students_list, dict1):
        found = False
        for student in students_list:
            if searched_rollno == student.roll_number:
                found = True
                if searched_rollno not in dict1:
                    dict1[searched_rollno] = {}
                num = int(input("Enter the number of suject: "))
                for i in range(1, num + 1):
                    subject_name = input(f"Enter Subject {i} Name: ")
                    subject_mark = int(input(f"Enter Marks for {subject_name}: "))
                    dict1[searched_rollno][subject_name] = subject_mark
                student.add_students()
                print("MARKS\n")
                print(dict1[searched_rollno])
                break
        if found == False:
            print("No Student Available")

    # ---------------------------------------
    # Update Marks
    # ---------------------------------------
    def update_marks(self, searched_rollno, students_list, dict1):
        found = False
        for student in students_list:
            if searched_rollno == student.roll_number:
                found = True
                if searched_rollno not in dict1 or len(dict1[searched_rollno]) == 0:
                    print("No marks exist yet for this student. Use Add Marks first.")
                    break
                print(f"Existing subjects: {list(dict1[searched_rollno].keys())}")
                subject = input("Enter Subject Name to update: ")
                mark = int(input(f"Enter new marks for {subject}: "))
                dict1[searched_rollno][subject] = mark
                print("\nMarks Updated Successfully!")
                student.add_students()
                break
        if found == False:
            print("No Student Available")

    # ---------------------------------------
    # View Marks
    # ---------------------------------------
    def view_marks(self, searched_rollno, dict1):
        if searched_rollno not in dict1 or len(dict1[searched_rollno]) == 0:
            print("No marks entered yet.")
            return
        print(f"\n========== MARKS (Roll No: {searched_rollno}) ==========")
        for subject, mark in dict1[searched_rollno].items():
            print(f"{subject:<20}: {mark}")
        print("=================================================")

    # ---------------------------------------
    # Total / Percentage / Average
    # ---------------------------------------
    def calculate_total(self, searched_rollno, dict1):
        marks = dict1.get(searched_rollno, {})
        print(f"Total Marks for {searched_rollno}: {sum(marks.values())}")

    def calculate_percentage(self, searched_rollno, dict1):
        marks = dict1.get(searched_rollno, {})
        if len(marks) == 0:
            print(f"Percentage for {searched_rollno}: 0.00%")
            return
        pct = (sum(marks.values()) / (len(marks) * 100)) * 100
        print(f"Percentage for {searched_rollno}: {pct:.2f}%")

    def calculate_average_marks(self, searched_rollno, dict1):
        marks = dict1.get(searched_rollno, {})
        if len(marks) == 0:
            print(f"Average Marks for {searched_rollno}: 0")
            return
        avg = sum(marks.values()) / len(marks)
        print(f"Average Marks for {searched_rollno}: {avg:.2f}")

    # ---------------------------------------
    # Topper / Lowest
    # ---------------------------------------
    def find_topper(self, students_list, dict1):
        eligible = [s for s in students_list if dict1.get(s.roll_number)]
        if len(eligible) == 0:
            print("No students with marks available.")
            return

        def pct(s):
            marks = dict1[s.roll_number]
            return (sum(marks.values()) / (len(marks) * 100)) * 100

        topper = max(eligible, key=lambda s: pct(s))
        print(f"\nTopper: {topper.student_name} (Roll {topper.roll_number}) - {pct(topper):.2f}%")

    def find_lowest(self, students_list, dict1):
        eligible = [s for s in students_list if dict1.get(s.roll_number)]
        if len(eligible) == 0:
            print("No students with marks available.")
            return

        def pct(s):
            marks = dict1[s.roll_number]
            return (sum(marks.values()) / (len(marks) * 100)) * 100

        lowest = min(eligible, key=lambda s: pct(s))
        print(f"\nLowest: {lowest.student_name} (Roll {lowest.roll_number}) - {pct(lowest):.2f}%")


class Course(Academics):
    """
    Adds course/semester assignment and course/semester filtered views.
    """

    def assign_course(self, students_list, searched_rollno):
        found = False
        for student in students_list:
            if searched_rollno == student.roll_number:
                found = True
                student.course = input("Enter Course Name: ")
                print("Course Assigned Successfully!")
                break
        if found == False:
            print("Student Not Found.")

    def update_course(self, students_list, searched_rollno):
        # Same action as assign_course - kept separate to match the
        # original menu options, but there is no distinct behavior.
        self.assign_course(students_list, searched_rollno)

    def assign_semester(self, students_list, searched_rollno):
        found = False
        for student in students_list:
            if searched_rollno == student.roll_number:
                found = True
                new_sem = int(input("Enter Semester Number: "))
                print(f"Note: overriding auto-calculated semester ({student.current_sem} -> {new_sem}).")
                student.current_sem = new_sem
                print("Semester Assigned Successfully!")
                break
        if found == False:
            print("Student Not Found.")

    def view_students_by_course(self, students_list, course_name):
        print(f"\n===== Students in Course: {course_name} =====")
        found = False
        for student in students_list:
            if student.course.lower() == course_name.lower():
                student.add_students()
                found = True
        if found == False:
            print("No students found in this course.")

    def view_students_by_semester(self, students_list, sem_number):
        print(f"\n===== Students in Semester: {sem_number} =====")
        found = False
        for student in students_list:
            if student.current_sem == sem_number:
                student.add_students()
                found = True
        if found == False:
            print("No students found in this semester.")


class Statistics(Course):
    """
    Adds aggregate counting operations.
    """

    def count_total_students(self, students_list):
        print(f"Total Students: {len(students_list)}")

    def count_students_by_course(self, students_list):
        counts = {}
        for student in students_list:
            counts[student.course] = counts.get(student.course, 0) + 1
        print("\n===== Students per Course =====")
        if len(counts) == 0:
            print("No students available.")
            return
        for course, count in counts.items():
            print(f"{course:<20}: {count}")

    def count_students_by_semester(self, students_list):
        counts = {}
        for student in students_list:
            counts[student.current_sem] = counts.get(student.current_sem, 0) + 1
        print("\n===== Students per Semester =====")
        if len(counts) == 0:
            print("No students available.")
            return
        for sem, count in sorted(counts.items()):
            print(f"Semester {sem:<10}: {count}")


class Sorting(Statistics):
    """
    Adds lambda-based sorting operations.
    """

    def sort_by_name(self, students_list):
        sorted_list = sorted(students_list, key=lambda s: s.student_name.lower())
        for student in sorted_list:
            print(f"{student.student_name} (Roll {student.roll_number})")

    def sort_by_marks(self, students_list, dict1):
        sorted_list = sorted(
            students_list,
            key=lambda s: sum(dict1.get(s.roll_number, {}).values()),
            reverse=True
        )
        for student in sorted_list:
            total = sum(dict1.get(student.roll_number, {}).values())
            print(f"{student.student_name} (Roll {student.roll_number}) - Total: {total}")

    def sort_by_percentage(self, students_list, dict1):
        def percentage(s):
            marks = dict1.get(s.roll_number, {})
            if len(marks) == 0:
                return 0
            return (sum(marks.values()) / (len(marks) * 100)) * 100

        sorted_list = sorted(students_list, key=lambda s: percentage(s), reverse=True)
        for student in sorted_list:
            print(f"{student.student_name} (Roll {student.roll_number}) - {percentage(student):.2f}%")


class Searching(Sorting):
    """
    Adds search-by-id/name/course operations.
    """

    def search_by_id(self, students_list, searched_rollno):
        self.search_any_student(students_list, searched_rollno)

    def search_by_name(self, students_list, searched_name):
        found = False
        for student in students_list:
            if searched_name.lower() in student.student_name.lower():
                student.add_students()
                found = True
        if found == False:
            print(f"No students found matching name '{searched_name}'.")

    def search_by_course(self, students_list, course_name):
        self.view_students_by_course(students_list, course_name)


class Display(Searching):
    """
    Adds higher-level display/reporting operations (details, top 3, failed).
    This is the final class in the chain and combines every capability
    from StudentInformation, Academics, Course, Statistics, Sorting and
    Searching.
    """

    def display_student_details(self, students_list, searched_rollno):
        self.search_any_student(students_list, searched_rollno)

    def display_top3(self, students_list, dict1):
        def percentage(s):
            marks = dict1.get(s.roll_number, {})
            if len(marks) == 0:
                return 0
            return (sum(marks.values()) / (len(marks) * 100)) * 100

        eligible = [s for s in students_list if dict1.get(s.roll_number)]
        if len(eligible) == 0:
            print("No students with marks available.")
            return

        top3 = sorted(eligible, key=lambda s: percentage(s), reverse=True)[:3]
        print("\n========== TOP 3 STUDENTS ==========")
        rank = 1
        for student in top3:
            print(f"{rank}. {student.student_name} (Roll {student.roll_number}) - {percentage(student):.2f}%")
            rank += 1

    def display_failed_students(self, students_list, dict1, passing_mark):
        print(f"\n========== FAILED STUDENTS (below {passing_mark}%) ==========")
        found = False
        for student in students_list:
            marks = dict1.get(student.roll_number, {})
            if len(marks) == 0:
                continue
            pct = (sum(marks.values()) / (len(marks) * 100)) * 100
            if pct < passing_mark:
                print(f"{student.student_name} (Roll {student.roll_number}) - {pct:.2f}%")
                found = True
        if found == False:
            print("No failed students.")


# ---------------------------------------
# List to Store Student Objects
# ---------------------------------------
students_list = []
deleted_student_list = []
dict1 = {}

# ---------------------------------------
# Single "app" object: since Display inherits from every other
# class, one object gives access to all functionality
# (info, academics, course, statistics, sorting, searching, display).
# ---------------------------------------
app = Display("", "", "", "", "", "", 0, 0, 0, 1)

# ---------------------------------------
# Menu Loop
# ---------------------------------------
while True:

    print("\n================ MENU ================")
    print(" 1. Add Student")
    print(" 2. View All Students")
    print(" 3. Search Student")
    print(" 4. Delete Student")
    print(" 5. View Deleted Students")
    print("\n--- Academic ---")
    print(" 6. Add Marks")
    print(" 7. Update Marks")
    print(" 8. View Marks")
    print(" 9. Calculate Total Marks")
    print("10. Calculate Percentage")
    print("11. Find Topper")
    print("12. Find Lowest Marks")
    print("13. Calculate Average Marks")
    print("\n--- Course ---")
    print("14. Assign Course")
    print("15. Update Course")
    print("16. Assign Semester")
    print("17. View Students by Course")
    print("18. View Students by Semester")
    print("\n--- Statistics ---")
    print("19. Count Total Students")
    print("20. Count Students in Each Course")
    print("21. Count Students in Each Semester")
    print("\n--- Sorting ---")
    print("22. Sort by Name")
    print("23. Sort by Marks")
    print("24. Sort by Percentage")
    print("\n--- Searching ---")
    print("25. Search by ID")
    print("26. Search by Name")
    print("27. Search by Course")
    print("\n--- Display ---")
    print("28. Display Student Details")
    print("29. Display Top 3 Students")
    print("30. Display Failed Students")
    print("\n31. Update Student")
    print("32. Exit")
    print("=======================================")

    choice = input("Enter your choice (1-32): ")

    # ---------------- Add Student ----------------
    if choice == "1":
        university_name = input("Enter University Name: ")
        college_name = input("Enter College Name: ")
        student_name = input("Enter Student Name: ")
        father_name = input("Enter Father Name: ")
        roll_number = input("Enter Roll Number: ")
        course = input("Enter Course Name: ")
        course_duration = int(input("Enter Course Duration (Years): "))
        year_of_admission = int(input("Enter Admission Year: "))
        current_year = int(input("Enter Current Year: "))
        month = int(input("Enter Current Month (1-12): "))

        new_student = Display(
            university_name,
            college_name,
            student_name,
            father_name,
            roll_number,
            course,
            course_duration,
            year_of_admission,
            current_year,
            month
        )

        students_list.append(new_student)

        print("\nStudent Added Successfully!")

    # ---------------- View All Students ----------------
    elif choice == "2":
        if len(students_list) > 0:
            app.view_all_students(students_list)
        else:
            print("No students available.")

    # ---------------- Search Student ----------------
    elif choice == "3":
        searched_rollno = input("Enter Roll Number: ")
        if len(students_list) > 0:
            app.search_any_student(students_list, searched_rollno)
        else:
            print("No students available.")

    # ---------------- Delete Student ----------------
    elif choice == "4":
        searched_rollno = input("Enter Roll Number: ")
        if len(students_list) > 0:
            app.delete_any_student(students_list, searched_rollno, deleted_student_list)
        else:
            print("No students available.")

    # ---------------- View Deleted Students ----------------
    elif choice == "5":
        if len(deleted_student_list) > 0:
            app.view_deleted_students(deleted_student_list)
        else:
            print("No deleted students available.")

    # ---------------- Add Marks ----------------
    elif choice == "6":
        if len(students_list) > 0:
            searched_rollno = input("Enter Roll Number: ")
            app.add_marks(searched_rollno, students_list, dict1)
        else:
            print("No students available.")

    # ---------------- Update Marks ----------------
    elif choice == "7":
        if len(students_list) > 0:
            searched_rollno = input("Enter Roll Number: ")
            app.update_marks(searched_rollno, students_list, dict1)
        else:
            print("No students available.")

    # ---------------- View Marks ----------------
    elif choice == "8":
        searched_rollno = input("Enter Roll Number: ")
        app.view_marks(searched_rollno, dict1)

    # ---------------- Calculate Total Marks ----------------
    elif choice == "9":
        searched_rollno = input("Enter Roll Number: ")
        app.calculate_total(searched_rollno, dict1)

    # ---------------- Calculate Percentage ----------------
    elif choice == "10":
        searched_rollno = input("Enter Roll Number: ")
        app.calculate_percentage(searched_rollno, dict1)

    # ---------------- Find Topper ----------------
    elif choice == "11":
        app.find_topper(students_list, dict1)

    # ---------------- Find Lowest ----------------
    elif choice == "12":
        app.find_lowest(students_list, dict1)

    # ---------------- Calculate Average Marks ----------------
    elif choice == "13":
        searched_rollno = input("Enter Roll Number: ")
        app.calculate_average_marks(searched_rollno, dict1)

    # ---------------- Assign Course ----------------
    elif choice == "14":
        searched_rollno = input("Enter Roll Number: ")
        app.assign_course(students_list, searched_rollno)

    # ---------------- Update Course ----------------
    elif choice == "15":
        searched_rollno = input("Enter Roll Number: ")
        app.update_course(students_list, searched_rollno)

    # ---------------- Assign Semester ----------------
    elif choice == "16":
        searched_rollno = input("Enter Roll Number: ")
        app.assign_semester(students_list, searched_rollno)

    # ---------------- View Students by Course ----------------
    elif choice == "17":
        course_name = input("Enter Course Name: ")
        app.view_students_by_course(students_list, course_name)

    # ---------------- View Students by Semester ----------------
    elif choice == "18":
        sem_number = int(input("Enter Semester Number: "))
        app.view_students_by_semester(students_list, sem_number)

    # ---------------- Count Total Students ----------------
    elif choice == "19":
        app.count_total_students(students_list)

    # ---------------- Count Students by Course ----------------
    elif choice == "20":
        app.count_students_by_course(students_list)

    # ---------------- Count Students by Semester ----------------
    elif choice == "21":
        app.count_students_by_semester(students_list)

    # ---------------- Sort by Name ----------------
    elif choice == "22":
        app.sort_by_name(students_list)

    # ---------------- Sort by Marks ----------------
    elif choice == "23":
        app.sort_by_marks(students_list, dict1)

    # ---------------- Sort by Percentage ----------------
    elif choice == "24":
        app.sort_by_percentage(students_list, dict1)

    # ---------------- Search by ID ----------------
    elif choice == "25":
        searched_rollno = input("Enter Roll Number: ")
        app.search_by_id(students_list, searched_rollno)

    # ---------------- Search by Name ----------------
    elif choice == "26":
        searched_name = input("Enter Student Name: ")
        app.search_by_name(students_list, searched_name)

    # ---------------- Search by Course ----------------
    elif choice == "27":
        course_name = input("Enter Course Name: ")
        app.search_by_course(students_list, course_name)

    # ---------------- Display Student Details ----------------
    elif choice == "28":
        searched_rollno = input("Enter Roll Number: ")
        app.display_student_details(students_list, searched_rollno)

    # ---------------- Display Top 3 ----------------
    elif choice == "29":
        app.display_top3(students_list, dict1)

    # ---------------- Display Failed Students ----------------
    elif choice == "30":
        raw = input("Enter passing mark (leave blank for default 33): ")
        if raw == "":
            passing_mark = 33
        else:
            passing_mark = int(raw)
        app.display_failed_students(students_list, dict1, passing_mark)

    # ---------------- Update Student ----------------
    elif choice == "31":
        if len(students_list) > 0:
            searched_rollno = input("Enter Roll Number: ")
            app.update_student(students_list, searched_rollno)
        else:
            print("No students available.")

    # ---------------- Exit ----------------
    elif choice == "32":
        print("\nProgram Ended.")
        break

    else:
        print("Wrong Input! Please enter a number between 1 and 32.")