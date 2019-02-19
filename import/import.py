import hydra_base as hb
import click

import hydra_base as hb
import click
import os
import json


@click.command()
@click.option('-p',  '--project-id', help='Project ID')
@click.option('-f', '--data-file', help="Data File")
@click.option('-d1', '--dummy1', help='Dummy1 (String)')
@click.option('-d2', '--dummy2', help='Dummy2 (Number)')
@click.option('-d3', '--dummy3', help='Dummy3 (Number)')
@click.option('--switch-on', default=False)
@click.option('--fail', default=False)
@click.option('--data-dir', default='/tmp')
def do_import(project_id, data_file, dummy1, dummy2, dummy3, switch_on, fail, data_dir):

        
    #Read the supplied file and save it to data_dir
    with open(data_file, 'r') as infile:

        filename = infile.name.split(os.sep)[-1]

        outfile_path = os.path.join(data_dir, filename)

        with open(outfile_path, 'w') as outfile:
            outfile.write(infile.read())

if __name__ == '__main__':
    do_import()
