# students = [
#   [30,25,28],
#   [20,22, 18],
#   [35,32,30]
# ]

# total_students = 0

# for branch in range(len(students) ):
#   for classroom in range(len(students[branch]) ):
#     total_students += students[branch] [classroom]

#   print(f"Chi nhánh {branch + 1}: {total_students} học viên")
#   total_students = 0 
  
# code đang bị sai nó cộng dồn liên tục k có reset lại biến cộng nên có cứ vậy cộng dồn 



branch_count = int(input("Nhập sô lượng chi nhánh: "))
class_count = int(input("Nhập sô lớp học của mối chi nhánh: "))


for branch in range(1, branch_count + 1):
  print(f"\nChi nhánh {branch}")

  total_students = 0
  
  for classroom in range(1, class_count + 1):
    student_count = int(input(f"Nhập sô học viên lớp {classroom}: "))
    total_students += student_count

  print(f"Chi nhánh {branch}: {total_students} học viên")
  
  
# code lỗi do đang đặt sai vị trí của biến reset total_students 
# Phải đặt biến này ở bên trong vòng lặp của từng chi nhánh
