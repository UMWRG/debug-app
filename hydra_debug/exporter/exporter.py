import os
import json
from hydra_client import write_progress, write_output
import logging
LOG = logging.getLogger(__name__)

def do_export(network_id, scenario_id, dummy1, dummy2, dummy3, switch_on, fail, data_dir):
    LOG.info("[log] Exporting data")
    write_output("[out] Exporting data")
    jobdetails = {
        'network_id'  : network_id,
        'scenario_id' : scenario_id,
        'dummy1'      : dummy1,
        'dummy2'      : dummy2,
        'dummy3'      : dummy3,
        'switch_on'   : switch_on,
        'fail'        : fail,
    }

    if fail is not False:
        raise Exception("Forced to fail using the 'fail' flag!")

    filepath = os.path.join(data_dir, 'DebugExport.json')
    with open(filepath, 'w') as f:
        json.dump(jobdetails, f)

    LOG.info("[log] Data Exported")
    write_output("[out] Data Exported")
