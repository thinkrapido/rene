
import subprocess

def run(arr):
    cmd = ['PYTHONPATH=./src:$PYTHONPATH', 'python', '-u', '-m']
    cmd.extend(arr)
    subprocess.run(arr)

def run_examples(arr):
    cmd = ['PYTHONPATH=./src:$PYTHONPATH', 'python']
    cmd.extend(arr)
    subprocess.run(arr)

def run_dep(arr):
    cmd = ['poetry', 'run']
    cmd.extend(arr)
    subprocess.run(arr)

def run_cli(cmd):
    import sys
    argv = sys.argv
    cmd = [cmd]
    cmd.extend(argv[1:])
    subprocess.run(cmd)

def test():
    """
    Run all unittests. Equivalent to:
    `poetry run python -u -m unittest discover`
    """
    run_dep(['nose2'])

def rene():
    run_cli('./main.py')

def nuitka():
    subprocess.run(['./bin/mkexe.sh'])
    
