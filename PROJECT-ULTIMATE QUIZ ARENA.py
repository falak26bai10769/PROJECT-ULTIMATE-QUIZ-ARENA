# ULTIMATE QUIZ ARENA - Beginner Level Quiz Project

import random

player = {
    "name": "Player",
    "score": 0,
    "xp": 0,
    "level": 1,
    "correct": 0,
    "wrong": 0,
    "questions": 0,
    "streak": 0,
    "best_streak": 0,
    "quizzes": 0,
    "games": 0,
    "coins": 20,
    "boss": 0,
    "tournament": 0,
    "daily": False,
    "perfect": 0,
    "achievements": [],
    "powerups": {"50/50": 2, "Hint": 2, "Phone": 2, "Skip": 1,
                 "Double": 1, "Shield": 1}
}

scores = []

qbank = {
    'Python': {
        'Easy': [
            ("What is the output of print(3 * 'Hi')?", ['HiHiHi', '3Hi', 'Hi3', 'Error'], 'A', 'A string can be repeated with the * operator.'),
            ('Which data type stores unique values?', ['List', 'Tuple', 'Set', 'String'], 'C', 'A set stores unique elements.'),
            ('What does len([4, 8, 12, 16]) return?', ['3', '4', '5', '16'], 'B', 'There are four elements in the list.')
        ],
        'Medium': [
            ('x=[10,20]; y=x; y.append(30); print(x)', ['[10,20]', '[30]', '[10,20,30]', 'Error'], 'C', 'x and y refer to the same list object.'),
            ('What does [x*2 for x in [1,2,3]] produce?', ['[1,2,3]', '[2,4,6]', '[1,4,9]', 'Error'], 'B', 'The comprehension doubles every element.'),
            ('Which creates a shallow copy of list a?', ['b=a', 'b=a[:]', 'b==a', 'a.copy(deep=True)'], 'B', 'Slicing creates a shallow list copy.')
        ],
        'Hard': [
            ('What is printed by: a=[1]; b=a.copy(); b.append(2); print(a,b)?', ['[1] [1,2]', '[1,2] [1,2]', '[1] [2]', 'Error'], 'A', 'copy() creates a separate outer list.'),
            ("d={'a':10}; print(d.get('b',0)+d['a']) gives:", ['0', '10', '20', 'Error'], 'B', 'The missing key returns 0, so 0+10=10.'),
            ('What does a function return when it reaches return without a value?', ['0', 'False', 'None', 'Error'], 'C', 'A bare return produces None.')
        ]
    },
    'Mathematics': {
        'Easy': [
            ('What is 12 × 8?', ['86', '96', '108', '112'], 'B', '12×8=96.'),
            ('What is √144?', ['10', '11', '12', '14'], 'C', '12×12=144.'),
            ('What is 25% of 200?', ['25', '40', '50', '75'], 'C', '25% is one fourth, so the answer is 50.')
        ],
        'Medium': [
            ('If 3x=27, what is x?', ['6', '8', '9', '12'], 'C', '27÷3=9.'),
            ('What is the derivative of x²?', ['x', '2x', 'x²', '2'], 'B', 'By the power rule, d(x²)/dx=2x.'),
            ('What is the average of 10,20,30?', ['15', '20', '25', '30'], 'B', '60÷3=20.')
        ],
        'Hard': [
            ('What is ∫2x dx?', ['x²+C', '2x²+C', 'x+C', '2+C'], 'A', 'The integral of 2x is x²+C.'),
            ('If f(x)=x²+3x, what is f(2)?', ['8', '10', '12', '14'], 'B', '4+6=10.'),
            ('Determinant of [[2,1],[3,4]] is:', ['5', '6', '8', '11'], 'A', '2×4−1×3=5.')
        ]
    },
    'Science': {
        'Easy': [
            ('Which gas do plants mainly use in photosynthesis?', ['Oxygen', 'Nitrogen', 'Carbon dioxide', 'Hydrogen'], 'C', 'Plants use carbon dioxide.'),
            ('What is H₂O?', ['Hydrogen', 'Water', 'Oxygen', 'Salt'], 'B', 'H₂O is water.'),
            ('Which organ pumps blood?', ['Lung', 'Brain', 'Heart', 'Kidney'], 'C', 'The heart pumps blood.')
        ],
        'Medium': [
            ('SI unit of electric current?', ['Volt', 'Ohm', 'Ampere', 'Watt'], 'C', 'Current is measured in amperes.'),
            ('Which particle has a negative charge?', ['Proton', 'Neutron', 'Electron', 'Nucleus'], 'C', 'Electrons carry negative charge.'),
            ('Boiling point of water at standard pressure?', ['50°C', '90°C', '100°C', '120°C'], 'C', 'It is 100°C at standard pressure.')
        ],
        'Hard': [
            ('Which law states V=IR?', ["Newton's law", "Ohm's law", "Boyle's law", "Hooke's law"], 'B', "Ohm's law relates voltage, current and resistance."),
            ('Which organelle is strongly associated with ATP production?', ['Ribosome', 'Nucleus', 'Mitochondrion', 'Golgi body'], 'C', 'Mitochondria generate much cellular ATP.'),
            ('Which bond involves sharing electrons?', ['Ionic', 'Covalent', 'Metallic', 'Hydrogen'], 'B', 'Covalent bonds involve shared electron pairs.')
        ]
    },
    'General Knowledge': {
        'Easy': [
            ('What is the capital of India?', ['Mumbai', 'New Delhi', 'Kolkata', 'Chennai'], 'B', "New Delhi is India's capital."),
            ('How many days are in a leap year?', ['365', '366', '364', '360'], 'B', 'A leap year has 366 days.'),
            ('Which is the largest planet?', ['Earth', 'Mars', 'Jupiter', 'Venus'], 'C', 'Jupiter is the largest planet.')
        ],
        'Medium': [
            ('Which metal is liquid near room temperature?', ['Iron', 'Copper', 'Mercury', 'Aluminium'], 'C', 'Mercury is liquid near typical room temperature.'),
            ('Which ocean is the deepest?', ['Atlantic', 'Indian', 'Pacific', 'Arctic'], 'C', 'The Pacific contains the Mariana Trench.'),
            ('Which country is known as the Land of the Rising Sun?', ['China', 'Japan', 'Thailand', 'Korea'], 'B', 'Japan is traditionally called the Land of the Rising Sun.')
        ],
        'Hard': [
            ('Which strait separates India and Sri Lanka?', ['Bering Strait', 'Palk Strait', 'Malacca Strait', 'Bosporus'], 'B', 'The Palk Strait lies between India and Sri Lanka.'),
            ('Which layer contains most of the ozone?', ['Troposphere', 'Stratosphere', 'Mesosphere', 'Thermosphere'], 'B', 'Most atmospheric ozone is in the stratosphere.'),
            ('Which agreement is associated with limiting global temperature rise?', ['Paris Agreement', 'Kyoto Protocol only', 'Geneva Convention', 'Montreal Charter'], 'A', 'The Paris Agreement addresses climate change and temperature goals.')
        ]
    }
}



def title(text):
    print("\n" + "=" * 60)
    print(text.center(60))
    print("=" * 60)


def num(msg, low, high):
    while True:
        try:
            value = int(input(msg))
            if low <= value <= high:
                return value
            print("Enter a number from", low, "to", high)
        except ValueError:
            print("Please enter a number.")


def wait():
    input("\nPress Enter to continue...")


def level():
    player["level"] = player["xp"] // 100 + 1

    rules = [
        ("First Quiz", player["questions"] >= 1),
        ("Knowledge Seeker", player["correct"] >= 10),
        ("Hot Streak", player["best_streak"] >= 5),
        ("Quiz Regular", player["quizzes"] >= 3),
        ("Boss Winner", player["boss"] >= 1),
        ("Game Player", player["games"] >= 3),
        ("Perfect Round", player["perfect"] >= 1),
        ("Coin Collector", player["coins"] >= 50),
        ("Tournament Champion", player["tournament"] >= 1),
        ("Arena Legend", player["level"] >= 10)
    ]

    player["achievements"] = []
    for name, done in rules:
        if done:
            player["achievements"].append(name)


def choose_subject():
    subjects = list(qbank.keys())

    print("\nSUBJECT")
    for i in range(len(subjects)):
        print(i + 1, subjects[i])

    sub = subjects[num("Choose subject: ", 1, len(subjects)) - 1]

    levels = ["Easy", "Medium", "Hard"]
    print("\nDIFFICULTY")
    for i in range(3):
        print(i + 1, levels[i])

    diff = levels[num("Choose difficulty: ", 1, 3) - 1]
    return sub, diff


def ask(q, num, total, mode):
    text, opts, ans, exp = q

    print("\n" + mode.upper(), "- Question", num, "of", total)
    print(text)

    for i in range(4):
        print(chr(65 + i) + ".", opts[i])

    print("Power-ups: 50/50 | Hint | Phone | Skip | Double | Shield")

    while True:
        ch = input("Answer or power-up: ").strip().upper()

        if ch in ["A", "B", "C", "D"]:
            return ch, ""

        if ch == "50/50" and player["powerups"]["50/50"] > 0:
            wrong = [x for x in "ABCD" if x != ans]
            removed = random.sample(wrong, 2)
            print("Try not to choose:", removed[0], "or", removed[1])
            player["powerups"]["50/50"] -= 1

        elif ch == "HINT" and player["powerups"]["Hint"] > 0:
            print("Hint:", exp.split(".")[0])
            player["powerups"]["Hint"] -= 1

        elif ch == "PHONE" and player["powerups"]["Phone"] > 0:
            print("Friend thinks the answer is", ans)
            player["powerups"]["Phone"] -= 1

        elif ch == "SKIP" and player["powerups"]["Skip"] > 0:
            player["powerups"]["Skip"] -= 1
            return "SKIP", ""

        elif ch == "DOUBLE" and player["powerups"]["Double"] > 0:
            player["powerups"]["Double"] -= 1
            print("Double points activated!")
            return input("Answer A/B/C/D: ").strip().upper(), "DOUBLE"

        elif ch == "SHIELD" and player["powerups"]["Shield"] > 0:
            player["powerups"]["Shield"] -= 1
            print("Shield activated!")
            return input("Answer A/B/C/D: ").strip().upper(), "SHIELD"

        else:
            print("Enter A, B, C, D or a valid power-up.")


def quiz(mode="Classic", count=5, lives=None):
    title(mode)

    if mode == "Category Mix":
        qs = []
        for i in range(count):
            sub = random.choice(list(qbank.keys()))
            diff = random.choice(["Easy", "Medium", "Hard"])
            qs.append(random.choice(qbank[sub][diff]))
    else:
        sub, diff = choose_subject()
        qs = random.sample(
            qbank[sub][diff],
            min(count, len(qbank[sub][diff]))
        )

    player["quizzes"] += 1
    right = 0
    pts = 0

    for num, q in enumerate(qs, 1):
        ans, use = ask(q, num, len(qs), mode)

        if ans == "SKIP":
            print("Skipped.")
            continue

        if ans == q[2]:
            if mode == "Rapid Fire":
                earned = 30
            else:
                earned = 20

            if use == "DOUBLE":
                earned *= 2

            player["correct"] += 1
            player["questions"] += 1
            player["streak"] += 1
            player["best_streak"] = max(player["best_streak"], player["streak"])
            player["score"] += earned
            player["xp"] += earned
            player["coins"] += max(1, earned // 10)
            right += 1
            pts += earned

            print("Correct! +", earned, "points")
        else:
            player["wrong"] += 1
            player["questions"] += 1

            if use != "SHIELD":
                player["streak"] = 0
                if lives is not None:
                    lives -= 1

            print("Wrong. Correct answer:", q[2])

        print("Explanation:", q[3])

        if lives is not None:
            print("Lives left:", lives)
            if lives <= 0:
                break

    if right == len(qs):
        player["perfect"] += 1
        player["score"] += 50
        player["xp"] += 50
        player["coins"] += 10
        print("Perfect round! +50 points")

    level()
    print("\nResult:", right, "correct")
    print("Round points:", pts)
    wait()
    return right


def modes():
    while True:
        title("QUIZ MODES")
        print("1. Classic Quiz")
        print("2. Rapid Fire")
        print("3. Survival")
        print("4. Daily Challenge")
        print("5. Boss Battle")
        print("6. Tournament")
        print("7. Category Mix")
        print("8. Return")

        ch = num("Choose: ", 1, 8)

        if ch == 8:
            break

        if ch == 1:
            quiz("Classic", 5)

        elif ch == 2:
            quiz("Rapid Fire", 5)

        elif ch == 3:
            quiz("Survival", 10, 3)

        elif ch == 4:
            if player["daily"]:
                print("Daily challenge already completed.")
            else:
                quiz("Daily Challenge", 5)
                player["daily"] = True
                player["score"] += 25
                player["xp"] += 25
                player["coins"] += 5
                print("Daily bonus: +25 points")
                level()
            wait()

        elif ch == 5:
            right = quiz("Boss Battle", 5)
            if right >= 4:
                player["boss"] += 1
                player["score"] += 100
                player["xp"] += 100
                player["coins"] += 20
                print("Boss defeated! +100 points")
                level()
            wait()

        elif ch == 6:
            print("\nTOURNAMENT")
            quiz("Qualifier", 3)
            quiz("Semi-Final", 3)
            quiz("Final", 3)
            player["tournament"] += 1
            player["score"] += 100
            player["xp"] += 100
            player["coins"] += 30
            print("Tournament completed! +100 points")
            level()
            wait()

        elif ch == 7:
            quiz("Category Mix", 6)


def games():
    while True:
        title("GAME HUB")
        print("1. Quick Math")
        print("2. Number Hunt")
        print("3. Rock Paper Scissors")
        print("4. Return")

        ch = num("Choose: ", 1, 4)

        if ch == 4:
            break

        player["games"] += 1

        if ch == 1:
            a = random.randint(5, 20)
            b = random.randint(2, 10)
            op = random.choice(["+", "-", "*"])
            ans = a + b if op == "+" else a - b if op == "-" else a * b

            try:
                user = int(input("Solve " + str(a) + " " + op + " " + str(b) + ": "))
                if user == ans:
                    player["score"] += 20
                    player["xp"] += 20
                    player["coins"] += 2
                    print("Correct! +20 points")
                else:
                    print("Correct answer:", ans)
            except ValueError:
                print("Please enter a number.")

        elif ch == 2:
            secret = random.randint(1, 50)
            won = False

            for i in range(6):
                guess = num("Guess 1-50: ", 1, 50)

                if guess == secret:
                    won = True
                    player["score"] += 30
                    player["xp"] += 30
                    player["coins"] += 3
                    print("You found it! +30 points")
                    break

                print("Higher." if guess < secret else "Lower.")

            if not won:
                print("The number was", secret)

        else:
            choices = ["rock", "paper", "scissors"]
            user = input("rock, paper or scissors: ").lower().strip()

            if user not in choices:
                print("Invalid choice.")
            else:
                computer = random.choice(choices)
                print("Computer:", computer)

                if user == computer:
                    print("Draw!")
                elif ((user == "rock" and computer == "scissors") or
                      (user == "paper" and computer == "rock") or
                      (user == "scissors" and computer == "paper")):
                    player["score"] += 15
                    player["xp"] += 15
                    player["coins"] += 2
                    print("You win! +15 points")
                else:
                    print("Computer wins.")

        level()
        wait()


def shop():
    items = [
        ("50/50", 20), ("Hint", 15), ("Phone", 20),
        ("Skip", 25), ("Double", 35), ("Shield", 40)
    ]

    while True:
        title("ARENA SHOP")
        print("Coins:", player["coins"])

        for i, item in enumerate(items, 1):
            name, price = item
            print(i, name, "-", price, "coins | Owned:", player["powerups"][name])

        print("7. Risk and Reward")
        print("8. Return")

        ch = num("Choose: ", 1, 8)

        if ch == 8:
            break

        if ch == 7:
            print("\n1. Safe   +10")
            print("2. Risky  +30 or 0")
            print("3. Extreme +70 or -20")

            risk = num("Choose risk: ", 1, 3)
            roll = random.randint(1, 100)

            if risk == 1:
                reward = 10
            elif risk == 2:
                reward = 30 if roll <= 60 else 0
            else:
                reward = 70 if roll <= 40 else -20

            player["score"] = max(0, player["score"] + reward)

            if reward > 0:
                player["xp"] += reward
                player["coins"] += max(1, reward // 10)

            print("Result:", reward, "points")
        else:
            name, price = items[ch - 1]

            if player["coins"] >= price:
                player["coins"] -= price
                player["powerups"][name] += 1
                print(name, "purchased!")
            else:
                print("Not enough coins.")

        level()
        wait()


def stats():
    level()
    title("PLAYER STATS")

    if player["questions"]:
        accuracy = player["correct"] / player["questions"] * 100
    else:
        accuracy = 0

    print("Name:", player["name"])
    print("Score:", player["score"])
    print("Level:", player["level"])
    print("XP:", player["xp"])
    print("Coins:", player["coins"])
    print("Accuracy:", round(accuracy, 1), "%")
    print("Correct:", player["correct"])
    print("Wrong:", player["wrong"])
    print("Best streak:", player["best_streak"])
    print("Quizzes:", player["quizzes"])
    print("Mini-games:", player["games"])
    print("Boss wins:", player["boss"])
    print("Tournament wins:", player["tournament"])

    print("\nPower-ups:")
    for name, count in player["powerups"].items():
        print(name, ":", count)

    wait()


def achieve():
    level()
    title("ACHIEVEMENTS")

    names = [
        "First Quiz", "Knowledge Seeker", "Hot Streak",
        "Quiz Regular", "Boss Winner", "Game Player",
        "Perfect Round", "Coin Collector", "Tournament Champion",
        "Arena Legend"
    ]

    for name in names:
        if name in player["achievements"]:
            print("[Unlocked]", name)
        else:
            print("[Locked]  ", name)

    wait()


def board():
    title("SESSION LEADERBOARD")

    temp = scores + [(player["name"], player["score"])]
    temp.sort(key=lambda x: x[1], reverse=True)

    for i, item in enumerate(temp[:10], 1):
        print(i, item[0], "-", item[1], "points")

    wait()


def help():
    title("ARENA GUIDE")
    print("Classic Quiz    - normal quiz")
    print("Rapid Fire      - extra points")
    print("Survival        - 3 lives")
    print("Daily Challenge - one challenge per session")
    print("Boss Battle     - hard questions and reward")
    print("Tournament      - three stages")
    print("Category Mix    - random subjects and levels")
    print("Game Hub        - three mini-games")
    print("Shop            - buy power-ups")
    print("Risk and Reward - chance for more points")
    print("\nPower-ups: 50/50, Hint, Phone, Skip, Double, Shield")
    print("Scores stay only while the program is running.")
    wait()


def main():
    title("ULTIMATE QUIZ ARENA")
    player["name"] = input("Enter your name: ").strip()

    if player["name"] == "":
        player["name"] = "Player"

    while True:
        level()

        print("\nPlayer:", player["name"],
              "| Level:", player["level"],
              "| Score:", player["score"],
              "| Coins:", player["coins"])

        print("\n1. Quiz Modes")
        print("2. Game Hub")
        print("3. Arena Shop")
        print("4. Player Stats")
        print("5. Achievements")
        print("6. Leaderboard")
        print("7. Arena Guide")
        print("8. Exit")

        ch = num("Choose: ", 1, 8)

        if ch == 1:
            modes()
        elif ch == 2:
            games()
        elif ch == 3:
            shop()
        elif ch == 4:
            stats()
        elif ch == 5:
            achieve()
        elif ch == 6:
            board()
        elif ch == 7:
            help()
        else:
            scores.append((player["name"], player["score"]))
            title("GAME OVER")
            print("Final score:", player["score"])
            print("Level:", player["level"])
            print("Coins:", player["coins"])
            print("Achievements:", len(player["achievements"]))
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
