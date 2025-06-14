# dl-ai-llmops
Fine tuning LLM Foundation model in GCP Vertex AI using RLHF PEFT. 

Public Datasets Used: 
- "preference_dataset": "gs://vertex-ai/generative-ai/rlhf/text_small/summarize_from_feedback_tfds/comparisons/train/*.jsonl",
- "prompt_dataset": "gs://vertex-ai/generative-ai/rlhf/text_small/reddit_tfds/train/*.jsonl",
- "eval_dataset": "gs://vertex-ai/generative-ai/rlhf/text_small/reddit_tfds/val/*.jsonl"

## Setup your gcp environment by following the link
https://community.deeplearning.ai/t/setting-up-google-cloud-platform-project-and-credentials-to-use-vertex-ai/555545
