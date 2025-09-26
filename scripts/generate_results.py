import json
import pandas as pd
from mathbench.dataset import load_dataset
from mathbench.evaluation import evaluate_model_llm

def main():
    # Load dataset
    test_data = load_dataset("../data/mathbench_test.json")

    # Evaluate
    results = evaluate_model_llm(test_data, model_name="gpt-4")

    # Save results to CSV
    df = pd.DataFrame([results])
    df.to_csv("../data/evaluation_results.csv", index=False)
    print("Evaluation completed. Results saved to ../data/evaluation_results.csv")
    print("Results:", results)

if __name__ == "__main__":
    main()
