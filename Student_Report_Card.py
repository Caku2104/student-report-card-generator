#   Student Report Card Generator
continuing = True
choice = ""
while continuing and choice != "quit":
    total = int(input("How many students do you have?:"))
    if total <= 0 or total >= 1000:
        print("You cannot use this program.")
        choice = input("If you want to get out off the program, write -> 'quit' : ")
    else:
        continuing = False

students = []
final_results = []

counter = 1
while counter <= total:
    continuing = True
    while continuing:
        name = input(f"What is the name of the student number {counter}: ")
        if name == "":
            print("You haven't entered a name.")
        elif name.isdigit():
            print("A name cannot contain numbers.")
        else:
            continuing = False

    grades = []
    continuing = True
    while continuing:
        for grade in input("What are the grades of the student: ").split(","):
            if int(grade) < 0 or int(grade) > 100:
                print("This grade(s) is invalid. Please enter again.") 
            else:
                grades.append(int(grade))
                continuing = False

    students.append({"name": name, "grade": grades})
    
    points = sum(grades)

    average = points/len(grades)

    final_results.append({"name": name, "average": average})

    counter += 1

def get_average(final_results):
    return final_results["average"]

final_results = sorted(final_results, key = get_average, reverse = True)

best_student = final_results[0]
worst_student = final_results[-1]

print()
print(f"Best student is {best_student["name"]} with avg = {best_student["average"]:.1f}.")
print(f"Worst student is {worst_student["name"]} with avg = {worst_student["average"]:.1f}.")
print()

for student in final_results:
    print(f"{student["name"]}: Avg = {student["average"]:.1f}", end= "")
    if student["average"] < 60:
        print(", Fail.")
    else:
        print(", Pass!")