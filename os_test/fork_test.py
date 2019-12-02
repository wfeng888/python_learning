import os,sys,time,subprocess

def fork_test():
    pass

def subprocess_test():
    subprocess.


if sys.platform == 'linux' :
    new_process = fork_test
elif sys.platform.startswith('win'):
    new_process = subprocess_test

if __name__ == '__main__':
