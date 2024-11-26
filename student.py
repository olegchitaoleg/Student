students = [{"name": "Aaron", "grades": [5, 3, 3, 5, 4]},
{"name": "Bilbo", "grades": [2, 2, 2, 3]},
{"name": "Johhny", "grades": [4, 5, 5, 2]},
{"name": "Khendrik", "grades": [4, 4, 3 ]},
{"name": "Steve", "grades": [5, 5, 5, 4, 5]}]
for student in students:
    avg_score = sum(student["grades"]) / len(student["grades"])
    print(f'{student["name"]}: Средний балл = {avg_score:.2f}')




