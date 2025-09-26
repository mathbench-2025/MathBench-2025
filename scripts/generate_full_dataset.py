import json
import random
import os
import math

os.makedirs("../data", exist_ok=True)

# Topics per category
categories = {
    "arithmetic": ["addition", "subtraction", "multiplication", "division"],
    "algebra": ["linear equations", "quadratic equations", "systems"],
    "proof": ["sum formulas", "inequalities", "geometry"],
    "applied": ["physics", "finance", "algorithms"]
}

# Number of problems per category and level
problem_counts = {
    "arithmetic": [600, 200, 100, 0, 0],
    "algebra": [200, 400, 500, 100, 0],
    "proof": [0, 50, 100, 300, 50],
    "applied": [0, 50, 150, 100, 200]
}

# Problem generators
def generate_arithmetic(idx, level):
    a, b = random.randint(1, 50), random.randint(1, 50)
    op = random.choice(["+", "-", "*", "//"])
    if op == "+": solution = a + b
    elif op == "-": solution = a - b
    elif op == "*": solution = a * b
    else: solution = a // b if b != 0 else 0
    steps = [f"Compute {a} {op} {b}", f"Result: {solution}"]
    return steps, solution

def generate_algebra(idx, level):
    if level <= 2:  # simple linear
        x = random.randint(1, 20)
        b = random.randint(1, 20)
        c = x + b
        steps = [f"Solve x + {b} = {c}", f"x = {c - b}"]
        solution = f"x = {c - b}"
    elif level == 3:  # multi-step linear
        x = random.randint(1, 20)
        y = random.randint(1, 20)
        # system: x + y = sum, 2x - y = diff
        sum_xy = x + y
        diff_xy = 2*x - y
        steps = [f"Solve system: x + y = {sum_xy}, 2x - y = {diff_xy}",
                 f"From x + y = {sum_xy} => y = {sum_xy}-x",
                 f"Substitute: 2x - ({sum_xy}-x) = {diff_xy} => Solve x",
                 f"x = {x}, y = {y}"]
        solution = f"x = {x}, y = {y}"
    else:  # level 4: quadratic
        a = random.randint(1,5)
        b = random.randint(1,10)
        c = random.randint(1,10)
        disc = b**2 - 4*a*c
        if disc < 0: disc = 0
        root1 = (-b + math.isqrt(disc)) // (2*a)
        root2 = (-b - math.isqrt(disc)) // (2*a)
        steps = [f"Solve quadratic: {a}x^2 + {b}x + {c} = 0",
                 "Compute discriminant D = b^2 - 4ac",
                 f"D = {disc}",
                 f"Roots: x = (-b ± √D) / (2a) => x1 = {root1}, x2 = {root2}"]
        solution = f"x1 = {root1}, x2 = {root2}"
    return steps, solution

def generate_proof(idx, level):
    steps = ["State base case", "Assume statement holds for n=k", "Prove for n=k+1"]
    solution = "Proof holds by induction"
    return steps, solution

def generate_applied(idx, level):
    if level <= 3:
        # basic applied problem
        u = random.randint(5, 20)
        a = random.randint(1,5)
        t = random.randint(1,10)
        v = u + a * t
        steps = [f"Initial velocity u={u}, acceleration a={a}, time t={t}",
                 f"Compute final velocity: v = u + a*t = {v}"]
        solution = f"v = {v}"
    else:  # level 4-5: multi-step physics + finance
        choice = random.choice(["physics", "finance"])
        if choice == "physics":
            u = random.randint(10,30)
            a = random.randint(1,5)
            t = random.randint(5,15)
            s = u*t + 0.5*a*t**2
            steps = [f"u={u}, a={a}, t={t}", f"s = ut + 0.5*a*t^2 = {s}"]
            solution = f"s = {s}"
        else:  # finance: compound interest
            P = random.randint(100,1000)
            r = random.randint(1,10)/100
            n = 1
            t = random.randint(5,10)
            A = P * (1 + r/n)**(n*t)
            steps = [f"P={P}, r={r}, n={n}, t={t}", f"A = P*(1+r/n)^(n*t) ≈ {round(A,2)}"]
            solution = f"A ≈ {round(A,2)}"
    return steps, solution

# Main problem generator
def generate_problem(category, level, idx):
    topic = categories[category][idx % len(categories[category])]
    pid = f"{category[:2].upper()}{level}{idx+1:04d}"

    if category == "arithmetic":
        steps, solution = generate_arithmetic(idx, level)
    elif category == "algebra":
        steps, solution = generate_algebra(idx, level)
    elif category == "proof":
        steps, solution = generate_proof(idx, level)
    else:
        steps, solution = generate_applied(idx, level)

    return {
        "problem_id": pid,
        "problem_type": category,
        "complexity_level": level,
        "solution_steps": steps,
        "topic": topic,
        "reference_solution": solution
    }

# Generate dataset according to counts
all_problems = []
for category, counts in problem_counts.items():
    for level, count in enumerate(counts, start=1):
        for i in range(count):
            all_problems.append(generate_problem(category, level, i))

random.shuffle(all_problems)

# Train/val/test split
total = len(all_problems)
train_end = int(0.7*total)
valid_end = train_end + int(0.15*total)

train = all_problems[:train_end]
valid = all_problems[train_end:valid_end]
test = all_problems[valid_end:]

# Save JSON
with open("../data/mathbench_train.json", "w") as f: json.dump(train, f, indent=4)
with open("../data/mathbench_valid.json", "w") as f: json.dump(valid, f, indent=4)
with open("../data/mathbench_test.json", "w") as f: json.dump(test, f, indent=4)

print(f"Dataset generated: Train {len(train)}, Valid {len(valid)}, Test {len(test)}, Total {len(all_problems)}")
