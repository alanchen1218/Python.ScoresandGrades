# Assignment: Scores and Grades
# Objectives:
# Practice writing functions and loops
# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

# Score: 60 - 69; Grade - D
# Score: 70 - 79; Grade - C
# Score: 80 - 89; Grade - B
# Score: 90 - 100; Grade - A

import random
random_num = random.random() # the random function will return a floating point number, that is 0.0 <= random_num < 1.0
random_num = random.randint(4,5) #random.randint, which will produce an integer between the two provided arguments
print(random_num)

def ScoresandGrades():
    print("Scores and Grades")
    for x in range(0,10):
        randomScore = random.randint(60,100)
        if randomScore >= 90:
            letter = "A"
        elif randomScore >= 80:
            letter = "B"
        elif randomScore >= 70:
            letter = "C"
        elif randomScore >= 60:
            letter = "D"
        print("Score:", randomScore, "; Your grade is", letter)
ScoresandGrades()