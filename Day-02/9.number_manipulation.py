bmi =84 / 1.65 ** 2
print(bmi)


print(int(bmi))
#gives a complete whole number

print(round(bmi))
#for rounding off to nearest decimal places


print(round(bmi, 2))
#rounding up bmi to specific decimal places


#assignment operators
score = 0
score += 1
print(score)
score -= 1
print(score)
score *= 1
print(score)
score /= 1
print(score)




#fstrings used for presenting different data types together
score = 0
height = 1.8
is_winning = True
print(f"your score is {score}, your height is {height}, you are winning is {is_winning}")
