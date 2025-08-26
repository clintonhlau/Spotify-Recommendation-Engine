from dotenv import load_dotenv
import os
from pathlib import Path

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
env_path = os.path.join(project_root, ".env")
load_dotenv(env_path)

print(os.getenv("SPOTIFY_CLIENT_ID"))
print(os.getenv("SPOTIFY_CLIENT_SECRET"))