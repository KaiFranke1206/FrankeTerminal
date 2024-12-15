import os
import subprocess

def run(args):
    if not args.strip():
        print("Usage: run <filename>")
        return

    filename = args.strip()
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return

    # Determine file extension
    _, ext = os.path.splitext(filename)
    ext = ext.lower()

    # Define commands based on file extensions
    commands = {
        '.py': ['python'],
        '.java': ['javac', 'java'],
        '.c': ['gcc', './a.out'],
        '.cpp': ['g++', './a.out'],
        '.cs': ['csc', 'mono'],
        '.rs': ['rustc', './a.out'],
        '.js': ['node']
    }

    if ext in commands:
        try:
            if ext in ['.c', '.cpp', '.rs']:
                compile_cmd = commands[ext][0]
                execute_cmd = commands[ext][1]
                subprocess.run([compile_cmd, filename], check=True)
                subprocess.run([execute_cmd], check=True)
            elif ext == '.java':
                compile_cmd = commands[ext][0]
                run_cmd = commands[ext][1]
                base_name = os.path.splitext(filename)[0]
                subprocess.run([compile_cmd, filename], check=True)
                subprocess.run([run_cmd, base_name], check=True)
            else:
                subprocess.run([commands[ext][0], filename], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error during execution: {e}")
    else:
        print(f"Unsupported file type: {ext}")
