student_name_ru = "Столыпин Александр"
student_name_en = "Stolypin Aleksandr"
student_number = 23
group_name = "М3О-111БВ-26"
language_name = "Python"

control_value = 304 * student_number
student_id = f"{group_name}/{student_number:02d}"

print(f"Hello to 304 from {student_name_en}, number {student_number}, group {group_name}!")
print(f"Привет, 304! Это {student_name_ru}, номер {student_number}, группа {group_name}!")
print(f"Student ID: {student_id} | Language: {language_name} | Control: {control_value}")
print(f"Word count in name: {len(student_name_en.split())}")