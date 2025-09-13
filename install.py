import os
import subprocess
import sys
import time
import shutil

# Loading bar for progress visualization
def loading_bar(iteration, total, prefix='', length=40):
    filled_length = int(length * iteration // total)
    bar = '█' * filled_length + '-' * (length - filled_length)
    percent = (100 * (iteration / total))
    sys.stdout.write(f'\r{prefix} |{bar}| {percent:.1f}% Complete')
    sys.stdout.flush()

# Execute shell command with error handling
def execute_command(command, description):
    try:
        print(f"\n{description}...")
        # Using a simple spinner for commands as progress bar is not always applicable
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        spinner = "|/-\\"
        idx = 0
        while process.poll() is None:
            sys.stdout.write(f'\r{description} {spinner[idx % len(spinner)]}')
            sys.stdout.flush()
            time.sleep(0.1)
            idx += 1
        
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            sys.stdout.write(f'\r{description} Done.      \n')
            sys.stdout.flush()
        else:
            sys.stdout.write(f'\r{description} Failed.    \n')
            sys.stdout.flush()
            print(f"Error: {stderr.decode().strip()}")

    except Exception as e:
        print(f"\nAn unexpected error occurred during {description}: {e}")

# Check if a command is available
def is_command_available(command):
    """Check if a command is in the system's PATH."""
    return shutil.which(command) is not None

# Check and install dependencies
def check_and_install_dependencies(dependencies):
    print("Checking for required dependencies...")
    missing_deps = []
    for pkg, cmd in dependencies:
        if not is_command_available(cmd):
            missing_deps.append(pkg)
        else:
            print(f"  [✓] {pkg} is already installed.")

    if not missing_deps:
        print("\nAll dependencies are satisfied.")
        return

    print("\nThe following dependencies are missing:", ", ".join(missing_deps))
    proceed = input("Do you want to install them? (y/n): ")
    if proceed.lower() == 'y':
        # Update package list first
        execute_command("sudo apt-get update", "Updating package list")
        
        for pkg in missing_deps:
            execute_command(f"sudo apt-get install -y {pkg}", f"Installing {pkg}")
    else:
        print("Skipping installation of missing dependencies. The tool may not work correctly.")

# Main function
def main():
    # Dependencies format: (package_name, command_to_check)
    dependencies = [
        ("python3-tk", "wish"),  # tk is checked via the 'wish' command
        ("git", "git"),
        ("python3", "python3"),
        ("wget", "wget"),
        ("php", "php"),
        ("openssh-client", "ssh"),
        ("jq", "jq")
    ]

    check_and_install_dependencies(dependencies)

    # Ask user for the installation directory
    try:
        import tkinter as tk
        from tkinter import filedialog
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        install_dir = filedialog.askdirectory(title="Select Installation Directory for Cypher")
    except (ImportError, RuntimeError) as e:
        print("\nCould not open a graphical file dialog.")
        print("This might be because you are in a non-GUI environment or 'python3-tk' is not properly installed.")
        install_dir = input("Please enter the full path for the installation directory: ")


    if not install_dir:
        print("No installation directory selected. Aborting.")
        return

    # Ensure the directory exists, if not, create it.
    if not os.path.isdir(install_dir):
        print(f"Directory '{install_dir}' does not exist. Creating it now.")
        try:
            os.makedirs(install_dir)
        except OSError as e:
            print(f"Error: Could not create directory {install_dir}. {e}")
            return
            
    os.chdir(install_dir)
    print(f"\nChanged working directory to {install_dir}")

    # Commands to execute for setup
    # Check if repo already cloned
    if not os.path.isdir(os.path.join(install_dir, "Cypher")):
        execute_command("git clone https://github.com/AsHfIEXE/Cypher", "Cloning Cypher repository")
    else:
        print("\nCypher repository already exists. Skipping clone.")

    # Generate SSH key if it doesn't exist
    if not os.path.exists(os.path.expanduser("~/.ssh/id_rsa")):
        execute_command("ssh-keygen -q -t rsa -N '' -f ~/.ssh/id_rsa", "Generating SSH key")
    else:
        print("SSH key already exists. Skipping generation.")

    # Change to repo directory and run
    cypher_dir = os.path.join(install_dir, "Cypher")
    if os.path.isdir(cypher_dir):
        os.chdir(cypher_dir)
        print("\nLaunching Cypher...")
        execute_command("python3 cypher.py", "Running cypher.py")
    else:
        print("Error: Cypher directory not found after cloning.")

if __name__ == "__main__":
    main()
