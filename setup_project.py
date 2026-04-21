from pathlib import Path

# Define the project structure
files = {
    "README.md": "# Serverless Notes API\nA CRUD notes API built with Python + AWS Lambda + DynamoDB.\nLearning project — work in progress.\n",
    
    "PROGRESS.md": "# Progress Log\n\n## Day 1\n- Set up repo structure via Python script\n- Next: Write basic Note class with create/read functions\n",
    
    ".gitignore": "__pycache__/\n*.pyc\n.env\nvenv/\n.venv/\n.aws-sam/\n.DS_Store\n*.egg-info/\n",
    
    "requirements.txt": "",
    
    "src/notes.py": '"""Notes module — core CRUD logic."""\n',
    
    "src/__init__.py": "",
}

# Create everything
for filepath, content in files.items():
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)  # create folders if needed
    path.write_text(content)
    print(f"✓ Created {filepath}")

print("\nDone! Project structure ready.")