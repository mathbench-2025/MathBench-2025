import json, random, os
os.makedirs("../data", exist_ok=True)

categories = {
    "arithmetic": ["addition", "subtraction", "multiplication", "division"],
    "algebra": ["linear equations", "quadratic equations", "systems"],
    "proof": ["sum formulas", "inequalities", "geometry"],
    "applied": ["physics", "finance", "algorithms"]
}

def generate_problem(category, idx):
    complexity = (idx % 5) + 1
    topic = categories[category][idx % len(categories[category])]
    pid = f"{category[:2].upper()}{idx+1:03d}"
    
    if category == "arithmetic":
        steps = [f"Compute {idx+1} + {idx+2}", f"{idx+1} + {idx+2} = {2*idx+3}"]
        solution = str(2*idx+3)
    elif category == "algebra":
        steps = [f"Solve x + {idx} = {idx+2}", "x = 2"]
        solution = "x = 2"
    elif category == "proof":
        steps = ["State base case", "Assume true for n=k", "Prove for n=k+1"]
        solution = "Proof holds"
    else:
        steps = [f"Apply formula for problem {idx}", "Compute final answer"]
        solution = "Final answer"
    
    return {
        "problem_id": pid,
        "problem_type": category,
        "complexity_level": complexity,
        "solution_steps": steps,
        "topic": topic,
        "reference_solution": solution
    }

all_problems = []
counter = 0
for category in categories:
    for i in range(25):
        all_problems.append(generate_problem(category, counter))
        counter += 1

random.shuffle(all_problems)
train = all_problems[:60]
valid = all_problems[60:80]
test  = all_problems[80:100]

os.makedirs("..", exist_ok=True)
with open("../data/mathbench_train.json", "w") as f: json.dump(train, f, indent=4)
with open("../data/mathbench_valid.json", "w") as f: json.dump(valid, f, indent=4)
with open("../data/mathbench_test.json", "w") as f: json.dump(test, f, indent=4)

print("Dataset generated: Train 60, Valid 20, Test 20")
