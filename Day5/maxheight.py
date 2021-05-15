#Similar warm up challenge utilizing loops in python
#Find the maximum int in a set input by the user without using the built in max()
student_scores = input("Input a list of student scores ").split()
max = int(student_scores[0])
for n in range(1, len(student_scores)):
  if int(student_scores[n]) > max:
    max = int(student_scores[n])
  
print(f"The highest score in the class is: {max}")