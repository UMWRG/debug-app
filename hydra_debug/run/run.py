from time import sleep, time
from hydra_client import write_progress, write_output
import multiprocessing
from random import randint
import logging
LOG = logging.getLogger(__name__)

class Object(object):
    pass

def do_run(network_id, timeout=5, fail=False, heavy_load=False):
    msg = "Calling Runner"
    write_output("[out] %s"%msg)
    LOG.info("[log] %s", msg)

    runner = Runner()
    if heavy_load is True:
        runner.do_heavy_load()
    elif fail is True:
        runner.fail()
    else:
        runner.wait(timeout)

    msg = "Finished Calling Runner"
    write_output("[out] %s"%msg)
    LOG.info("[log] %s", msg)

class Runner(object):
    def __init__(self):
        pass

    def wait(self, timeout):
        msg = "Waiting {0} seconds".format(timeout)
        write_output("[out] %s"%msg)
        LOG.info("[log] %s", msg)

        for i in range(0, timeout):
            sleep(1)
            write_progress(i+1, timeout)

        msg = "Waiting complete"
        write_output("[out] %s"%msg)
        LOG.info("[log] %s", msg)

    def fail(self):
        msg = "Forcing a user-defined failure"
        write_output("[out] %s"%msg)
        LOG.info("[log] %s", msg)
        raise Exception("User-forced failure")

    def do_heavy_load(self):
        msg = "Doing a heavy load"
        write_output("[out] %s"%msg)
        LOG.info("[log] %s", msg)

        processes=[]
        for i in range(0,4):
            process = Object()
            process.name = "process_{}".format(i)

            processes.append(multiprocessing.Process(name=process.name,
                                                     target=self._run_process,
                                                     args=(process,)))

        for p in processes:
            p.start()

        for p in processes:
            p.join()

        msg = "Heavy Load Done"
        write_output("[out] %s"%msg)
        LOG.info("[log] %s", msg)

    def _run_process(self, process=None):
        write_output("v.0.2 - Running "+ str(process.name))
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

        msg = "End Process {} for a total of {} cycles".format(str(process.name),a)
        write_output("[out] %s"%msg)
        LOG.info("[log] %s", msg)
