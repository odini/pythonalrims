import random
import string

alphabet = string.lowercase + ' '
goal = 'methinks it is like a weasel'

def random_generator(size):
    return ''.join(random.choice(alphabet) for i in range (size))

def scoring(goal):
    sum = 0
    #sentence = random_generator(len(goal))
    sentence = 'methinks da ds like a weadel'
    print sentence, goal
    for i in range (len(goal)):
        if sentence[i] == goal[i]:
            sum += 1
    return (float((sum/len(goal))*100))

print scoring(goal)
