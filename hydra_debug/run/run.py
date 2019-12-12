from time import sleep, time
from hydra_client import write_progress, write_output
import multiprocessing
from random import randint

class Object(object):
    pass

def do_run(network_id, timeout=5, fail=False, heavy_load=False, data_file=None):
    runner = Runner(network_id)
    if heavy_load is True:
        runner.do_heavy_load()
    elif fail is True:
        runner.fail()
    elif data_file is not None:
        runner.manage_file(data_file)
    else:
        runner.wait(timeout)

class Runner(object):
    def __init__(self, network_id = 0):
        self.network_id = network_id

    def manage_file(self, data_file):
        write_output(data_file)
        path=os.path.dirname(data_file)
        while path != "":
            write_output(path)
            new_path=os.path.dirname(path)
            if new_path == path:
                break
            new_path=path
        # if not os.path.isfile(data_file_1):
        #     raise Exception(f"The provided filepath 1 ''{data_file_1}'' does not exists")

    def wait(self, timeout):
        write_output("Waiting {0} seconds".format(timeout))
        for i in range(0, timeout):
            sleep(1)
            write_progress(i+1, timeout)
        write_output("Waiting Complete")

    def fail(self):
        write_output("Forcing a user-defined failure")
        raise Exception("[Network ID: {}] - User-forced failure".format(self.network_id))

    def do_heavy_load(self):

        processes=[]
        for i in range(0,4):
            process = Object()
            process.name = "process_{}".format(i)

            processes.append(multiprocessing.Process(name=process.name, target=self._run_loop_process, args=(process,)))

        for p in processes:
            p.start()

        for p in processes:
            p.join()

    def _run_loop_process(self, process=None):
        print("[Network ID: {}] v.0.2 - Running {}".format(self.network_id, process.name))
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

        print("[Network ID: {}] End Process {} for a total of {} cycles".format(self.network_id, str(process.name),a))
