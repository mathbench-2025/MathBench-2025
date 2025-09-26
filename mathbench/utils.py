def compare_stepwise(pred_steps, ref_steps):
    matched_steps = sum([1 for p, r in zip(pred_steps, ref_steps) if p.strip() == r.strip()])
    stepwise_score = matched_steps / max(len(ref_steps), 1)
    final_correct = pred_steps[-1].strip() == ref_steps[-1].strip()
    return stepwise_score, final_correct

def print_problem(problem):
    print(f"ID: {problem['problem_id']}")
    print(f"Type: {problem['problem_type']} | Complexity: {problem['complexity_level']}")
    for s in problem["solution_steps"]:
        print(" -", s)
    print("Reference solution:", problem["reference_solution"])
