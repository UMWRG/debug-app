import click
import os
import json


@click.command()
@click.option('-n',  '--network-id', help='Network ID')
@click.option('-s',  '--scenario-id', help='Scenario ID')
@click.option('-d1', '--dummy1', help='Dummy1 (String)')
@click.option('-d2', '--dummy2', help='Dummy2 (Number)')
@click.option('-d3', '--dummy3', help='Dummy3 (Number)')
@click.option('--switch-on', default=False)
@click.option('--fail', default=False)
@click.option('--data-dir', default='/tmp')
def do_export(network_id, scenario_id, dummy1, dummy2, dummy3, switch_on, fail, data_dir):
    

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

if __name__ == '__main__':
    do_export()
