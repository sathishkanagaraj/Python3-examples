#! python3
# inputvalidation.py  - input validation with the help of available modules.
import random

import pyinputplus as pyip
import time


def takenumber():
    numberOfQuestions = 10
    correctAnswers = 0
    for questionNumber in range(numberOfQuestions):
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)

        prompt = '#%s: %s x %s = ' % (questionNumber, num1, num2)
        try:
            # Right answers are handled by allowRegexes.
            # Wrong answers are handled by blockRegexes, with a custom message.
            #print(pyip.inputNum('>>>>>', min=4, lessThan=10, timeout=10, limit=2, default=5))
            #print(pyip.inputNum(allowRegexes=[r'(Q|W|E|R|T|Y)+', r'zero']))
            pyip.inputNum(prompt, allowRegexes=['^%s$' %(num1 * num2)],
                            blockRegexes=[('.*', 'In-Correct')], timeout=8, limit=3)
        except pyip.TimeoutException:
            print('Out of time!')
        except pyip.RetryLimitException:
            print('Out of tries!')
        else:
            # This block runs if no exceptions were raised in the try block.
            print('Correct!')
            correctAnswers += 1
            time.sleep(1) # Brief pause to let user see the result.
            print('Score: %s / %s' % (correctAnswers, numberOfQuestions))


takenumber()