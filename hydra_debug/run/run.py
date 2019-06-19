from time import sleep
from hydra_client import write_progress
import multiprocessing
from random import randint

class Object(object):
    pass

def do_run(network_id, timeout=5, fail=False, heavy_load=False):
    runner = Runner()
    if heavy_load is True:
        runner._do_heavy_load()
    else:
        runner.wait(timeout)

class Runner(object):
    def __init__(self):
        pass

    def wait(self, timeout):
        write_progress(1, 2)
        if fail is True:
            raise Exception("User-forced failure")
        sleep(int(timeout))
        write_progress(2, 2)

    def _do_heavy_load(self):
        mpc=multiprocessing.cpu_count()

        processes=[]
        for i in range(0,4):
            process = Object()
            process.name = "process_{}".format(i)

            processes.append(multiprocessing.Process(name=process.name, target=self._run_process, args=(process,)))

        for p in processes:
            p.start()

        for p in processes:
            p.join()

    def _run_process(self, process=None):
        print("v.0.2 - Running "+ str(process.name))
        a=0
        st=100000000
        limit=randint(st / 10,2*st)
        while a<limit:
            a = a + 1

        print("End Process {} for a total of {} cycles".format(str(process.name),a))
