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
            if mask == selectors.EVENT_READ:
                data=key.fileobj.read()
                print(data)
            else:
                key.fileobj.write(b'wait')
        sel.unregister(proc.stdout)
        sel.unregister(proc.stdin)
        break;
if __name__=='__main__':
    subprocess_run_test()