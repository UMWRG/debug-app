import os
from hydra_client import write_progress, write_output
import logging
LOG = logging.getLogger(__name__)

def do_import(project_id, dummy1, dummy2, dummy3, switch_on, fail, data_dir, data_file_1=None, data_file_2=None):
    """
        This debug app get 2 files as input
    """


    msg = "Importing data"
    write_output("[out] %s"% msg)
    LOG.info("[log] %s", msg)

    files = []

    if data_file_1 is None:
        raise Exception("Missing file 1")

    if not os.path.isfile(data_file_1):
        raise Exception(f"The provided filepath 1 ''{data_file_1}'' does not exists")

    files.append(data_file_1)

    if data_file_2 is None:
        raise Exception("Missing file 2")

    if not os.path.isfile(data_file_2):
        raise Exception(f"The provided filepath 2 ''{data_file_2}'' does not exists")

    files.append(data_file_2)


    for file in files:
        #Read the supplied file and save it to data_dir
        with open(file, 'r') as infile:

            filename = infile.name.split(os.sep)[-1]

            outfile_path = os.path.join(data_dir, filename)

            with open(outfile_path, 'w') as outfile:
                outfile.write(infile.read())
                outfile.write("This content has been proudly updated by the debug-app import APP!\n\n")
    msg = "Data Imported"
    write_output("[out] %s"% msg)
    LOG.info("[log] %s", msg)
