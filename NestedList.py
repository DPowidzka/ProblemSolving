if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])


# student[1] -> score
unique_scores = sorted(set(student[1] for student in students))
# drugi wynik na liscie unique_scores
second_score = unique_scores[1]
# student[0] -> name, student[1] ->score
second_students = [student[0] for student in students if student[1] == second_score] 
second_students.sort()
for student in second_students:
    print(student)

      
