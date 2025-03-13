import os

# Check if the environment variable is being set from system variables
print("OPENAI_API_KEY from os.getenv:", os.getenv("OPENAI_API_KEY"))

# Check all environment variables
print("\nAll environment variables containing 'OPENAI':")
for key, value in os.environ.items():
    if "OPENAI" in key:
        print(f"{key} = {value}")
