__author__ = "Steven Brown"
from collections import deque

twelveCount = 0
minuteCount = 0
dayCount = 0
numBalls = int(0)
numberMinutesToRun = 0
originalOrder = ""
originalId = ""
minuteStack = []
fiveStack = []
hourStack = [str(0)]
ballQueue = deque([])

def loadqueue(numBalls):
    for x in range(1,int(numBalls)+1):
        ballQueue.append(x)

def executeminute():

    global minuteCount, twelveCount, dayCount

    minuteCount += 1

    if len(minuteStack) != 4:
        minuteStack.append(ballQueue.popleft()); #// if there is room in the minuteStack, add a ball from the queue.

    else:
        #// this code will execute iff the minuteStack was full
        for i in range(0,4):
            ballQueue.append(minuteStack.pop()) #// pop all off the minute stack, add to ballQueue

        if len(fiveStack) != 11:
            fiveStack.append(ballQueue.popleft()) #// if there is room in the Fives Stack, add ball from the queue.
        else:
            #// this code will execute if the fiveStack was full
            for j in range(0,11):
                ballQueue.append(fiveStack.pop()) #// pop all off the fiveStack, and add to ballQueue

            if len(hourStack) != 12:
                hourStack.append(ballQueue.popleft());

            else:
                for k in range(0,11):
                    ballQueue.append(hourStack.pop())

                ballQueue.append(ballQueue.popleft())

                twelveCount += 1

                if twelveCount == 2:
                    dayCount += 1
                    twelveCount = 0

def executeminutes(numMin):
    global twelveCount, dayCount

    while numMin != 0:

        if len(minuteStack) != 4:
            minuteStack.append(
                ballQueue.popleft());  # // if there is room in the minuteStack, add a ball from the queue.

        else:
            # // this code will execute iff the minuteStack was full
            for i in range(0, 4):
                ballQueue.append(minuteStack.pop())  # // pop all off the minute stack, add to ballQueue

            if len(fiveStack) != 11:
                fiveStack.append(
                    ballQueue.popleft())  # // if there is room in the Fives Stack, add ball from the queue.
            else:
                # // this code will execute if the fiveStack was full
                for j in range(0, 11):
                    ballQueue.append(fiveStack.pop())  # // pop all off the fiveStack, and add to ballQueue

                if len(hourStack) != 12:
                    hourStack.append(ballQueue.popleft());

                else:
                    for k in range(0, 11):
                        ballQueue.append(hourStack.pop())

                    ballQueue.append(ballQueue.popleft())

                    twelveCount += 1

                    if twelveCount == 2:
                        dayCount += 1
                        twelveCount = 0

        numMin -= 1

def loadstacks():

    while len(hourStack) != 12:
        hourStack.append(ballQueue.popleft())

    while len(fiveStack) != 11:
        fiveStack.append(ballQueue.popleft())

    while len(minuteStack) != 4:
        minuteStack.append(ballQueue.popleft())

def gettime():

    hour = len(hourStack)
    minutes = ""

    if len(fiveStack) == 1 or len(fiveStack) == 0:
        minutes = "0" + str(len(minuteStack))
    else:
        minutes = str((len(fiveStack) * 5) + len(minuteStack))

    return str(hour) + ":" + str(minutes)

def getcurrentorder():

    currentorder = "";

    for i in range(1, len(hourStack)):
        currentorder += str(hourStack[i])

    if len(fiveStack) == 0:
        for j in range(0,len(fiveStack)):
            currentorder += str(fiveStack[j])

    if len(minuteStack) == 0:
        for k in range(0,len(minuteStack)):
            currentorder += str(minuteStack[i])

    for x in range(0, len(ballQueue)):
        currentorder += str(ballQueue[x])

    return currentorder

def printjson():
    minutes = ''.join(str(minuteStack))

    fives = ''.join(str(fiveStack))

    hourStack.pop(0)
    hours = ''.join(str(hourStack))

    queue = '[%s]' % ', '.join(map(str, ballQueue))

    json = "{\"Min\":" + minutes + ",\"FiveMin\":" + fives + ",\"Hour\":" + hours + ",\"Main\"" + queue + "}"

    json = json.replace(" ", "")
    return str(json)


numBalls = input("Enter Number of balls (27 - 127): ")

try:
    if not (27 <= int(numBalls) <= 127):
        print("Invalid Input. Please enter a integer bewteen 27 and 127")
        exit(0)
except Exception:
    print("Invalid Input. Please enter a integer bewteen 27 and 127")
    exit(0)


tmp = input("do you want to enter minutes? (y/n)")

loadqueue(int(numBalls))

if tmp == "n" or tmp == "N":

    loadstacks()
    condition = False

    originalOrder = getcurrentorder()

    while condition == False:
        executeminute()
        #print(gettime())
        if originalOrder == getcurrentorder():
            condition = True

    print(str(numBalls) + " balls cycle after "+str(dayCount) + " days")

elif tmp == "y" or tmp == "Y":
    numberMinutesToRun = input("Enter Number of minutes to run: ")

    try:
        if not (0 <= int(numberMinutesToRun)):
            print("Invalid Input. Please enter a integer greater than 0.")
            exit(0)
    except Exception:
        print("Invalid Input. Please enter a integer.")
        exit(0)

    executeminutes(int(numberMinutesToRun))
    print(printjson())

else:
    print("Invalid inputs")
