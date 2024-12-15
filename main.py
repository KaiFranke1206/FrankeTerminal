import os
import sys
import importlib
import shlex
from _startup import startup

commandsDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'commands')
sys.path.append(commandsDir)

def execute(inp):
    try:
        parts = shlex.split(inp)
        if not parts:
            print("No command entered.")
            return
        
        commandName = parts[0]
        args = " ".join(parts[1:]) if len(parts) > 1 else ""
        
        commandList = [f.split('.', 1)[0] for f in os.listdir(commandsDir) if f.endswith('.py')]
        
        if commandName in commandList:
            try:
                moduledir = f"{commandName}"
                module = importlib.import_module(moduledir)
                if hasattr(module, 'run'):
                    module.run(args)
                else:
                    print(f"The module '{commandName}' does not have a 'run' function.")
            except Exception as e:
                print(f"Failed to execute command '{commandName}': {e}")
        else:
            print(f"Command '{commandName}' not found.")
            print(f"Available commands: {', '.join(commandList)}")
    except Exception as e:
        print(f"Error processing input: {e}")
		
def terminal():
	startup()
	while True:
		try:
			execute(input('>>> '))
		except KeyboardInterrupt:
			print("\nExiting terminal...")
			break
			
terminal()