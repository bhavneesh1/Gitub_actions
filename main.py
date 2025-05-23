import os
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
