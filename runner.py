import subprocess
import tempfile
import os

def run_python_code(code, inputs):
    # Combine user inputs with newlines
    combined_input = '\n'.join(inputs) if inputs else ''

    # Create a temp .py file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as temp_file:
        temp_file.write(code)
        temp_filename = temp_file.name

    try:
        result = subprocess.run(
            ['python', temp_filename],
            input=combined_input,
            capture_output=True,
            text=True,
            timeout=5
        )
        output = result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        output = "[Error] Execution timed out."
    except Exception as e:
        output = f"[Error] {str(e)}"
    finally:
        os.remove(temp_filename)

    return output
