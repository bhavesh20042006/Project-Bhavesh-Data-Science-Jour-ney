student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total = sum(student_scores)

#or

sum = 0
max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
    sum += score
print(sum)
print(max_score)