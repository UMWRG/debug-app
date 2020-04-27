from time import sleep, time
from hydra_client import write_progress, write_output
import multiprocessing
from random import randint
import logging
LOG = logging.getLogger(__name__)

class Object(object):
    pass

def do_run(network_id, scenario_id, timeout=5, fail=False):
    msg = "Running Utility on Network %s, Scenario %s", network_id, scenario_id
    LOG.info("[log] %s",msg)
    write_output("[out] %s"%msg)
    runner = Runner()
    if fail is True:
        runner.fail()
    else:
        runner.wait(timeout)
    LOG.info("[log] Network Utility Run")
class Runner(object):
    def wait(self, timeout):
        """
            Wait for the specified number of seconds.
        """
        msg = "Waiting for {0} seconds".format(timeout)
        LOG.info("[log] %s",msg)
        write_output("[out] %s"%msg)

        for i in range(0, timeout):
            sleep(1)
            write_progress(i+1, timeout)

        msg = "Waiting Complete".format(timeout)
        LOG.info("[log] %s",msg)
        write_output("[out] %s"%msg)

    def fail(self):
        """
            Throw an exception, mimicing something going wrong inside an app.
        """
        msg = "Entering failure mode..."
        LOG.info("[log] %s",msg)
        write_output("[out] %s"%msg)

        raise Exception("User-forced failure")
