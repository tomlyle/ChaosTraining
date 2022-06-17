import random as r
from os import getcwd

# gv stands for global variables
class gv:
    list_of_exercises = []
    ab_exercises = []

def init():
    # get the contents of the file
    fn = getcwd() + "/exercises.txt"
    file = open(fn, "r")
    contents = file.readlines()

    abs_ex = False

    # for all the lines in the text document, split by each comma and add to master list
    for i in contents:
        exercises = i.split(",")
        for each_exercise in exercises:
            if each_exercise != '\n':
                if each_exercise == "ABS":
                    abs_ex = True
                formatted_exercise = each_exercise.strip(" ")
                result = formatted_exercise[0].upper() + formatted_exercise[1:]
                if abs_ex:
                    if result != "ABS":
                        gv.ab_exercises.append(result)
                else:
                    gv.list_of_exercises.append(result)


def __main__(exercises_lower, exercises_upper, ab_lower, ab_upper, sets_lower_bound, sets_upper_bound, reps_lower_bound, reps_upper_bound):
    init()
    num_of_exercises = r.randint(exercises_lower, exercises_upper)
    num_ab_exercises = r.randint(ab_lower, ab_upper)
    rolling_string = "=======================\n"
    rolling_string += "     Chaos Program\n=======================\n\n"
    # Main accessories choices:
    for i in range(num_of_exercises - 1):
        choice = r.choice(gv.list_of_exercises)
        sets = r.randint(sets_lower_bound, sets_upper_bound)
        reps = r.randint(reps_lower_bound, reps_upper_bound)
        rolling_string += "Exercise {}: {}\n   {} x {}\n\n".format(i+1, choice, sets, reps)
    # Ab accessories choices
    for i in range(num_ab_exercises):
        choice = r.choice(gv.ab_exercises)
        sets = r.randint(sets_lower_bound, sets_upper_bound)
        reps = r.randint(reps_lower_bound, reps_upper_bound)
        rolling_string += "Exercise {}: {}\n   {} x {}\n\n".format(num_of_exercises + i, choice, sets, reps)
    print(rolling_string)


if __name__ == "__main__":
    __main__(4, 10, 1, 2, 3, 6, 5, 20)

