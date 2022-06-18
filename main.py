import random as r
from os import getcwd


class GlobalVariables:
    list_of_exercises = []
    ab_exercises = []

    reps_range = (5, 20)
    sets_range = (3, 6)
    range_exercises = (5, 15)
    range_ab_exercises = (1, 3)

    # Import ranges of reps and sets
    reps_lower_bound, reps_upper_bound = reps_range
    sets_lower_bound, sets_upper_bound = sets_range

    # Create list to add each exercise into once it has been chosen
    exercises_list = []

    superset_exercises = []
    message = ""


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
                        GlobalVariables.ab_exercises.append(result)
                else:
                    GlobalVariables.list_of_exercises.append(result)


def random_exercise(exercise_list):
    # Choose an exercise and remove it from the list
    choice = r.choice(exercise_list)
    exercise_list.remove(choice)

    # Determine the sets and reps for each exercise
    sets = r.randint(GlobalVariables.sets_lower_bound, GlobalVariables.sets_upper_bound)
    reps = r.randint(GlobalVariables.reps_lower_bound, GlobalVariables.reps_upper_bound)

    # Superset and dropset probabilities
    superset = False
    dropset = False

    superset_proc = r.random()
    dropset_proc = r.random()

    if superset_proc <= 0.50:
        superset = True
    if dropset_proc <= 0.5:
        dropset = True
    if superset and dropset:
        tiebreaker = r.randint(0, 1)
        if tiebreaker == 0:
            superset = False
        elif tiebreaker == 1:
            dropset = False

    # extra_effort tuple to be sent into the package
    if superset:
        extra_work = random_exercise(exercise_list)
        keyword = "superset"
    elif dropset:
        number_of_drops = r.randint(1, 3)
        extra_work = number_of_drops
        keyword = "dropset"
    else:
        extra_work = False
        keyword = "nothing"

    bundle = (keyword, extra_work)
    # Package variables and return
    package = (choice, sets, reps, bundle)
    return package


def unpack_ss_ds(bundle):
    # unpack all layers of the superset/dropset package
    keyword, extra_work = bundle
    if keyword == "superset":
        print("ss trigger")
        exercise, sets, reps, subbundle = extra_work
        message = "    supersetted with {} for {} reps.\n".format(exercise, reps)
        GlobalVariables.message += message
        unpack_ss_ds(subbundle)

    elif keyword == "dropset":
        print("ds trigger")
        message = "    dropsetted {} time".format(extra_work)
        if extra_work != 1:
            message += "s"
        message += ".\n"
        GlobalVariables.message += message


def __main__():
    init()

    # Determine the allocation of ab workouts to regular workouts.
    # Start by importing the ranges of the exercise limits
    exercises_lower_bound, exercises_upper_bound = GlobalVariables.range_exercises
    ab_lower_bound, ab_upper_bound = GlobalVariables.range_ab_exercises

    # 1. Determine the number of total exercises
    # 2. Determine the number of ab exercises
    # 3. Subtract the number of ab exercises from the total to calc the remaining.
    total_exercises = r.randint(exercises_lower_bound, exercises_upper_bound)
    num_ab_exercises = r.randint(ab_lower_bound, ab_upper_bound)
    num_other_exercises = total_exercises - num_ab_exercises

    exercises_list = []

    print("=======================\n      Chaos Program\n=======================\n")
    # Main accessories choices:
    for i in range(num_other_exercises):
        try:
            exercises = random_exercise(GlobalVariables.list_of_exercises)
            exercises_list.append(exercises)
        except IndexError:
            pass
    # Ab accessories choices
    for i in range(num_ab_exercises):
        try:
            exercises = random_exercise(GlobalVariables.ab_exercises)
            exercises_list.append(exercises)
        except IndexError:
            pass

    r.shuffle(exercises_list)
    # Print out the exercises
    counter = 1
    for i in exercises_list:
        exercise, sets, reps, bundle = i
        unpack_ss_ds(bundle)
        print("Exercise {}: {}\n    {} x {}\n{}".format(counter, exercise, sets, reps, GlobalVariables.message))
        GlobalVariables.message = ""
        counter += 1


if __name__ == "__main__":
    __main__()

