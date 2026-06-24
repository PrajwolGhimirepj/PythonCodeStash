import random

states = ["R", "P", "S"]

wins = {
    ("R", "S"): "P1",
    ("S", "P"): "P1",
    ("P", "R"): "P1",
    ("S", "R"): "P2",
    ("P", "S"): "P2",
    ("R", "P"): "P2",
}

def play():
    p1 = random.choice(states)
    p2 = input("Enter your choice (R/P/S): ").strip().upper()

    if p2 not in states:
        print("Invalid choice. Please enter R, P, or S.")
        return

    print("P1 =", p1)
    print("P2 =", p2)

    if p1 == p2:
        print("Result: Tie")
    else:
        winner = wins.get((p1, p2), "P2")
        print("Result:", winner, "wins")

    print("Next Round")


for i in range(5):
    play()