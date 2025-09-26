import os
import openai
from tqdm import tqdm
from .utils import compare_stepwise

openai.api_key = os.getenv("OPENAI_API_KEY")

def evaluate_model_llm(dataset, model_name="gpt-4"):
    total = len(dataset)
    correct = 0
    stepwise_total = 0
    complexity_sum = 0
    
    for item in tqdm(dataset):
        prompt = "Solve this problem step by step:\n" + item['solution_steps'][0]
        response = openai.ChatCompletion.create(
            model=model_name,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        pred_steps = response.choices[0].message.content.split("\n")
        stepwise_score, final_correct = compare_stepwise(pred_steps, item['solution_steps'])
        correct += int(final_correct)
        stepwise_total += stepwise_score
        complexity_sum += item['complexity_level']
    
    return {
        "accuracy": 100 * correct / total,
        "stepwise_correctness": 100 * stepwise_total / total,
        "avg_complexity": complexity_sum / total
    }
