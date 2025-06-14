# dl-ai-llmops
This repository showcases an end-to-end Reinforcement Learning from Human Feedback (RLHF) pipeline implemented on Google Cloud's Vertex AI Pipelines. 

## Public Datasets Used: 
- "preference_dataset": "gs://vertex-ai/generative-ai/rlhf/text_small/summarize_from_feedback_tfds/comparisons/train/*.jsonl",
- "prompt_dataset": "gs://vertex-ai/generative-ai/rlhf/text_small/reddit_tfds/train/*.jsonl",
- "eval_dataset": "gs://vertex-ai/generative-ai/rlhf/text_small/reddit_tfds/val/*.jsonl"

## Reinforcement Learning from Human Feedback (RLHF) Pipeline
RLHF is a state-of-the-art technique used to align Large Language Models (LLMs) with human preferences, significantly improving their helpfulness, harmlessness, and overall quality.

The pipeline consists of three core stages, orchestrated as distinct components, allowing for modularity, reproducibility, and scalability. 
![RLHF Pipeline](/images/RLHF%20Pipeline%20Run.png)

### **Reward Model (RM) Training** 
**Purpose**: To train a model that accurately predicts human preferences for LLM responses, serving as an automated "human-in-the-loop" signal.

**Process**:

A dedicated Reward Model (typically a smaller LLM) is trained on a human preference dataset. This dataset contains pairs of LLM responses for the same prompt, along with a label indicating which response was preferred by humans.
The RM learns to assign a scalar "reward score" to any given LLM response.
The training objective usually involves minimizing a pairwise ranking loss (e.g., a logistic loss) to ensure the preferred response consistently receives a higher score than the non-prefered one. 
![KFP graph for "Reward Model Training" component](/images/Reward%20Model%20Training%20Components.png)

### **Reinforcement Learning (Policy Optimization)**
**Purpose**:: To fine-tune the LLM to generate responses that maximize the reward signal from the trained Reward Model, thereby aligning its outputs with human preferences.

**Process**:

The base LLM (now acting as the Policy Model) generates responses to a diverse prompt dataset.
Each of these generated responses is then scored by the trained Reward Model.
Using Reinforcement Learning algorithms (e.g. Proximal Policy Optimization - PPO), the Policy Model's parameters are iteratively updated. The goal is to maximize the cumulative reward received from the Reward Model for its generated responses.
A KL divergence penalty is typically incorporated to prevent the LLM from deviating too far from its initial supervised fine-tuned (SFT) state, preserving fluency and avoiding undesirable drifts or "reward hacking."
This iterative optimization process effectively fine-tunes the LLM, making its outputs more aligned with human expectations. 
![KFP graph for "Reinforcement Learning" component](/images/Reinforcement%20Learning%20Components.png)

### **Inference on Evaluation Dataset**
**Purpose**:: To assess the performance and alignment of the fine-tuned LLM on unseen data and validate the effectiveness of the RLHF process.

**Process**:

The newly fine-tuned LLM (the policy model from the RL step) is used to generate responses on a held-out evaluation dataset.
These generated responses can then be:
Manually reviewed for qualitative assessment.
Automatically evaluated using metrics (e.g., ROUGE scores for summarization tasks, or by re-scoring them with the Reward Model if applicable for evaluation).
This final step provides critical quantitative and qualitative insights into the model's improvements in helpfulness, truthfulness, and alignment with desired characteristics.
![KFP graph for "Inference on Evaluation Dataset" component](/images/RLHF%20Inference%20Components.png)

## Setup GCP environment
https://community.deeplearning.ai/t/setting-up-google-cloud-platform-project-and-credentials-to-use-vertex-ai/555545

