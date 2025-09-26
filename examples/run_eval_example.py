from mathbench.dataset import load_dataset
from mathbench.evaluation import evaluate_model_llm

def main():
    test_data = load_dataset("data/mathbench_test.json")
    results = evaluate_model_llm(test_data, model_name="gpt-4")
    print("Evaluation Results:", results)

if __name__ == "__main__":
    main()
