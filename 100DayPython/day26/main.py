numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

range_list = [num * 2 for num in range(1, 5)]
print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor"]
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

student_dict = {
    "student": ["A", "B", "C"],
    "score": [56, 76, 98]
}

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    print(row.student)