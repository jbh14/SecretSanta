import random

def main():
    gifterFromID = get_names()

    # pick a random name to start with
    start_id = random.randint(0, 9)
    print(start_id)
    print(f"Starting with {gifterFromID[start_id].name}")

    # while there are no unassigned names, find another name that was not who gave this person a gift
    assign_secret_santa_naive(gifterFromID, gifterFromID[start_id])

    cur = gifterFromID[start_id]
    counter = 0
    while cur.gifted_to is not None and counter < 10:
        print(f"{cur.name} --> ")
        cur = cur.gifted_to
        counter += 1

# naive approach - randomly pick a name, reject if it's the same person, someone who gifted this person, someone who has already been gifted, or forms a cycle before final gifter
def assign_secret_santa_naive(gifterFromID, cur):
    gifters = len(gifterFromID.values())
    gifted = 0
    
    while gifted < gifters:
        print("")
        print("Finding a giftee for " + cur.name)
        new_id = random.randint(0, 9)
        print(f"Trying {gifterFromID[new_id].name}")

        if gifterFromID[new_id].gifted:
            print("Already gifted")
            continue
        elif new_id == cur.id:
            print("Same person")
            continue
        elif gifterFromID[new_id].gifted_to == cur.id:
            print("Giftee gifted this person")
            continue
        # we can only allow a cycle IF this is the last person to gift 
        elif gifted < (gifters - 1) and gifterFromID[new_id].gifted_to is not None: 
            print("Cycle detected - not last person")
            continue
        else:
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

    while gifted < (gifters - 1): # we need to make sure the last person is gifting to the original gifter
        print("")
        print("Finding a giftee for " + cur.name)
        
        

        # we only need to consider unassigned gifters, minus the current person
        print(f"# gifted: {gifted}")
        
        new_relative_id = random.randint(0, 10 - gifted - 2) # subtract 2 because we are 0-indexed and we need to exclude the current person
        # now, we need to find the actual person from the list of unassigned gifters
        print(f"Relative ID: {new_relative_id}")
        print(f"Unassigned gifters: {unassignedGifters}")
        
        new_id = unassignedGifters[new_relative_id]
        print(f"Trying {gifterFromID[new_id].name}")

        # should not have to check for "gifted" or "same person" - we are only considering unassigned gifters
        if gifterFromID[new_id].gifted:
            print("Already gifted")
            continue
        elif new_id == cur.id:
            print("Same person")
            continue
        elif gifterFromID[new_id].gifted_to == cur.id:
            print("Giftee gifted this person")
            continue
        # we can only allow a cycle IF this is the last person to gift 
        # this will need adjusted here - let's just automaticallly gift to the original gifter if this is the last person
        elif gifted < (gifters - 1) and gifterFromID[new_id].gifted_to is not None: 
            print("Cycle detected - not last person")
            continue
        else:
            print("valid giftee")
            print(f"{cur.name} is gifting to {gifterFromID[new_id].name}")
            cur.set_gifted_to(gifterFromID[new_id])
            unassignedGifters.remove(new_id)
            cur = gifterFromID[new_id]
            cur.set_gifted()
            gifted += 1

    # last person - gift to original gifter
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

    print("Enter 10 names:")

    # Loop to collect 10 inputs
    for i in range(10):
        user_input = input(f"Input {i+1}: ")
        gifterFromID[i] = Gifter(user_input, i)

    # Display the collected inputs
    print("\nYou entered:")
    for i in range(10):
        print(f"{i+1}. {gifterFromID[i].name}")

    return gifterFromID


if __name__ == "__main__":
    main()