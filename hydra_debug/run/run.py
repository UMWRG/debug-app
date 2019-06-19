from time import sleep, time
from hydra_client import write_progress
import multiprocessing
from random import randint

class Object(object):
    pass

def do_run(network_id, timeout=5, fail=False, heavy_load=False):
    runner = Runner()
    if heavy_load is True:
        runner._do_heavy_load()
    elif fail is True:
        runner._fail()
    else:
        runner.wait(timeout)

class Runner(object):
    def __init__(self):
        pass

    def wait(self, timeout):
        #write_progress(1, 2)
        for i in range(0, timeout):
            sleep(1)
            write_progress(i+1, timeout)

    def _do_fail(self):
        #write_progress(1, 2)
        raise Exception("User-forced failure")

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

        start_time=time()

        while a<limit:
            a = a + 1
            current_time=time()
            if current_time > start_time+1:
                print(process.name)
                write_progress(a, limit)
                start_time=current_time

        print("End Process {} for a total of {} cycles".format(str(process.name),a))
