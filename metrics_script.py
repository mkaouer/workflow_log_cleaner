import pandas as pd
import numpy as np
import time
import re
from sklearn.metrics import cohen_kappa_score
from collections import Counter

# Simulated input: Replace these with your actual files
raw_logs = ["Error: Connection failed", "Build failed due to timeout", "Syntax error in line 5"]
preprocessed_logs = ["Connection failed", "Timeout error", "Syntax error"]
llm_explanations = pd.DataFrame({
    "log_id": [1, 2, 3],
    "model": ["GPT-4", "GPT-4", "GPT-4"],
    "explanation": ["Check network settings", "Increase timeout value", "Fix syntax in line 5"],
    "correctness_score": [8, 7, 9],
    "relevance_score": [9, 8, 9],
    "depth_score": [7, 6, 8],
    "clarity_score": [8, 9, 9],
    "formatting_score": [7, 8, 9],
    "response_time": [200, 250, 180],  # in milliseconds
    "actionable_steps": [2, 3, 1]
})

# ✅ 1. FAILURE LOCALIZATION ACCURACY
correct_localizations = 2  # Replace with expert-verified counts
total_failures = len(raw_logs)
failure_localization_accuracy = (correct_localizations / total_failures) * 100

# ✅ 2. FIX RECOMMENDATION ACCURACY
correct_fixes = 2  # Replace with expert-verified counts
total_fixes = len(llm_explanations)
fix_recommendation_accuracy = (correct_fixes / total_fixes) * 100

# ✅ 3. TOKEN REDUCTION PERCENTAGE
raw_tokens = sum(len(log.split()) for log in raw_logs)
preprocessed_tokens = sum(len(log.split()) for log in preprocessed_logs)
token_reduction_percentage = ((raw_tokens - preprocessed_tokens) / raw_tokens) * 100

# ✅ 4. RESPONSE TIME ANALYSIS
average_response_time = np.mean(llm_explanations["response_time"])

# ✅ 5. AGREEMENT BETWEEN HUMAN EVALUATORS (Cohen's Kappa)
# Simulated human evaluation scores for correctness
human_scores_1 = [8, 7, 9]  # Evaluator 1
human_scores_2 = [7, 8, 9]  # Evaluator 2
cohens_kappa = cohen_kappa_score(human_scores_1, human_scores_2)

# ✅ 6. MODEL CONSISTENCY (Same explanations for the same log)
consistency_scores = llm_explanations.groupby("log_id")["explanation"].nunique().apply(lambda x: 100 if x == 1 else 0)
model_consistency = consistency_scores.mean()

# ✅ 7. TABLE OF METRICS
metrics_table = pd.DataFrame({
    "Metric": ["Failure Localization Accuracy", "Fix Recommendation Accuracy", "Token Reduction Percentage", 
               "Average Response Time (ms)", "Cohen's Kappa (Evaluator Agreement)", "Model Consistency"],
    "Value": [failure_localization_accuracy, fix_recommendation_accuracy, token_reduction_percentage, 
              average_response_time, cohens_kappa, model_consistency]
})

print("\n📊 Final Metrics Table:")
print(metrics_table)

# ✅ 8. PLOTTING THE METRICS
import matplotlib.pyplot as plt
import seaborn as sns

# 📌 Bar Chart: Scores for Correctness, Relevance, Depth, etc.
scores_df = llm_explanations[["correctness_score", "relevance_score", "depth_score", "clarity_score", "formatting_score"]]
scores_df.mean().plot(kind='bar', title="Model Performance Scores", figsize=(8, 5), colormap='viridis')
plt.ylabel("Average Score (1-10)")
plt.show()

# 📌 Line Graph: Response Time per Model
plt.figure(figsize=(8, 5))
sns.lineplot(data=llm_explanations, x="log_id", y="response_time", marker="o")
plt.title("LLM Response Time per Log")
plt.xlabel("Log ID")
plt.ylabel("Response Time (ms)")
plt.show()

# 📌 Pie Chart: Token Reduction
plt.figure(figsize=(6, 6))
plt.pie([token_reduction_percentage, 100-token_reduction_percentage], labels=["Tokens Removed", "Tokens Retained"], autopct='%1.1f%%', colors=['green', 'gray'])
plt.title("Token Reduction Percentage")
plt.show()
