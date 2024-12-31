import random
from secretSanta_util import get_names, Gifter, assign_secret_santa_smartRandomize

def createSecretSantaAssignments(gifterFromID = None) -> Gifter:
    
    if not gifterFromID:
        gifterFromID = get_names()

    # pick a random name to start with
    start_id = random.randint(0, 9)
    print(start_id)
    print(f"Starting with {gifterFromID[start_id].name}")

    # while there are no unassigned names, find another name that was not who gave this person a gift
    assign_secret_santa_smartRandomize(gifterFromID, gifterFromID[start_id])

    cur = gifterFromID[start_id]
    counter = 0
    while cur.gifted_to is not None and counter < 10:
        print(f"{cur.name} --> ")
        cur = cur.gifted_to
        counter += 1

    return gifterFromID[start_id]  # return the first person in the linked list

if __name__ == "__main__":
    secretSantaLinkedList = createSecretSantaAssignments()
