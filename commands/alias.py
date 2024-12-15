aliases = {}

def run(args):
    global aliases
    if "=" in args:
        alias, command = args.split("=", 1)
        aliases[alias.strip()] = command.strip()
        print(f"Alias set: {alias.strip()} -> {command.strip()}")
    elif args.strip() in aliases:
        print(f"{args.strip()} -> {aliases[args.strip()]}")
    else:
        print("Usage: alias <name>=<command>")
