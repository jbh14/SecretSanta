import random

def main(participants=10):

    # Get the number of participants
    num_gifters = get_number_of_gifters()

    # Get the names of the participants
    gifterFromID = get_names(num_gifters)

    # pick a random name to start with
    start_id = random.randint(0, num_gifters - 1)

    # while there are no unassigned names, find another name that was not who gave this person a gift
    assign_secret_santa_smartRandomize(gifterFromID, gifterFromID[start_id])

    # displaying output, if desired
    print_output(gifterFromID[start_id], num_gifters)
    
def print_output(cur, num_gifters):
    counter = 0
    while cur.gifted_to is not None and counter < num_gifters:
        print(f"{cur.name} --> ")
        cur = cur.gifted_to
        counter += 1

# naive approach - randomly pick a name, reject if it's the same person, someone who gifted this person, someone who has already been gifted, or forms a cycle before final gifter
def assign_secret_santa_naive(gifterFromID, cur):
    gifters = len(gifterFromID.values())
    gifted = 0
    
    # toggle on/off to see the processing steps play out
    print_processing_steps = False

    while gifted < gifters:
        
        if print_processing_steps:
            print("")
            print("Finding a giftee for " + cur.name)
        
        new_id = random.randint(0, gifters - 1)
        
        if print_processing_steps:
            print(f"Trying {gifterFromID[new_id].name}")

        if gifterFromID[new_id].gifted:
            if print_processing_steps:
                print("Already gifted")
            continue
        elif new_id == cur.id:
            if print_processing_steps:
                print("Same person")
            continue
        elif gifterFromID[new_id].gifted_to == cur.id:
            if print_processing_steps:
                print("Giftee gifted this person")
            continue
        # we can only allow a cycle IF this is the last person to gift 
        elif gifted < (gifters - 1) and gifterFromID[new_id].gifted_to is not None: 
            if print_processing_steps:
                print("Cycle detected - not last person")
            continue
        else:
            if print_processing_steps:
                print("valid giftee")
                print(f"{cur.name} is gifting to {gifterFromID[new_id].name}")
            cur.set_gifted_to(gifterFromID[new_id])
            cur = gifterFromID[new_id]
            cur.set_gifted()
            gifted += 1

# slightly better approach - randomly pick a name ONLY from remaining ungifted people, excluding this person
# still reject if it's someone who gifted this person forms a cycle before final gifter
def assign_secret_santa_smartRandomize(gifterFromID, originalGifter):
    gifters = len(gifterFromID.values())
    gifted = 0
    
    unassignedGifters = list(gifterFromID.keys()) # this is only "available" and valid giftees
    unassignedGifters.remove(originalGifter.id) # remove the current person from the list of available giftees

    cur = originalGifter

    # toggle on/off to see the processing steps play out
    print_processing_steps = False

    while gifted < (gifters - 1): # we need to make sure the last person is gifting to the original gifter
        
        if print_processing_steps:
            print("")
            print("Finding a giftee for " + cur.name)
            # we only need to consider unassigned gifters, minus the current person
            print(f"# gifted: {gifted}")
        
        new_relative_id = random.randint(0, gifters - gifted - 2) # subtract 2 because we are 0-indexed and we need to exclude the current person
        # now, we need to find the actual person from the list of unassigned gifters
        
        if print_processing_steps:
            print(f"Relative ID: {new_relative_id}")
            print(f"Unassigned gifters: {unassignedGifters}")
        
        new_id = unassignedGifters[new_relative_id]
        
        if print_processing_steps:
            print(f"Trying {gifterFromID[new_id].name}")

        # should not have to check for "gifted" or "same person" - we are only considering unassigned gifters
        if gifterFromID[new_id].gifted:
            if print_processing_steps:
                print("Already gifted")
            continue
        elif new_id == cur.id:
            if print_processing_steps:
                print("Same person")
            continue
        elif gifterFromID[new_id].gifted_to == cur.id:
            if print_processing_steps:
                print("Giftee gifted this person")
            continue
        # we can only allow a cycle IF this is the last person to gift 
        # this will need adjusted here - let's just automaticallly gift to the original gifter if this is the last person
        elif gifted < (gifters - 1) and gifterFromID[new_id].gifted_to is not None: 
            if print_processing_steps:
                print("Cycle detected - not last person")
            continue
        else:
            if print_processing_steps:
                print("valid giftee")
                print(f"{cur.name} is gifting to {gifterFromID[new_id].name}")
            cur.set_gifted_to(gifterFromID[new_id])
            unassignedGifters.remove(new_id)
            cur = gifterFromID[new_id]
            cur.set_gifted()
            gifted += 1

    # last person - gift to original gifter
    if print_processing_steps:
        print("Last person - gifting to original gifter")
    cur.set_gifted_to(originalGifter)
    cur = originalGifter
    cur.set_gifted()
    gifted += 1

# linked list element
class Gifter:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.gifted = False
        self.gifted_to = None

    def set_gifted(self):
        self.gifted = True

    def set_gifted_to(self, gifted_to):
        self.gifted_to = gifted_to

def get_number_of_gifters(input_func=input):
    """
    Collects the number of participants from user input or a provided input function (mocked during testing).

    Args:
        input_func: Function to use for input. Defaults to built-in input().
    
    Returns:
        int: The number of participants.
    """

    # Get the number of participants
    num_gifters = int(input_func("Enter the number of participants: "))

    return num_gifters

def get_names(input_func=input, num_gifters=10):
    """
    Collects 10 names from user input or a provided input function (mocked during testing).

    Args:
        input_func: Function to use for input. Defaults to built-in input().
    
    Returns:
        dict: A dictionary mapping IDs to Gifter objects.
    """

    # Initialize an empty dict
    gifterFromID = dict()

    print(f"Please enter the names of {num_gifters} participants.")

    # Loop to collect inputs
    for i in range(num_gifters):
        user_input = input(f"Input {i+1}: ")
        gifterFromID[i] = Gifter(user_input, i)

    return gifterFromID


if __name__ == "__main__":
    main()