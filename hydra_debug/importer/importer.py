import os
from hydra_client import write_progress, write_output
import logging
LOG = logging.getLogger(__name__)

def do_import(project_id, data_file, dummy1, dummy2, dummy3, switch_on, fail, data_dir):
    msg = "Importing data"
    write_output("[out] %s"% msg)
    LOG.info("[log] %s", msg)
    if data_file is None:
        raise Exception("No file specified")

    #Read the supplied file and save it to data_dir
    with open(data_file, 'r') as infile:

        filename = infile.name.split(os.sep)[-1]

        outfile_path = os.path.join(data_dir, filename)

        with open(outfile_path, 'w') as outfile:
            outfile.write(infile.read())

    msg = "Data Imported"
    write_output("[out] %s"% msg)
    LOG.info("[log] %s", msg)
