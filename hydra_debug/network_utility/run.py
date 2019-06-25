from time import sleep, time
from hydra_client import write_progress, write_output
import multiprocessing
from random import randint

class Object(object):
    pass

def do_run(network_id, scenario_id, timeout=5, fail=False):
    write_output("Running Utility on Network {0}, Scenario {1}".format(network_id, scenario_id))
    runner = Runner()
    if fail is True:
        runner.fail()
    else:
        runner.wait(timeout)

class Runner(object):
    def wait(self, timeout):
        """
            Wait for the specified number of seconds.
        """
        write_output("Waiting for {0} seconds".format(timeout))
        for i in range(0, timeout):
            sleep(1)
            write_progress(i+1, timeout)
        write_output("Waiting Complete")

    def fail(self):
        """
            Throw an exception, mimicing something going wrong inside an app.
        """
        write_progress("Entering failure mode...")
        raise Exception("User-forced failure")
