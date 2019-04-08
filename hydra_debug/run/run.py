#
from time import sleep
from hydra_client import write_progress

def do_run(network_id, timeout=5, fail=False):
    write_progress(1, 2) 
    if fail is True:
        raise Exception("User-forced failure")

    sleep(int(timeout))
    write_progress(2, 2) 
