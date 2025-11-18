import time
import threading
import sys
import numpy as np
import pandas as pd

# Global variable to stop quiz when time is up
time_up = False

def countdown(seconds):
    global time_up
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        print(f"\rTime Left: {mins:02d}:{secs:02d}", end="")
        time.sleep(1)
        seconds -= 1

    time_up = True
    print("\n\n⏳ Time is up!")
    print("Quiz Ended.")
    sys.exit()


# ==========================
#    QUIZ DATA (PANDAS)
# ==========================
data = {
    "question": [
        "What is the capital of India?",
        "Who created Python?",
        "What is 10 + 15?",
        "Which is the Red Planet?",
        "Which one is NOT a programming language?"
    ],

    "A": ["Mumbai", "James Gosling", "20", "Earth", "Python"],
    "B": ["New Delhi", "Guido van Rossum", "25", "Mars", "Java"],
    "C": ["Chennai", "Dennis Ritchie", "30", "Jupiter", "HTML"],
    "D": ["Kolkata", "Elon Musk", "35", "Venus", "C"],

    "answer": ["B", "B", "B", "B", "C"]
}

df = pd.DataFrame(data)

# Shuffle questions using numpy
question_order = np.arange(len(df))
np.random.shuffle(question_order)


# ==========================
#      START QUIZ
# ==========================
def start_quiz():
    score = 0

    print("\n📘 Welcome to the Multiple Choice Quiz!")
    print("⏳ Total time: 60 seconds\n")

    timer = threading.Thread(target=countdown, args=(60,))
    timer.daemon = True
    timer.start()

    for i in question_order:
        if time_up:
            break

        print("\n" + df.loc[i, "question"])
        print("A.", df.loc[i, "A"])
        print("B.", df.loc[i, "B"])
        print("C.", df.loc[i, "C"])
        print("D.", df.loc[i, "D"])

        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == df.loc[i, "answer"]:
            score += 1

    print("\n🎉 Quiz Finished!")
    print(f"Your Score: {score}/{len(df)}")


start_quiz()
