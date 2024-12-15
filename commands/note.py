def run(args):
    if not args.strip():
        print("Usage: note <message>")
        return

    message = args.strip()
    with open("notes.txt", "a") as f:
        f.write(message + "\n")
    print(f"Note saved: {message}")
