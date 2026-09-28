#--------------------------------------------- ULTIMATE QUIZ ARENA---------------------------------------------------

import random
import time

player = {
    "name": "Player", "score": 0, "xp": 0, "level": 1,
    "correct": 0, "wrong": 0, "questions": 0, "streak": 0,
    "best_streak": 0, "quizzes": 0, "boss_wins": 0, "games": 0,
    "lifelines": 0, "phone_help": 0, "double_used": False,
    "achievements": [], "perfect_rounds": 0, "coins": 0,
    "tournament_wins": 0, "daily_done": False, "rounds_won": 0,
    "best_speed": None, "total_time": 0, "questions_answered": 0,
    "powerups": {"50/50": 2, "Hint": 2, "Phone": 2, "Skip": 1, "Double": 1, "Shield": 1}
}

leaderboard = []

questions = {
    "Python": {
        "Easy": [
            ("What is the output of print(3 * 'Hi')?", ["HiHiHi", "3Hi", "Hi3", "Error"], "A", "A string can be repeated with the * operator."),
            ("Which data type stores unique values?", ["List", "Tuple", "Set", "String"], "C", "A set stores unique elements."),
            ("What does len([4, 8, 12, 16]) return?", ["3", "4", "5", "16"], "B", "There are four elements in the list."),
            ("Which operator checks equality?", ["=", "==", "!=", "=>"], "B", "== compares two values."),
            ("Which keyword defines a function?", ["func", "define", "def", "function"], "C", "Python uses def to define functions."),
            ("What is the first index of a Python list?", ["0", "1", "-1", "It depends"], "A", "Python uses zero-based indexing."),
            ("Which function displays output?", ["input()", "show()", "print()", "display()"], "C", "print() displays information on the screen."),
            ("Which symbol starts a Python comment?", ["//", "#", "/*", "--"], "B", "Python comments begin with #."),
            ("What type is the value True?", ["int", "str", "bool", "float"], "C", "True and False are Boolean values."),
            ("Which method adds one item to the end of a list?", ["add()", "push()", "append()", "insertEnd()"], "C", "append() adds an item at the end.")
        ],
        "Medium": [
            ("x=[10,20]; y=x; y.append(30); print(x)", ["[10,20]", "[30]", "[10,20,30]", "Error"], "C", "x and y refer to the same list object."),
            ("What does [x*2 for x in [1,2,3]] produce?", ["[1,2,3]", "[2,4,6]", "[1,4,9]", "Error"], "B", "The comprehension doubles every element."),
            ("Which creates a shallow copy of list a?", ["b=a", "b=a[:]", "b==a", "a.copy(deep=True)"], "B", "Slicing creates a shallow list copy."),
            ("What does range(2, 8, 2) produce?", ["2,4,6", "2,4,6,8", "1,3,5,7", "2,3,4,5,6,7"], "A", "The stop value 8 is excluded."),
            ("What is the result of 17 // 5?", ["2", "3", "3.4", "4"], "B", "// performs floor division."),
            ("Which statement safely handles an exception?", ["if/else", "try/except", "for/while", "def/return"], "B", "try/except handles runtime exceptions."),
            ("What does dictionary.get('x', 0) return if x is absent?", ["None only", "0", "Error", "x"], "B", "get() can return a default value."),
            ("What is len({'a':1,'b':2,'c':3})?", ["2", "3", "4", "6"], "B", "A dictionary has three key-value pairs."),
            ("What does enumerate(['a','b']) provide?", ["Only values", "Only indexes", "Indexes and values", "Keys and values"], "C", "enumerate() yields index-value pairs."),
            ("Which is immutable?", ["List", "Set", "Dictionary", "Tuple"], "D", "Tuples cannot be changed after creation.")
        ],
        "Hard": [
            ("What is printed by: a=[1]; b=a.copy(); b.append(2); print(a,b)?", ["[1] [1,2]", "[1,2] [1,2]", "[1] [2]", "Error"], "A", "copy() creates a separate outer list."),
            ("d={'a':10}; print(d.get('b',0)+d['a']) gives:", ["0", "10", "20", "Error"], "B", "The missing key returns 0, so 0+10=10."),
            ("What does a function return when it reaches return without a value?", ["0", "False", "None", "Error"], "C", "A bare return produces None."),
            ("What is the output of print([i for i in range(6) if i % 2 == 0])?", ["[1,3,5]", "[0,2,4]", "[2,4,6]", "[]"], "B", "The condition keeps even numbers from 0 through 5."),
            ("Which statement about a shallow copy is correct?", ["Nested objects are always copied", "Only the outer container is copied", "Nothing is copied", "It converts a list to a tuple"], "B", "Nested mutable objects may still be shared."),
            ("What is the value of bool([])?", ["True", "False", "None", "Error"], "B", "Empty containers are falsy."),
            ("What does *args collect in a function?", ["Keyword arguments", "Positional arguments", "Only strings", "Return values"], "B", "*args collects extra positional arguments."),
            ("Which data structure is best suited for key-based lookup?", ["Dictionary", "Tuple", "String", "Float"], "A", "Dictionaries map keys to values."),
            ("If a=[1,2,3], what is a[-1]?", ["1", "2", "3", "Error"], "C", "-1 refers to the last element."),
            ("What does sorted([3,1,2], reverse=True) return?", ["[1,2,3]", "[3,2,1]", "(3,2,1)", "Error"], "B", "sorted() returns a new list in descending order.")
        ]
    },
    "Mathematics": {
        "Easy": [
            ("What is 12 × 8?", ["86", "96", "108", "112"], "B", "12×8=96."),
            ("What is √144?", ["10", "11", "12", "14"], "C", "12×12=144."),
            ("What is 25% of 200?", ["25", "40", "50", "75"], "C", "25% is one fourth, so the answer is 50."),
            ("What is 7²?", ["14", "21", "49", "56"], "C", "7×7=49."),
            ("What is 15 + 27?", ["32", "40", "42", "44"], "C", "15+27=42."),
            ("What is 3/4 as a percentage?", ["25%", "50%", "75%", "80%"], "C", "3/4 = 0.75 = 75%."),
            ("What is the perimeter of a square of side 6 cm?", ["12 cm", "18 cm", "24 cm", "36 cm"], "C", "Perimeter=4×side=24 cm."),
            ("What is 2⁵?", ["10", "16", "25", "32"], "D", "2×2×2×2×2=32."),
            ("What is the next prime after 7?", ["8", "9", "10", "11"], "D", "11 is the next prime number."),
            ("What is 0.5 × 20?", ["5", "10", "15", "20"], "B", "Half of 20 is 10.")
        ],
        "Medium": [
            ("If 3x=27, what is x?", ["6", "8", "9", "12"], "C", "27÷3=9."),
            ("What is the derivative of x²?", ["x", "2x", "x²", "2"], "B", "By the power rule, d(x²)/dx=2x."),
            ("What is the average of 10,20,30?", ["15", "20", "25", "30"], "B", "60÷3=20."),
            ("What is 2³+3²?", ["13", "15", "17", "18"], "C", "8+9=17."),
            ("Solve: 2x+5=17.", ["5", "6", "7", "8"], "B", "2x=12, so x=6."),
            ("What is the slope of y=3x+2?", ["2", "3", "5", "-3"], "B", "The coefficient of x is the slope."),
            ("What is the area of a triangle with base 10 and height 6?", ["16", "30", "60", "120"], "B", "Area=1/2×10×6=30."),
            ("What is 15% of 80?", ["8", "10", "12", "15"], "C", "0.15×80=12."),
            ("If a:b=2:3 and a=10, b is:", ["12", "15", "20", "30"], "B", "The scale factor is 5, so b=15."),
            ("What is the median of 3,7,9,12,15?", ["7", "8", "9", "12"], "C", "The middle value is 9.")
        ],
        "Hard": [
            ("What is ∫2x dx?", ["x²+C", "2x²+C", "x+C", "2+C"], "A", "The integral of 2x is x²+C."),
            ("If f(x)=x²+3x, what is f(2)?", ["8", "10", "12", "14"], "B", "4+6=10."),
            ("Determinant of [[2,1],[3,4]] is:", ["5", "6", "8", "11"], "A", "2×4−1×3=5."),
            ("What is log₁₀(1000)?", ["2", "3", "10", "100"], "B", "10³=1000."),
            ("Solve x²−5x+6=0.", ["1,6", "2,3", "-2,-3", "3,4"], "B", "(x−2)(x−3)=0."),
            ("What is the derivative of sin(x)?", ["cos(x)", "-cos(x)", "sin(x)", "-sin(x)"], "A", "The derivative of sin(x) is cos(x)."),
            ("If vectors are perpendicular, their dot product is:", ["1", "−1", "0", "Their magnitudes"], "C", "Perpendicular vectors have dot product zero."),
            ("What is the probability of getting two heads in two fair coin tosses?", ["1/2", "1/3", "1/4", "3/4"], "C", "Only HH works out of four equally likely outcomes."),
            ("The eigenvalues of an identity matrix are:", ["0 only", "1 only", "−1 only", "Any integer"], "B", "Every eigenvalue of I is 1."),
            ("What is lim(x→0) sin(x)/x?", ["0", "1", "∞", "Does not exist"], "B", "The standard trigonometric limit equals 1.")
        ]
    },
    "Science": {
        "Easy": [
            ("Which gas do plants mainly use in photosynthesis?", ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"], "C", "Plants use carbon dioxide."),
            ("What is H₂O?", ["Hydrogen", "Water", "Oxygen", "Salt"], "B", "H₂O is water."),
            ("Which organ pumps blood?", ["Lung", "Brain", "Heart", "Kidney"], "C", "The heart pumps blood."),
            ("What force pulls objects toward Earth?", ["Friction", "Gravity", "Magnetism", "Pressure"], "B", "Gravity attracts masses toward Earth."),
            ("What is the basic unit of life?", ["Atom", "Cell", "Tissue", "Organ"], "B", "The cell is the basic unit of life."),
            ("Which planet is closest to the Sun?", ["Earth", "Mars", "Mercury", "Venus"], "C", "Mercury is closest."),
            ("What is the chemical symbol for oxygen?", ["Ox", "O", "O2", "Og"], "B", "O is the element symbol."),
            ("Which state has a fixed volume but no fixed shape?", ["Solid", "Liquid", "Gas", "Plasma"], "B", "A liquid takes the shape of its container."),
            ("Which vitamin is commonly produced in skin with sunlight exposure?", ["Vitamin A", "Vitamin B12", "Vitamin C", "Vitamin D"], "D", "Sunlight supports vitamin D production."),
            ("What instrument measures temperature?", ["Barometer", "Thermometer", "Ammeter", "Voltmeter"], "B", "A thermometer measures temperature.")
        ],
        "Medium": [
            ("SI unit of electric current?", ["Volt", "Ohm", "Ampere", "Watt"], "C", "Current is measured in amperes."),
            ("Which particle has a negative charge?", ["Proton", "Neutron", "Electron", "Nucleus"], "C", "Electrons carry negative charge."),
            ("Boiling point of water at standard pressure?", ["50°C", "90°C", "100°C", "120°C"], "C", "It is 100°C at standard pressure."),
            ("Liquid water changing to vapour is:", ["Condensation", "Evaporation", "Freezing", "Melting"], "B", "Evaporation changes liquid to gas."),
            ("Which blood cells help fight infection?", ["Red blood cells", "White blood cells", "Platelets", "Plasma only"], "B", "White blood cells are involved in immune defence."),
            ("Which gas is most abundant in Earth's atmosphere?", ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"], "B", "Nitrogen makes up most of the atmosphere."),
            ("What is the pH of a neutral solution at 25°C?", ["0", "5", "7", "14"], "C", "Neutral water has pH 7 at 25°C."),
            ("Which energy source is renewable?", ["Coal", "Petroleum", "Solar", "Natural gas"], "C", "Solar energy is renewable."),
            ("What does DNA primarily store?", ["Heat", "Genetic information", "Oxygen", "Water"], "B", "DNA carries genetic information."),
            ("Which lens is thicker at the centre than the edges?", ["Concave", "Convex", "Plane", "Cylindrical only"], "B", "A convex lens bulges outward.")
        ],
        "Hard": [
            ("Which law states V=IR?", ["Newton's law", "Ohm's law", "Boyle's law", "Hooke's law"], "B", "Ohm's law relates voltage, current and resistance."),
            ("Which organelle is strongly associated with ATP production?", ["Ribosome", "Nucleus", "Mitochondrion", "Golgi body"], "C", "Mitochondria generate much cellular ATP."),
            ("Which bond involves sharing electrons?", ["Ionic", "Covalent", "Metallic", "Hydrogen"], "B", "Covalent bonds involve shared electron pairs."),
            ("Acceleration is:", ["Change in velocity per unit time", "Distance only", "Mass per volume", "Force only"], "A", "Acceleration is the rate of change of velocity."),
            ("Which principle explains pressure transmission in a confined fluid?", ["Pascal's law", "Newton's third law", "Hooke's law", "Faraday's law"], "A", "Pascal's principle describes pressure transmission in confined fluids."),
            ("What is the oxidation state of oxygen in H₂O?", ["+2", "−2", "0", "+1"], "B", "Hydrogen is +1, so oxygen is −2 overall."),
            ("Which process produces ATP without oxygen in cells?", ["Anaerobic respiration", "Photosynthesis only", "Transpiration", "Diffusion"], "A", "Anaerobic pathways can generate ATP without oxygen."),
            ("If wavelength decreases while wave speed stays constant, frequency:", ["Decreases", "Increases", "Becomes zero", "Stays unrelated"], "B", "From v=fλ, frequency rises when wavelength falls at fixed speed."),
            ("Which particle determines an element's atomic number?", ["Neutron", "Electron", "Proton", "Photon"], "C", "Atomic number equals the number of protons."),
            ("In an exothermic reaction, heat is generally:", ["Absorbed", "Released", "Destroyed", "Converted only to mass"], "B", "Exothermic reactions release heat to the surroundings.")
        ]
    },
    "General Knowledge": {
        "Easy": [
            ("What is the capital of India?", ["Mumbai", "New Delhi", "Kolkata", "Chennai"], "B", "New Delhi is India's capital."),
            ("How many days are in a leap year?", ["365", "366", "364", "360"], "B", "A leap year has 366 days."),
            ("Which is the largest planet?", ["Earth", "Mars", "Jupiter", "Venus"], "C", "Jupiter is the largest planet."),
            ("How many continents are commonly taught?", ["5", "6", "7", "8"], "C", "The commonly taught model has seven continents."),
            ("Which is the largest ocean?", ["Atlantic", "Indian", "Arctic", "Pacific"], "D", "The Pacific is the largest ocean."),
            ("Which currency is used in Japan?", ["Won", "Yuan", "Yen", "Ringgit"], "C", "Japan uses the yen."),
            ("Which is the fastest land animal?", ["Lion", "Cheetah", "Horse", "Tiger"], "B", "The cheetah is the fastest land animal."),
            ("Which language has the largest number of native speakers?", ["English", "Spanish", "Mandarin Chinese", "French"], "C", "Mandarin Chinese has the largest native-speaker population."),
            ("Which planet is famous for its prominent rings?", ["Mercury", "Saturn", "Mars", "Earth"], "B", "Saturn has a prominent ring system."),
            ("Which direction does the Sun appear to rise from?", ["North", "South", "East", "West"], "C", "The Sun appears to rise in the east.")
        ],
        "Medium": [
            ("Which metal is liquid near room temperature?", ["Iron", "Copper", "Mercury", "Aluminium"], "C", "Mercury is liquid near typical room temperature."),
            ("Which ocean is the deepest?", ["Atlantic", "Indian", "Pacific", "Arctic"], "C", "The Pacific contains the Mariana Trench."),
            ("Which country is known as the Land of the Rising Sun?", ["China", "Japan", "Thailand", "Korea"], "B", "Japan is traditionally called the Land of the Rising Sun."),
            ("Which is the smallest prime number?", ["0", "1", "2", "3"], "C", "2 is the smallest prime."),
            ("Which instrument measures atmospheric pressure?", ["Thermometer", "Barometer", "Hygrometer", "Ammeter"], "B", "A barometer measures pressure."),
            ("Which is the longest river in India by commonly cited geography references?", ["Ganga", "Narmada", "Godavari", "Kaveri"], "A", "The Ganga is commonly identified as India's longest river."),
            ("What does UNESCO stand for?", ["United Nations Educational, Scientific and Cultural Organization", "United Nations Energy Science Council", "Universal Education and Science Council", "United Nations Economic Society"], "A", "UNESCO is the UN agency named in option A."),
            ("Which city is known as India's Silicon Valley?", ["Pune", "Bengaluru", "Jaipur", "Lucknow"], "B", "Bengaluru is widely known by this nickname."),
            ("Which is the largest desert in the world by area?", ["Sahara", "Gobi", "Antarctic Desert", "Arabian"], "C", "Antarctica is classified as the world's largest desert."),
            ("Which Indian space agency is ISRO?", ["Indian Space Research Organisation", "Indian Satellite Research Office", "International Space Research Organisation", "Indian Science Research Organisation"], "A", "ISRO expands to Indian Space Research Organisation.")
        ],
        "Hard": [
            ("Which strait separates India and Sri Lanka?", ["Bering Strait", "Palk Strait", "Malacca Strait", "Bosporus"], "B", "The Palk Strait lies between India and Sri Lanka."),
            ("Which layer contains most of the ozone?", ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere"], "B", "Most atmospheric ozone is in the stratosphere."),
            ("Which agreement is associated with limiting global temperature rise?", ["Paris Agreement", "Kyoto Protocol only", "Geneva Convention", "Montreal Charter"], "A", "The Paris Agreement addresses climate change and temperature goals."),
            ("What is the SI base unit of luminous intensity?", ["Lumen", "Lux", "Candela", "Watt"], "C", "Candela is the SI base unit of luminous intensity."),
            ("Which ancient civilization developed cuneiform writing?", ["Sumerians", "Romans", "Vikings", "Aztecs"], "A", "Cuneiform is strongly associated with ancient Mesopotamia and the Sumerians."),
            ("Which Indian classical dance originated in Kerala?", ["Kathak", "Bharatanatyam", "Kathakali", "Odissi"], "C", "Kathakali originated in Kerala."),
            ("What does GDP measure broadly?", ["A country's total final output/income measure", "Only exports", "Only government spending", "Population density"], "A", "GDP is a broad measure of economic production."),
            ("Which planet has the shortest orbital period around the Sun?", ["Earth", "Mars", "Mercury", "Venus"], "C", "Mercury completes an orbit in about 88 Earth days."),
            ("Which branch of government interprets laws in many constitutional systems?", ["Judiciary", "Legislature", "Executive", "Election commission"], "A", "The judiciary generally interprets and applies laws."),
            ("What is the study of earthquakes called?", ["Ecology", "Seismology", "Meteorology", "Geology of fossils"], "B", "Seismology studies earthquakes and seismic waves.")
        ]
    }
}


def line(char="═", width=72):
    print(char * width)

def title(text, subtitle=""):
    print("\n╔" + "═" * 70 + "╗")
    print("║" + text.center(70) + "║")
    print("╠" + "═" * 70 + "╣")
    if subtitle:
        for part in subtitle.split("\n"):
            print("║" + part.center(70) + "║")
        print("╚" + "═" * 70 + "╝")
    else:
        print("╚" + "═" * 70 + "╝")

def pause():
    input("\nPress ENTER to continue...")

def get_int(msg, low, high):
    while True:
        try:
            n = int(input(msg))
            if low <= n <= high:
                return n
            print(f"Please enter a number from {low} to {high}.")
        except ValueError:
            print("Please enter a valid number.")

def update_level():
    old = player["level"]
    player["level"] = player["xp"] // 100 + 1
    if player["level"] > old:
        print(f"\n★ LEVEL UP! You reached Level {player['level']}! ★")
        player["coins"] += 10
        print("Reward: +10 coins")

def progress_bar(value, maximum, width=24):
    if maximum <= 0:
        return "[" + "-" * width + "]"
    filled = int(width * min(value, maximum) / maximum)
    return "[" + "█" * filled + "░" * (width - filled) + "]"

def add_result(correct, points):
    player["questions"] += 1
    player["questions_answered"] += 1
    if correct:
        player["correct"] += 1
        player["score"] += points
        player["xp"] += points
        player["coins"] += max(1, points // 10)
        player["streak"] += 1
        player["best_streak"] = max(player["best_streak"], player["streak"])
        player["rounds_won"] += 1
    else:
        player["wrong"] += 1
        player["streak"] = 0
    update_level()

def check_achievements():
    rules = [
        ("First Quiz", player["questions"] >= 1),
        ("Knowledge Seeker", player["correct"] >= 10),
        ("Hot Streak", player["best_streak"] >= 5),
        ("Quiz Regular", player["quizzes"] >= 3),
        ("Boss Winner", player["boss_wins"] >= 1),
        ("Game Player", player["games"] >= 3),
        ("Perfect Round", player["perfect_rounds"] >= 1),
        ("Coin Collector", player["coins"] >= 50),
        ("Tournament Champion", player["tournament_wins"] >= 1),
        ("Streak Master", player["best_streak"] >= 10),
        ("Century Club", player["questions"] >= 100),
        ("Accuracy Ace", player["questions"] >= 20 and player["correct"] / player["questions"] >= .90),
        ("Arena Legend", player["level"] >= 10),
        ("All-Rounder", len(player["achievements"]) >= 10)
    ]
    player["achievements"] = [name for name, unlocked in rules if unlocked]

def choose_subject():
    names = list(questions.keys())
    print("\nSUBJECT SELECT")
    for i, name in enumerate(names, 1):
        print(f"  {i}. {name}")
    return names[get_int("\nChoose subject: ", 1, len(names)) - 1]

def choose_level():
    levels = ["Easy", "Medium", "Hard"]
    print("\nDIFFICULTY SELECT")
    print("  1. Easy    | Foundation")
    print("  2. Medium  | Application")
    print("  3. Hard    | Analysis")
    return levels[get_int("\nChoose difficulty: ", 1, 3) - 1]

def show_hud():
    needed = player["level"] * 100
    current = player["xp"] % 100
    print(f"Player: {player['name']}   Lv.{player['level']}   Score: {player['score']}   Coins: {player['coins']}")
    print(f"XP {progress_bar(current, 100)} {current}/100   Streak: {player['streak']}   Best: {player['best_streak']}")

def show_question(q, number, total, mode="Classic", use_lifeline=True):
    text, opts, answer, explanation = q
    print("\n┌" + "─" * 70 + "┐")
    print(f"│ {mode.upper():<18} QUESTION {number}/{total}" + " " * (70 - 18 - 11 - len(str(number)) - len(str(total))) + "│")
    print("├" + "─" * 70 + "┤")
    for part in textwrap_lines(text, 66):
        print("│ " + part.ljust(68) + "│")
    print("├" + "─" * 70 + "┤")
    for i, option in enumerate(opts):
        print(f"│   {chr(65+i)}. {option}".ljust(71) + "│")
    print("└" + "─" * 70 + "┘")
    if use_lifeline:
        print("L = Power-Up / Lifeline")
    while True:
        ans = input("\nYour answer: ").upper().strip()
        if ans in ["A", "B", "C", "D"]:
            return ans, False
        if ans == "L" and use_lifeline:
            result = lifeline(q)
            if result is not None:
                return result, True
        else:
            print("Enter A, B, C, D or L.")

def textwrap_lines(text, width):
    words = text.split()
    lines, current = [], ""
    for word in words:
        if len(current) + len(word) + 1 <= width:
            current = (current + " " + word).strip()
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines or [""]

def lifeline(q):
    text, opts, answer, explanation = q
    title("POWER-UP STATION", "Use your limited power-ups wisely")
    inventory = player["powerups"]
    print(f"1. 50/50        [{inventory['50/50']} available]")
    print(f"2. Hint         [{inventory['Hint']} available]")
    print(f"3. Phone Friend [{inventory['Phone']} available]")
    print(f"4. Skip         [{inventory['Skip']} available]")
    print(f"5. Double       [{inventory['Double']} available]")
    print(f"6. Shield       [{inventory['Shield']} available]")
    print("7. Cancel")
    c = get_int("\nChoose: ", 1, 7)
    if c == 7:
        return None
    names = {1: "50/50", 2: "Hint", 3: "Phone", 4: "Skip", 5: "Double", 6: "Shield"}
    name = names[c]
    if inventory[name] <= 0:
        print("You do not have that power-up.")
        return None
    inventory[name] -= 1
    player["lifelines"] += 1
    if name == "50/50":
        wrong = [x for x in "ABCD" if x != answer]
        keep = sorted([answer, random.choice(wrong)])
        print("\nTwo options remain:")
        for x in keep:
            print(x + ".", opts[ord(x)-65])
        while True:
            a = input("Answer: ").upper().strip()
            if a in keep:
                return a
            print("Choose one of the displayed options.")
    if name == "Hint":
        hints = [
            "Think about the definition or rule being tested.",
            "Eliminate the option that conflicts with the core concept.",
            "Look carefully at units, keywords, or boundary conditions."
        ]
        print("Hint:", random.choice(hints))
        return input("Answer: ").upper().strip()
    if name == "Phone":
        chance = 82 if player["level"] < 5 else 68
        guess = answer if random.randint(1, 100) <= chance else random.choice([x for x in "ABCD" if x != answer])
        player["phone_help"] += 1
        print("Your friend says:", guess, "but sounds", random.choice(["confident.", "unsure.", "surprisingly serious."]))
        return input("Your final answer: ").upper().strip()
    if name == "Skip":
        print("Question skipped. No points lost.")
        return "SKIP"
    if name == "Double":
        player["double_used"] = True
        print("DOUBLE activated! Your next correct answer earns 2× points.")
        return input("Your answer: ").upper().strip()
    if name == "Shield":
        player["shield_active"] = True
        print("SHIELD active: your next wrong answer will not break your streak.")
        return input("Your answer: ").upper().strip()

def host_comment(correct, streak, points=0):
    if correct:
        if streak >= 5:
            print("🔥 DOMINATING! The arena is officially nervous.")
        elif streak >= 3:
            print("⚡ COMBO BUILDING! Keep the streak alive.")
        else:
            print(random.choice(["✓ Clean hit!", "✓ Excellent!", "✓ Locked in!", "✓ That's the one!"]))
        if points >= 40:
            print("★ BIG REWARD! That answer was worth serious XP.")
    else:
        print(random.choice(["✗ Not this time. Reset and refocus.", "✗ The arena strikes back.", "✗ Close call. Learn it and move on."]))

def calculate_points(level, mode, streak, elapsed=0):
    base = {"Easy": 10, "Medium": 20, "Hard": 30}[level]
    mode_bonus = {"Classic": 0, "Rapid Fire": 10, "Tournament": 15, "Category Mix": 8}.get(mode, 0)
    streak_bonus = min(streak * 2, 20)
    speed_bonus = 10 if elapsed <= 5 else 5 if elapsed <= 10 else 0
    return base + mode_bonus + streak_bonus + speed_bonus

def run_round(selected, mode, level=None, lives=None, boss=False):
    round_score = 0
    correct_count = 0
    start_total = time.time()
    for i, q in enumerate(selected, 1):
        show_hud()
        before = time.time()
        ans, used = show_question(q, i, len(selected), mode)
        elapsed = time.time() - before
        player["total_time"] += elapsed
        if player["best_speed"] is None or elapsed < player["best_speed"]:
            player["best_speed"] = elapsed
        if ans == "SKIP":
            add_result(False, 0)
            print("Skipped. No points awarded.")
            continue
        correct = ans == q[2]
        shield_saved = False
        if correct:
            points = calculate_points(level or "Hard", mode, player["streak"], elapsed)
            if player.get("double_used"):
                points *= 2
                player["double_used"] = False
            add_result(True, points)
            round_score += points
            correct_count += 1
            print(f"✓ CORRECT   +{points} points   +{max(1, points//10)} coins")
            host_comment(True, player["streak"], points)
        else:
            shield_saved = bool(player.get("shield_active"))
            if shield_saved:
                player["shield_active"] = False
                print("SHIELD SAVED YOUR STREAK!")
                player["questions"] += 1
                player["wrong"] += 1
                print("Correct answer:", q[2])
            else:
                add_result(False, 0)
                print("✗ WRONG   Correct answer:", q[2])
            host_comment(False, player["streak"])
        print("Explanation:", q[3])
        if lives is not None and not correct and not shield_saved:
            lives -= 1
            print("Lives remaining:", lives)
            if lives <= 0:
                break
        if i < len(selected):
            print("\n" + "─" * 72)
    total_time = time.time() - start_total
    if correct_count == len(selected):
        player["perfect_rounds"] += 1
        bonus = 50
        player["score"] += bonus
        player["xp"] += bonus
        player["coins"] += 10
        update_level()
        print("\n★ PERFECT ROUND! +50 points +10 coins ★")
    return round_score, correct_count, lives, total_time

def quiz(mode="Classic"):
    player["double_used"] = False
    player["shield_active"] = False
    title("QUIZ ARENA", f"{mode} Mode")
    subject = choose_subject()
    level = choose_level()
    pool = questions[subject][level]
    selected = random.sample(pool, min(7 if mode == "Classic" else 5, len(pool)))
    player["quizzes"] += 1
    print(f"\n{subject} | {level} | {len(selected)} questions")
    score, correct, _, _ = run_round(selected, mode, level)
    check_achievements()
    print(f"\nROUND RESULT: {correct}/{len(selected)} correct | +{score} round points")
    pause()

def category_mix():
    title("CATEGORY MIX", "Every question can come from a different subject")
    levels = ["Easy", "Medium", "Hard"]
    selected = []
    for _ in range(8):
        subject = random.choice(list(questions.keys()))
        level = random.choice(levels)
        selected.append((subject, level, random.choice(questions[subject][level])))
    total = 0
    correct = 0
    player["quizzes"] += 1
    for i, (subject, level, q) in enumerate(selected, 1):
        print(f"\nCategory: {subject} | Difficulty: {level}")
        show_hud()
        before = time.time()
        ans, _ = show_question(q, i, len(selected), "Category Mix")
        elapsed = time.time() - before
        if ans == q[2]:
            pts = calculate_points(level, "Category Mix", player["streak"], elapsed)
            add_result(True, pts)
            total += pts
            correct += 1
            print("✓ Correct! +", pts)
        elif ans == "SKIP":
            add_result(False, 0)
            print("Skipped.")
        else:
            add_result(False, 0)
            print("✗ Correct answer:", q[2])
        print("Explanation:", q[3])
    print(f"\nMIX COMPLETE | {correct}/{len(selected)} correct | {total} points")
    check_achievements()
    pause()

def daily_challenge():
    if player["daily_done"]:
        print("\nDAILY CHALLENGE already completed in this session.")
        pause()
        return
    title("DAILY CHALLENGE", "One high-value challenge for the session")
    subject = random.choice(list(questions.keys()))
    pool = questions[subject]["Hard"]
    selected = random.sample(pool, min(5, len(pool)))
    player["quizzes"] += 1
    player["double_used"] = False
    score, correct, _, _ = run_round(selected, "Daily Challenge", "Hard")
    player["daily_done"] = True
    bonus = 75 if correct >= 4 else 25
    player["score"] += bonus
    player["xp"] += bonus
    player["coins"] += 15
    update_level()
    print(f"\nDAILY BONUS: +{bonus} points +15 coins")
    check_achievements()
    pause()

def survival():
    title("SURVIVAL MODE", "Three lives. Increasing pressure. No second chances.")
    subject = choose_subject()
    level = choose_level()
    pool = questions[subject][level]
    lives = 3
    player["quizzes"] += 1
    selected = [random.choice(pool) for _ in range(10)]
    score, correct, lives, _ = run_round(selected, "Survival", level, lives)
    if lives and correct >= 7:
        bonus = 75
        player["score"] += bonus
        player["xp"] += bonus
        player["coins"] += 15
        update_level()
        print("\nSURVIVAL MASTER BONUS: +75 points +15 coins")
    print(f"\nSURVIVAL RESULT | Correct: {correct} | Lives: {lives}")
    check_achievements()
    pause()

def boss_battle():
    title("BOSS BATTLE", "Defeat the arena boss with analytical answers")
    subject = choose_subject()
    pool = questions[subject]["Hard"]
    selected = random.sample(pool, min(7, len(pool)))
    player["quizzes"] += 1
    score, wins, _, _ = run_round(selected, "Boss Battle", "Hard", boss=True)
    if wins >= 5:
        player["boss_wins"] += 1
        bonus = 150
        player["score"] += bonus
        player["xp"] += bonus
        player["coins"] += 30
        update_level()
        print("\n╔════════════════════════════════════════════════════════════╗")
        print("║                 BOSS DEFEATED! 🏆                         ║")
        print("║             +150 POINTS   +30 COINS                       ║")
        print("╚════════════════════════════════════════════════════════════╝")
    else:
        print(f"\nBoss survives. You scored {wins}/{len(selected)} hits.")
    check_achievements()
    pause()

def tournament():
    title("ARENA TOURNAMENT", "Three rounds. Each round gets harder.")
    stages = [("Qualifier", "Easy", 5, 15), ("Semi-Final", "Medium", 6, 25), ("Final", "Hard", 7, 40)]
    total_score = 0
    total_correct = 0
    for stage, level, count, reward in stages:
        print(f"\n>>> {stage.upper()} <<<")
        subject = random.choice(list(questions.keys()))
        selected = random.sample(questions[subject][level], min(count, len(questions[subject][level])))
        score, correct, _, _ = run_round(selected, "Tournament", level)
        total_score += score
        total_correct += correct
        if correct < max(2, count // 2):
            print(f"Tournament run ended in the {stage}.")
            pause()
            return
        print(f"{stage} cleared! Stage reward: +{reward} coins")
        player["coins"] += reward
    player["tournament_wins"] += 1
    bonus = 200
    player["score"] += bonus
    player["xp"] += bonus
    player["coins"] += 50
    update_level()
    print("\n╔════════════════════════════════════════════════════════════╗")
    print("║                 TOURNAMENT CHAMPION!                     ║")
    print("║          +200 POINTS   +50 COINS   +1 WIN                ║")
    print("╚════════════════════════════════════════════════════════════╝")
    check_achievements()
    pause()

def quick_math():
    title("QUICK MATH", "Fast thinking mini-game")
    a = random.randint(5, 30)
    b = random.randint(2, 15)
    op = random.choice(["+", "-", "*"])
    ans = a+b if op == "+" else a-b if op == "-" else a*b
    print(f"\nSolve: {a} {op} {b}")
    try:
        user = int(input("Answer: "))
        if user == ans:
            player["score"] += 20; player["xp"] += 20; player["coins"] += 2
            update_level(); print("✓ Correct! +20 points")
        else: print("✗ Correct answer:", ans)
    except ValueError: print("Invalid answer.")
    player["games"] += 1
    check_achievements(); pause()

def number_game():
    title("NUMBER HUNT", "Find the hidden number")
    secret = random.randint(1, 50)
    print("Guess a number from 1 to 50. You have 6 tries.")
    won = False
    for _ in range(6):
        guess = get_int("Guess: ", 1, 50)
        if guess == secret:
            won = True; print("✓ You found it! +30 points")
            player["score"] += 30; player["xp"] += 30; player["coins"] += 3; update_level(); break
        print("Higher." if guess < secret else "Lower.")
    if not won: print("The number was", secret)
    player["games"] += 1; check_achievements(); pause()

def rps():
    title("ROCK PAPER SCISSORS", "Beat the arena bot")
    choices = ["rock", "paper", "scissors"]
    user = input("Choose rock, paper or scissors: ").lower().strip()
    if user not in choices:
        print("Invalid choice."); pause(); return
    comp = random.choice(choices); print("Arena bot:", comp)
    if user == comp: print("Draw!")
    elif (user == "rock" and comp == "scissors") or (user == "paper" and comp == "rock") or (user == "scissors" and comp == "paper"):
        print("✓ You win! +15 points"); player["score"] += 15; player["xp"] += 15; player["coins"] += 2; update_level()
    else: print("Bot wins this round.")
    player["games"] += 1; check_achievements(); pause()

def game_hub():
    while True:
        title("GAME HUB", "Mini-games for extra points and coins")
        print("1. Quick Math")
        print("2. Number Hunt")
        print("3. Rock Paper Scissors")
        print("4. Return")
        c = get_int("\nChoose: ", 1, 4)
        if c == 1: quick_math()
        elif c == 2: number_game()
        elif c == 3: rps()
        else: break

def risk_reward():
    title("RISK & REWARD", "Choose your risk before the result is revealed")
    print("1. Safe      +10 guaranteed")
    print("2. Risky     +30 or 0")
    print("3. Extreme   +70 or -20")
    c = get_int("\nChoose: ", 1, 3)
    roll = random.randint(1, 100)
    if c == 1:
        reward = 10
    elif c == 2:
        reward = 30 if roll <= 60 else 0
    else:
        reward = 70 if roll <= 40 else -20
    player["score"] = max(0, player["score"] + reward)
    if reward > 0:
        player["xp"] += reward; player["coins"] += max(1, reward//10); update_level()
    print("\nOutcome:", f"+{reward}" if reward >= 0 else str(reward), "points")
    pause()

def shop():
    items = [("50/50", 20), ("Hint", 15), ("Phone", 20), ("Skip", 25), ("Double", 35), ("Shield", 40)]
    while True:
        title("ARENA SHOP", "Spend coins on power-ups")
        print("Your coins:", player["coins"])
        for i, (name, cost) in enumerate(items, 1):
            print(f"{i}. {name:<10} {cost:>3} coins   Owned: {player['powerups'][name]}")
        print(f"{len(items)+1}. Return")
        c = get_int("\nChoose: ", 1, len(items)+1)
        if c == len(items)+1: break
        name, cost = items[c-1]
        if player["coins"] >= cost:
            player["coins"] -= cost; player["powerups"][name] += 1
            print(f"Purchased {name} power-up!")
        else: print("Not enough coins.")
        pause()

def performance():
    title("PERFORMANCE LAB", "Understand how you play")
    q = player["questions"]
    acc = player["correct"] / q * 100 if q else 0
    avg_time = player["total_time"] / player["questions_answered"] if player["questions_answered"] else 0
    print(f"Accuracy          : {acc:.1f}%")
    print(f"Questions         : {q}")
    print(f"Correct           : {player['correct']}")
    print(f"Wrong             : {player['wrong']}")
    print(f"Best streak       : {player['best_streak']}")
    print(f"Average time      : {avg_time:.1f}s/question")
    print(f"Fastest answer    : {player['best_speed']:.1f}s" if player['best_speed'] else "Fastest answer    : --")
    print(f"Perfect rounds    : {player['perfect_rounds']}")
    print(f"Boss wins         : {player['boss_wins']}")
    print(f"Tournament wins   : {player['tournament_wins']}")
    print("\nPerformance class:", "EXCELLENT" if acc >= 85 else "STRONG" if acc >= 70 else "DEVELOPING" if acc >= 50 else "KEEP PRACTISING")
    pause()

def profile():
    check_achievements()
    title("PLAYER PROFILE", f"{player['name']} | Level {player['level']}")
    total = player["questions"]
    accuracy = player["correct"] / total * 100 if total else 0
    print(f"Score             : {player['score']}")
    print(f"XP                : {player['xp']}")
    print(f"Coins             : {player['coins']}")
    print(f"Accuracy          : {accuracy:.1f}%")
    print(f"Best streak       : {player['best_streak']}")
    print(f"Quizzes           : {player['quizzes']}")
    print(f"Boss wins         : {player['boss_wins']}")
    print(f"Tournament wins   : {player['tournament_wins']}")
    print(f"Mini-games        : {player['games']}")
    print(f"Achievements      : {len(player['achievements'])}")
    print("\nPower-up inventory:")
    for name, count in player["powerups"].items(): print(f"  {name:<10}: {count}")
    pause()

def achievements():
    check_achievements()
    title("ACHIEVEMENT HALL", "Collect badges by playing different parts of the arena")
    all_a = ["First Quiz", "Knowledge Seeker", "Hot Streak", "Quiz Regular", "Boss Winner", "Game Player", "Perfect Round", "Coin Collector", "Tournament Champion", "Streak Master", "Century Club", "Accuracy Ace", "Arena Legend", "All-Rounder"]
    for a in all_a:
        print(("★" if a in player["achievements"] else "☆"), a)
    pause()

def leaderboard_show():
    current = (player["name"], player["score"])
    temp = leaderboard + [current]
    temp.sort(key=lambda x: x[1], reverse=True)
    title("SESSION LEADERBOARD", "Scores disappear when the program closes")
    if not temp: print("No scores yet.")
    for i, item in enumerate(temp[:10], 1):
        medal = ["1st", "2nd", "3rd"][i-1] if i <= 3 else f"{i}th"
        print(f"{medal:<5} {item[0]:<20} {item[1]:>7} pts")
    pause()

def how_to_play():
    title("ARENA GUIDE", "Everything you need to know")
    print("CLASSIC       7-question subject challenge")
    print("RAPID FIRE    5-question high-bonus round")
    print("SURVIVAL      10 questions with 3 lives")
    print("BOSS BATTLE   Hard questions and major rewards")
    print("TOURNAMENT    Qualifier → Semi-Final → Final")
    print("CATEGORY MIX  Subjects and difficulty change every question")
    print("DAILY         One high-value challenge per session")
    print("RISK & REWARD Gamble coins/score for larger rewards")
    print("GAME HUB      Three mini-games")
    print("SHOP          Spend coins on limited power-ups")
    print("\nPower-ups: 50/50, Hint, Phone, Skip, Double and Shield.")
    print("Speed matters: faster correct answers can earn bonus points.")
    print("All records and scores exist only while the program is running.")
    pause()

def main():
    title("ULTIMATE QUIZ ARENA", "QUIZ • COMPETE • LEVEL UP • CONQUER")
    player["name"] = input("Enter your player name: ").strip() or "Player"
    print(f"\nWelcome to the Arena, {player['name']}!")
    print("Your mission: build XP, protect your streak, collect coins and master every mode.")
    time.sleep(0.4)
    while True:
        check_achievements()
        print("\n")
        line()
        show_hud()
        line()
        print("  1. Classic Quiz       2. Rapid Fire")
        print("  3. Survival Mode      4. Risk & Reward")
        print("  5. Boss Battle        6. Daily Challenge")
        print("  7. Tournament         8. Category Mix")
        print("  9. Game Hub          10. Arena Shop")
        print(" 11. Player Profile    12. Performance Lab")
        print(" 13. Achievements      14. Leaderboard")
        print(" 15. Arena Guide       16. Exit")
        c = get_int("\nSelect an option: ", 1, 16)
        if c == 1: quiz("Classic")
        elif c == 2: quiz("Rapid Fire")
        elif c == 3: survival()
        elif c == 4: risk_reward()
        elif c == 5: boss_battle()
        elif c == 6: daily_challenge()
        elif c == 7: tournament()
        elif c == 8: category_mix()
        elif c == 9: game_hub()
        elif c == 10: shop()
        elif c == 11: profile()
        elif c == 12: performance()
        elif c == 13: achievements()
        elif c == 14: leaderboard_show()
        elif c == 15: how_to_play()
        else:
            leaderboard.append((player["name"], player["score"]))
            title("ARENA COMPLETE", f"Thanks for playing, {player['name']}!")
            print("Final Score :", player["score"])
            print("Final Level :", player["level"])
            print("Coins       :", player["coins"])
            print("Achievements:", len(player["achievements"]))
            print("\nCome back and beat your score! 🎮")
            break

if __name__ == "__main__":
    main()
