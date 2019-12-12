import click
from hydra_debug import exporter, importer, run, network_utility
from hydra_client.click import hydra_app, make_plugins, write_plugins

@click.group()
@click.pass_obj
@click.option('-u', '--username', type=str, default=None)
@click.option('-p', '--password', type=str, default=None)
@click.option('-h', '--hostname', type=str, default=None)
@click.option('-s', '--session', type=str, default=None)
def cli(obj, username, password, hostname, session):
    """ CLI for the GAMS-Hydra application. """

    obj['hostname'] = hostname
    obj['username'] = username
    obj['password'] = password
    obj['session']  = session

def start_cli():
    cli(obj={}, auto_envvar_prefix='HYDRA_DEBUG')

@hydra_app(category='export', name="Debug Export")
@cli.command(name='export')
@click.pass_obj
@click.option('-n',  '--network-id', help='Network ID')
@click.option('-s',  '--scenario-id', help='Scenario ID')
@click.option('-d1', '--dummy1', help='Dummy1 (String)')
@click.option('-d2', '--dummy2', help='Dummy2 (Number)')
@click.option('-d3', '--dummy3', help='Dummy3 (Number)')
@click.option('--switch-on', default=False)
@click.option('--fail', default=False)
@click.option('--data-dir', default='/tmp')
def do_export(obj, network_id, scenario_id, dummy1, dummy2, dummy3, switch_on, fail, data_dir):
    exporter.do_export(network_id, scenario_id, dummy1, dummy2, dummy3, switch_on, fail, data_dir)

@hydra_app(category='import', name="Debug Import")
@cli.command(name='import')
@click.pass_obj
@click.option('-p',  '--project-id', help='Project ID')
@click.option('-f1', '--data-file-1', help="Data File 1")
@click.option('-f2', '--data-file-2', help="Data File 2")
@click.option('-d1', '--dummy1', help='Dummy1 (String)')
@click.option('-d2', '--dummy2', help='Dummy2 (Number)')
@click.option('-d3', '--dummy3', help='Dummy3 (Number)')
@click.option('--switch-on', default=False)
@click.option('--fail', default=False)
@click.option('--data-dir', default='/tmp')
def do_import(obj, project_id, dummy1, dummy2, dummy3, switch_on, fail, data_dir, data_file_1=None, data_file_2=None):

    importer.do_import(project_id, dummy1, dummy2, dummy3, switch_on, fail, data_dir, data_file_1=data_file_1, data_file_2=data_file_2)

@hydra_app(category='model', name="Debug Run")
@cli.command(name='run')
@click.pass_obj
@click.option('-n',  '--network-id', help='Network ID')
@click.option('-f', '--data-file', help="Data File")
@click.option('-t', '--timeout', default=5, help='How log to sleep for')
@click.option('--fail', 'fail', flag_value=True)
@click.option('--heavy-load', 'heavy_load', flag_value=True)
def do_run(obj, network_id, timeout, fail, heavy_load, data_file=None):

    run.do_run(network_id, timeout, fail, heavy_load,data_file=data_file)

@hydra_app(category='network_utility', name="Debug Network Utility")
@cli.command(name='netutil')
@click.pass_obj
@click.option('-n',  '--network-id', help='Network ID')
@click.option('-s',  '--scenario-id', help='Scenario ID')
@click.option('-t', '--timeout', default=5, help='How log to sleep for')
@click.option('--fail', 'fail', flag_value=True)
def do_run(obj, network_id, scenario_id, timeout, fail):
    """
        An app with mainly similar functionality to the 'run' (pauses for a few seconds)
        except that it is in the 'network_utility' category, which allows it to be
        placed in a dedicated place in side HWI. Examples of use would be to update
        all the nodes in an existing network, upload partial data (for example updating all
        inflows) etc.
    """

    network_utility.do_run(network_id, scenario_id, timeout, fail)

@cli.command()
@click.pass_obj
@click.argument('docker-image', type=str, required=False)
def register(obj, docker_image):
    """ Register the app with the Hydra installation. """
    app_name = 'hydra-debug'

    if docker_image:
        plugins = make_plugins(cli, 'hydra-debug', docker_image=docker_image)
    else:
        plugins = make_plugins(cli, 'hydra-debug', docker_image=docker_image)

    write_plugins(plugins, app_name)
