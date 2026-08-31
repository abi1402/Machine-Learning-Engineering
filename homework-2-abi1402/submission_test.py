import os
import subprocess


def test_submission():
    os.environ["NUM_EPOCHS"] = "1"

    result = subprocess.run(
        ["jupyter", "nbconvert", "--to", "notebook", "--execute", "Assignment_2_2026.ipynb"],
        capture_output=True,
        text=True
    )

    assert result.returncode == 0