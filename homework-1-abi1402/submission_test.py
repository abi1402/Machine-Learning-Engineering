import subprocess
import pytest

def test_submission():
    result = subprocess.run([
        "jupyter", "nbconvert", 
        "--to", "notebook", 
        "--execute", "Assignment_1_2026.ipynb"
    ], capture_output=True, text=True, timeout=300)
    
    if result.returncode != 0:
        print("STDOUT:", result.stdout)
        pytest.fail(f"Notebook failed: {result.stderr}")
    print("Notebook executed successfully!")
