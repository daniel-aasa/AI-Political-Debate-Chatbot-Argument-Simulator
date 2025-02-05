from gpt1 import call_gpt
from gpt2 import call_gpt2
from utilities import gpt_messages,gpt_messages2
from bias import detect_bias


print(f"GPT:\n{gpt_messages[0]}\n")
print(f"GPT2:\n{gpt_messages2[0]}\n")

conversation_transcript = ""

for i in range(5):
    gpt_next = call_gpt()
    print(f"GPT:\n{gpt_next}\n")
    gpt_messages.append(gpt_next)
    
    gpt_next2 = call_gpt2()
    print(f"GPT2:\n{gpt_next2}\n")
    gpt_messages2.append(gpt_next2)

    conversation_transcript += "GPT1: " + gpt_next + "\n"
    conversation_transcript += "GPT2: " + gpt_next2 + "\n"

print("Bias Analysis:")
print(detect_bias(conversation_transcript))