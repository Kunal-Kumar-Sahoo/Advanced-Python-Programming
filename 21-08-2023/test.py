import subprocess

ls_process = subprocess.Popen(
    ['ls'], stdout=subprocess.PIPE,
    text=True
)

grep_process = subprocess.Popen(
    ['grep', 'test.py'],
    stdin=ls_process.stdout,
    stdout=subprocess.PIPE,
    text=True
)

output, error = grep_process.communicate()

print(output)
print(error)