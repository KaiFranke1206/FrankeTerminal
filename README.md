# FrankeOS v1.0

FrankeOS is a lightweight, terminal-based operating system simulator. It provides an interactive command-line interface with a range of useful commands, allowing users to simulate OS-like functionality.

---

## Features

- **Custom Terminal Experience**: A startup sequence followed by an interactive terminal environment.
- **Built-in Commands**: A rich set of commands for file management, networking, system utilities, and more.
- **Extensible Architecture**: Easily add new commands by creating Python modules in the `commands` directory.

---

## Prerequisites

- **Python 3.8+**
- Dependencies listed in `requirements.txt`.

### Installation

Clone the repository or download the source code, then install dependencies:
```bash
pip install -r requirements.txt
```

---

## Usage

1. **Run the Program**  
   Start the terminal simulator by executing the `main.py` file:
   ```bash
   python main.py
   ```

2. **Interact with the Terminal**  
   After the startup sequence, you will be presented with a terminal interface (`>>>`). Type any of the supported commands to interact with the system.

3. **Exit the Terminal**  
   Use the `exit` command or press `Ctrl+C` to leave the terminal environment.

---

## Commands

| Command      | Description                                          |
|--------------|------------------------------------------------------|
| **alias**    | Manage command aliases.                              |
| **cal**      | Display a calendar.                                  |
| **cd**       | Change the current working directory.                |
| **exit**     | Exit the terminal session.                           |
| **fileinfo** | Retrieve details about a specified file.             |
| **find**     | Search for files or directories by name.             |
| **help**     | Display help information for available commands.     |
| **ifconfig** | Display network interface configuration.             |
| **kill**     | Terminate a process by its process ID (PID).         |
| **list**     | List files and directories in the current location.  |
| **mkdir**    | Create a new directory.                              |
| **netstat**  | Show network statistics and active connections.      |
| **note**     | Create, edit, and view notes.                        |
| **ping**     | Test connectivity to a host.                         |
| **pwd**      | Print the current working directory.                 |
| **recall**   | Usage like echo.                                     |
| **rm**       | Remove files or directories.                         |
| **run**      | Execute a specified program or script.               |
| **sysinfo**  | Display detailed system information.                 |
| **taskman**  | Manage running processes and view their status.      |
| **theme**    | Customize the terminal appearance.                   |
| **wget**     | Download files from the internet.                    |
| **wipe**     | Clear the Terminal Screen.                           |

---

## File Structure

```plaintext
.
├── _startup.py         # Handles the startup sequence for FrankeOS.
├── main.py             # Main entry point for the terminal simulator.
├── requirements.txt    # List of required Python packages.
├── commands/           # Directory for all command modules.
│   ├── alias.py        # Command module for alias management.
│   ├── cal.py          # Command module to display a calendar.
│   ├── cd.py           # Command module to change directories.
│   ├── ...             # Additional commands (one per file).
```

### Adding New Commands
1. Create a new Python file in the `commands/` directory.
2. Implement a `run(args)` function in the file. This function is called when the command is executed.
3. The new command will automatically be available in the terminal.

Example command module (`commands/hello.py`):
```python
def run(args):
    print("Hello, World!")
```

---

## Examples

### General Usage
- **List files in the current directory**:
  ```plaintext
  >>> list
  ```
- **Create a new directory**:
  ```plaintext
  >>> mkdir new_folder
  ```
- **Download a file**:
  ```plaintext
  >>> wget http://example.com/file.txt
  ```
- **Ping a host**:
  ```plaintext
  >>> ping 8.8.8.8
  ```
- **Check system information**:
  ```plaintext
  >>> sysinfo
  ```

---

## Dependencies

The project relies on the following Python libraries:
- `psutil`: For system and process management.
- `requests`: For handling HTTP requests (e.g., `wget`).

Install them using:
```bash
pip install -r requirements.txt
```

---

## Extending FrankeOS

Adding functionality to FrankeOS is straightforward. Write a new command as described in the **Adding New Commands** section. Leverage Python libraries or system APIs to extend the capabilities of the terminal.

---

## Acknowledgements

This `README.md` file was created by ChatGPT, as the author was too lazy to write it. Enjoy using FrankeOS, and feel free to improve upon this work!

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and share.

---

## Acknowledgements

Thanks for exploring FrankeOS! Feedback and contributions are welcome.

