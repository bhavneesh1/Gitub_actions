
import subprocess
import requests
if __name__ == "__main__":
    # Get list of changed files in the last commit
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD^", "HEAD"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    print(result)
    changed_files = result.stdout.strip().split("\n")
    ini_files = [f for f in changed_files if f in ["new.ini", "new2.ini"]]

    if not ini_files:
        print("No relevant .ini files changed.")
        exit(0)

    for ini_file in ini_files:
        if ini_file == "new.ini":
            print("this is new ")
        elif ini_file == "new.ini":
            print("this is new2 ")
        else:
            print("none file modified")
