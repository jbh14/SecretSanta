import random
from secretSanta_util import get_number_of_gifters, get_names, Gifter, assign_secret_santa_naive, print_output

def createSecretSantaAssignments(gifterFromID = None) -> Gifter:
    
    num_gifters = 10 # default, but should be gathered from user input or from size of gifterFromID

    if not gifterFromID:
         # Get the number of participants
        num_gifters = get_number_of_gifters()
        # Get the names of the participants
        gifterFromID = get_names(None, num_gifters)

    else:
        num_gifters = len(gifterFromID.values())

    # pick a random name to start with
    start_id = random.randint(0, num_gifters - 1)

    # while there are no unassigned names, find another name that was not who gave this person a gift
    assign_secret_santa_naive(gifterFromID, gifterFromID[start_id])

    # displaying output, if desired
    print_output(gifterFromID[start_id], num_gifters)

    return gifterFromID[start_id]  # return the first person in the linked list

if __name__ == "__main__":
    secretSantaLinkedList = createSecretSantaAssignments()
