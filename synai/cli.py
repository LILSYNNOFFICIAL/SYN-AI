from synai.agent import SYNAgent


def main():
    agent = SYNAgent()
    print("SYN-AI ready. Termux automation core online.")

    while True:
        request = input("syn-ai> ").strip()
        if request.lower() in {"exit", "quit"}:
            break
        print(agent.handle(request))


if __name__ == "__main__":
    main()
