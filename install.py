import os

# Content of the Python script
python_script_content = """\
#!/bin/bash
python3 {python_script_path} "$@"
"""

# Path to the Python script
python_script_path = "ai-text.py"  # Replace with the actual path to your ask.py script

# Path to the shell script
shell_script_path = "/usr/local/bin/ask"

# Create the shell script
with open(shell_script_path, "w") as file:
    file.write(python_script_content.format(python_script_path=python_script_path))

# Make the shell script executable
os.chmod(shell_script_path, 0o755)

print("Installation completed.")
