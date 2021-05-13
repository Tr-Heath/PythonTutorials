#Warm up exercise utilizing loop structures.

student_heights = [180, 124, 165, 173, 189, 169, 146]
total = 0
numStudents = 0
averageheight = 0

for student in student_heights:
    total += student
    numStudents += 1

if numStudents > 0:
    averageheight = total / numStudents
displaytext = "The average height of the students is {:.2f}"
print(displaytext.format(averageheight))