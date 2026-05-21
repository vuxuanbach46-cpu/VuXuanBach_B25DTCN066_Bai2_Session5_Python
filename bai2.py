students = [
  [30,25,28],
  [20,22, 18],
  [35,32,30]
]

total_students = 0

for branch in range(len(students) ):
  for classroom in range(len(students[branch]) ):
    total_students += students[branch] [classroom]

  print(f"Chi nhánh {branch + 1}: {total_students} học viên")
  total_students = 0 
  
# code đang bị sai nó cộng dồn liên tục k có reset lại biến cộng nên có cứ vậy cộng dồn 
