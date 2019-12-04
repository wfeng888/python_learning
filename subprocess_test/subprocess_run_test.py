#!  /usr/local/bin/python3
import  subprocess,selectors

# def run(*popenargs,input=None, capture_output=False, timeout=None, check=False, **kwargs)
sel = selectors.DefaultSelector()
def subprocess_run_test():
    proc = subprocess.Popen('ssh mysql@mysql2',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE,
                   stderr=subprocess.STDOUT);
    sel.register(proc.stdout,selectors.EVENT_READ)
    sel.register(proc.stdin,selectors.EVENT_WRITE)
    while True:
        events = sel.select()
        for key,mask in events:
            data=key.fd.read()
            print(data)
        sel.unregister(proc.stdout)
        break;
if __name__=='__main__':
    subprocess_run_test()