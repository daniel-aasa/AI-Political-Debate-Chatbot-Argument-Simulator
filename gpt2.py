from utilities import openai2,gpt_model,gpt_system2,gpt_messages,gpt_messages2 

def call_gpt2():
    messages = []
    for gpt, gpt2 in zip(gpt_messages, gpt_messages2):
        messages = [{"role": "system", "content": gpt_system2}]
        messages.append({"role": "user", "content": gpt})
        messages.append({"role": "assistant", "content": gpt2})
    messages.append({"role": "user", "content": gpt_messages[-1]})
    completion = openai2.chat.completions.create(
        model=gpt_model,
        messages=messages
    )
    return completion.choices[0].message.content

#print(call_gpt2())