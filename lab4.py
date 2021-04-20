"""
Program allows user to attempt to guess the correct answer 3 times
"What is the capital of California?
Answer : Sacramento"

First set max_tries = 3. Loop iterates 3 times.
for each iteration, we ask the userr for the answer (user input)
Based on the answer user gives, we check top see if the user input matches the answer if so print CorrecT!
terminate loop with a break statement

if the user could not guess the correct answer within the maximum tries, print
"You have used up your allotement of guesses, print "The correct answer was California" 
"""
"""
PSUEDOCODE

main
    question = What is the capital of California
    answer = California
    ask(question, answer)

ask
    tries = 3
    loop three times
        increment tries
        ask user inputs()
        check answer
            if correct, print "Correct" exit loop
            if incorrect, print "Incorrect" 
                loop for additional inputs
            if incorrect and no tries left
                print "You have used  up your allotment of guesses"\
                print the correct Answer "California"
main
                
"""

