import random

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):
        return self.name < other.name

    def __ge__(self, other):
        return self.name >= other.name

def main():
    num_students = int(input("Enter the number of students: "))
    students = []
    for i in range(num_students):
        name = input(f"Enter the name of student {i+1}: ")
        scores = [random.randint(60, 100) for _ in range(3)]  # Generating random scores between 60 and 100
        students.append(Student(name, scores))

    print("\nComparison Tests:")
    for i in range(num_students):
        for j in range(num_students):
            if i != j:
                print(f"{students[i].name} == {students[j].name}: {students[i] == students[j]}")
                print(f"{students[i].name} < {students[j].name}: {students[i] < students[j]}")
                print(f"{students[i].name} >= {students[j].name}: {students[i] >= students[j]}")
                print()

    print("\nUnsorted list of students:")
    for student in students:
        print("Name:", student.name)
        print("Scores:", " ".join(map(str, student.scores)))

    students.sort()
    print("\nSorted list of students:")
    for student in students:
        print("Name:", student.name)
        print("Scores:", " ".join(map(str, student.scores)))

if __name__ == "__main__":
    main()
    #gusto niya ng effort, eto effort ./.