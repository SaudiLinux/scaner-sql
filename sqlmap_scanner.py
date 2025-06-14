import subprocess
import os

def run_sqlmap_on_file(file_path):
    """
    Runs sqlmap on a list of URLs from a given file.

    Args:
        file_path (str): The absolute path to the file containing URLs.
    """
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    # Assuming sqlmap is in your system's PATH
    # You might need to specify the full path to sqlmap.py if it's not in PATH
    # e.g., sqlmap_command = ['python', '/path/to/sqlmap.py', '-m', file_path, '--batch']
    sqlmap_command = ['sqlmap', '-m', file_path, '--batch', '--random-agent', '--level=5', '--risk=3']

    print(f"[*] Running sqlmap on URLs from: {file_path}")
    print(f"[*] Command: {' '.join(sqlmap_command)}")

    try:
        # Start the process
        process = subprocess.Popen(sqlmap_command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, bufsize=1, universal_newlines=True)

        # Print output line by line
        for line in process.stdout:
            print(line, end='')
        
        process.wait()

        if process.returncode == 0:
            print("\n[*] sqlmap scan completed successfully.")
        else:
            print(f"\n[!] sqlmap scan finished with errors. Exit code: {process.returncode}")

    except FileNotFoundError:
        print("[!] Error: sqlmap command not found. Make sure sqlmap is installed and in your system's PATH.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

if __name__ == "__main__":
    # Use the urls.txt.txt file found in your workspace
    # It's better to rename it to urls.txt for clarity
    urls_file = r"c:\Users\Dell\Desktop\code\urls.txt.txt"
    
    # You can change this to prompt the user for the file path if needed
    # urls_file = input("Enter the path to the file containing URLs: ")
    
    run_sqlmap_on_file(urls_file)