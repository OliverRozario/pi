OverallHighest = 0
OverallLowest = 100
OverallTotal = 0
for test in range(1, 5):
    SubjectHighest = 0
    SubjectLowest = 100
    SubjectTotal = 0
    match test:
        case 1:
            SubjectName = "Maths"
        case 2:
            SubjectName = "Science"
        case 3:
            SubjectName = "English"
        case 4:
            SubjectName = "IT"
    for StudentNumber in range(1, 601):
        while True:
            try:
                Mark = int(input(f"Enter Student {StudentNumber}'s mark for {SubjectName}: "))
                if -1 < Mark < 101:
                    break
            except ValueError:
                print("Invalid input. Please enter valid number")
        if Mark < OverallLowest:
            OverallLowest = Mark
        if Mark < SubjectLowest:
            SubjectLowest = Mark
        if Mark > OverallHighest:
            OverallHighest = Mark
        if Mark > SubjectHighest:
            SubjectHighest = Mark
        OverallTotal = OverallTotal + Mark
        SubjectTotal = SubjectTotal + Mark
    SubjectAverage = SubjectTotal / 600
    print(SubjectName)
    print(f"Average is {SubjectName}")
    print(f"Highest Mark is {SubjectHighest}")
    print(f"Lowest Mark is {SubjectLowest}")
OverallAverage = OverallHighest / 2400
print(f"Overalll Average is {OverallAverage}")
print(f"Overall Highest Mark is {OverallHighest}")
print(f"Overall Lowest Mark is {OverallLowest}")
