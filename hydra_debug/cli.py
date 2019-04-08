import click 
from hydra_debug import exporter, importer, run

def hydra_app(category='import'):
    def hydra_app_decorator(func):
        func.hydra_app_category = category
        return func
    return hydra_app_decorator

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

@hydra_app(category='export')
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

@hydra_app(category='import')
@cli.command(name='import')
@click.pass_obj
@click.option('-p',  '--project-id', help='Project ID')
@click.option('-f', '--data-file', help="Data File")
@click.option('-d1', '--dummy1', help='Dummy1 (String)')
@click.option('-d2', '--dummy2', help='Dummy2 (Number)')
@click.option('-d3', '--dummy3', help='Dummy3 (Number)')
@click.option('--switch-on', default=False)
@click.option('--fail', default=False)
@click.option('--data-dir', default='/tmp')
def do_import(obj, project_id, data_file, dummy1, dummy2, dummy3, switch_on, fail, data_dir):
    
    importer.do_import(project_id, data_file, dummy1, dummy2, dummy3, switch_on, fail, data_dir)

@hydra_app(category='model')
@cli.command(name='run')
@click.pass_obj
@click.option('-n',  '--network-id', help='Network ID')
@click.option('-t', '--timeout', default=5, help='How log to sleep for')
@click.option('--fail', 'fail', flag_value=True)
def do_run(obj, network_id, timeout, fail):

    run.do_run(network_id, timeout, fail)

@cli.command()
@click.pass_obj
@click.option('--all', is_flag=True, help='By default only the Export, Run, Import is registered. This flag registers the import, export and auto apps')
def register(obj, all=False):

    run.register()

    if all is True:
        importer.register()
        exporter.register()
