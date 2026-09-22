import random
import time

RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

TEMPLATES = [
    "ERROR...error...FIX THE CODE LN{a} LN{b}...shutdown system...{c}",
    "ERROR...ERRORRRR...FIX THE CODE LN{a} LN{b}.ERRORRR...shutdown system",
    "ERROR.....FIX THE CODE.........",
    "ERROR...error...FIX THE CODE LN{a} LN{b}...shutdown system...{c}",
]

def random_line():
    template = random.choice(TEMPLATES)
    return template.format(
        a=random.randint(100, 999),
        b=random.randint(1, 99),
        c=random.randint(1, 999),
    )

def main():
    try:
        while True:
            print(f"{RED}{BOLD}{random_line()}{RESET}")
            time.sleep(0.03)
    except KeyboardInterrupt:
        print(f"{RESET}\nDihentikan oleh pengguna (Ctrl+C).")

if __name__ == "__main__":
    main()
