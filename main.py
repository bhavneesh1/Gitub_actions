import subprocess

def get_changed_files():
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD^", "HEAD"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    if result.returncode != 0:
        print("Error running git diff:", result.stderr)
        return []

    return result.stdout.strip().split("\n")

if __name__ == "__main__":
    changed_files = get_changed_files()

    print("Changed files:", changed_files)

    new_ini = "new.ini"
    new2_ini = "new2.ini"

    if new_ini in changed_files:
        print("✅ new.ini was changed")

    if new2_ini in changed_files:
        print("✅ new2.ini was changed")

    if new_ini not in changed_files and new2_ini not in changed_files:
        print("ℹ️ No relevant .ini files were changed.")
