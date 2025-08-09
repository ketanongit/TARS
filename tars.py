from llama_cpp import Llama
import os
from colorama import Fore, Style
import sys

# Paths
MODEL_PATH = r"E:\mistral-7b-instruct-v0.2.Q5_K_M.gguf"  # Path to the model
MEMORY_FILE = "memory.txt"

# Load conversation memory
if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        memory = f.read()
else:
    memory = ""

# Personality prompt for TARS
SYSTEM_PROMPT = (
    "You are TARS, a witty and humorous AI assistant with a dry, sarcastic but friendly sense of humor. "
    "Always keep responses concise but clever, like a movie character."
)

print(Fore.YELLOW + "Loading model into memory... please wait..." + Style.RESET_ALL)
llm = Llama(model_path=MODEL_PATH, n_ctx=2048, verbose=False)

# Prime model with SYSTEM_PROMPT so it’s already “thinking” as TARS
print(Fore.YELLOW + "Priming TARS personality..." + Style.RESET_ALL)
_ = llm(
    f"{SYSTEM_PROMPT}\n\n{memory}\nUser: Hello TARS\nTARS:",
    max_tokens=1
)

print(Fore.GREEN + "TARS online. Type 'exit' to quit." + Style.RESET_ALL)

while True:
    user_input = input(Fore.CYAN + "You: " + Style.RESET_ALL)
    if user_input.lower() in ["exit", "quit"]:
        print(Fore.YELLOW + "Shutting down TARS..." + Style.RESET_ALL)
        break

    # Build full prompt
    prompt = f"{SYSTEM_PROMPT}\n\n{memory}\nUser: {user_input}\nTARS:"

    print(Fore.MAGENTA + "TARS: " + Style.RESET_ALL, end="", flush=True)

    tars_reply = ""
    for token in llm(
        prompt,
        max_tokens=256,
        stop=["User:"],
        temperature=0.7,
        stream=True
    ):
        piece = token["choices"][0]["text"]
        sys.stdout.write(piece)
        sys.stdout.flush()
        tars_reply += piece

    print()  # Newline after streaming

    # Append to memory
    memory += f"\nUser: {user_input}\nTARS: {tars_reply.strip()}"
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        f.write(memory)
