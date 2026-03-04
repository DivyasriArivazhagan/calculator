'''Student mark analysis
  - - - - - -
  1.average by subject and student 
  2.highesst & lowest per subject 
  3.overall class topper
  4.pass count per subject
  5.which subject is difficult ?
  6.ranking students
'''
import numpy as np

np.random.seed(20)
marks = np.random.randint(10,101,size=(20,5))
print(marks)

average_by_subject = np.mean(marks,axis =0)
average_by_student = np.mean(marks,axis=1)

highest_subject = np.max(marks,axis = 0)
lowest_subject = np.min(marks,axis = 0)

total_marks = np.sum(marks,axis = 1)
high_total = np.max(total_marks)
topper = np.argmax(total_marks)

pass_fail = marks >= 40
pass_count = np.sum(pass_fail,axis=0)

difficult_subject = np.argmin(average_by_subject)

rank = np.argsort(total_marks)

print(pass_fail)

print(total_marks)
print(high_total)
print(topper)

print("hishest marks per subject:",highest_subject)
print("lowest marks per subject:",lowest_subject)

print("Average by subject:",average_by_subject)
print("Average by student:",average_by_student)

print("Topper of the class",topper,"with the marks of ",high_total)

print("Pass count by subject ",pass_count)
print("Diffficult subject is ",difficult_subject ,"with the average marks of",average_by_subject[difficult_subject])

print("First rank of the class",rank[0])
print("first 5 rank of the class",rank[:5])