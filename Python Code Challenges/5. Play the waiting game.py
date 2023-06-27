import timeit
import random

def waiting_game():
    time = random.randint(0, 5)
    print("Your target time is " + str(time) + " seconds.")
    input("---Press Enter to Begin---\n")
    startTime = timeit.default_timer()
    input("...Press Enter again after " + str(time) + " seconds...\n")
    endTime = timeit.default_timer()
    actualTime = round(endTime - startTime, 3)
    timeDiff = round(actualTime - time, 3)
    if timeDiff < 0:
        fastOrSlow = "fast"
        timeDiff *= -1
    elif timeDiff > 0:
        fastOrSlow = "slow"
    else:
        print("Unbelievable! Perfect timing!")
        return
    print("Elapsed time: " + str(actualTime) + " (" + str(timeDiff) + " seconds too " + str(fastOrSlow) + ")")

waiting_game()  