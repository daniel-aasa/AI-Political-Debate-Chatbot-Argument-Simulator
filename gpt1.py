from utilities import openai,gpt_model,gpt_system,gpt_messages,gpt_messages2 


def call_gpt():
    messages = [{"role": "system", "content": gpt_system}]
    for gpt, gpt2 in zip(gpt_messages, gpt_messages2):
        messages.append({"role": "assistant", "content": gpt})
        messages.append({"role": "user", "content": gpt2})
    completion = openai.chat.completions.create(
        model=gpt_model,
        messages=messages
    )
    return completion.choices[0].message.content

#print(call_gpt())