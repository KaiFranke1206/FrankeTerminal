import os

def run(args):
    commands_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    try:
        commands = [f.split(".")[0] for f in os.listdir(commands_dir) if f.endswith(".py")]

        print("Available Commands:")
        print("-------------------")
        for command in sorted(commands):
            print(f"- {command}")
        print("\nUse '<command> --help' for more information on a specific command.")
    except Exception as e:
        print(f"Error retrieving commands: {e}")
