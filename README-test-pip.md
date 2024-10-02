pip install SimpleDSL
pip install pytest


create a test file
write test case
test_simpledsl.py

import pytest 

def test_simple_command():
	command = "python main.py example.dsl"
	result = subprocess.run(command, shell=True, capture_output=True, text=True)
	assert result.stdout.strip() == "expected_output"
	assert result.returncode == 0

if __name__ == "__main__"":
	pytest.main()

run the test
pytest test_simpledsl.py
