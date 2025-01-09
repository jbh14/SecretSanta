# SecretSanta
This is me playing around with some algorithms for a better Secret Santa assignment after being frustrated with Elfster creating multiple disconnected cycles.
In particular, no two people should be gifting each other (this is strangely annoying to me) in a Secret Santa group that is larger than 2 participants - what's the fun in that?

# Running this code
Create virtual environment: 
```
python3 -m venv .venv       # Mac/Linux
python -m venv .venv        # Windows
```

Activate virtual environment: 
```
source .venv/bin/activate   # Mac/Linux
.\venv\Scripts\activate     # Windows
```

Install required dependencies:
```
pip install -r requirements.txt
```

Run tests (omit `-s` flag if not wanting to print test outputs):
```
pytest -s
```

# Approach
Definitions:
- "gifter" - someone giving a gift to someone else
- "giftee" - the person on the receiving end of a gift.  A "gifter" gives a gift to their assigned "giftee".

I realized that we can avoid creating multiple, disconnected cycles of gifters by simply never assigning a giftee that is already a gifter at each step of assignment.  The only exception is the final gifter, who should have the starting/original gifter assigned as their giftee.

In addition to ensuring that there is only one cylce in the randomly-generated Secret Santa assignments for any group size, I tried two approaches to generating the assignments:
1. A "naive" approach, where for each gifter to assign a giftee to, a random potential giftee is selected but rejected if it is the same person, a person who was already gifted, or a person whose assignment would lead to multiple, disconnected "cycles" within the assignment result (a person who already has a giftee assigned, unless this is the last gifter to assign a giftee to).
2. A smarter approach that only considers valid giftees as candidates for the random assignment from the start (I use some "shifting" of the random index generated within the assignment array to accomplish this).

The results are returned in the form of a signle "Gifter" object, which is the head of a linked list of "Gifters" (each Gifter's "gifted_to" represents the person they are buying a gift for, essentially the next element in the linked list).

# Testing
I tested both approaches for groups of 10 and 100 participants.  The test ensures that:
1. Every participant was included in the assignment
2. Only 1 cycle is present in the assignment (no separate, disconnected cycles)

# Results
In general, the "smarter" approach seems to generally execute roughly twice as fast as the "naive" approach (possibly faster as input size grows, but a Secret Santa group beyond 1000 people seems a little far-fetched):
| Secret Santa Participants | Naive Approach Execution Time | Smart Approach Execution Time |
|-------|-------------------| -------------------|
| 10     |     0.0000219s | 0.0000122s |
| 100    |    0.000303s  | 0.0000629s |
| 1000   | 0.00340s | 0.00170s |
