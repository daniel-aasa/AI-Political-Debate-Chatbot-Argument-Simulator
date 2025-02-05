from utilities import gpt_model,openai

def detect_bias(conversation):
    bias_system = "You are an unbiased political analyst specialized in detecting bias in political discussions. Analyze the conversation for signs of political bias (e.g., partisan language, extreme positions) and provide a concise report."
    messages = [{"role": "system", "content": bias_system}, {"role": "user", "content": conversation}]
    bias_completion = openai.chat.completions.create(
        model=gpt_model,
        messages=messages
    )
    return bias_completion.choices[0].message.content