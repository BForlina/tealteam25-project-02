
import os
import sys

# Files that must exist
required_files = ["README.md", ".gitignore"]

# Keep a list of any missing files
missing_files = []

# Check each required file
for file in required_files:
    if not os.path.isfile(file):
        missing_files.append(file)

# If any are missing, print them and fail
if missing_files:
    print("Missing required files:")
    for file in missing_files:
        print(f" - {file}")
    sys.exit(1)  # Non-zero = fail

# If all good, pass
print("All required files are present!")
sys.exit(0)