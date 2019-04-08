import click

from time import sleep

@click.command()
@click.option('-n',  '--network-id', help='Project ID')
@click.option('-t', '--timeout', help='How log to sleep for')
@click.option('--fail', 'fail', flag_value=True)
def do_run(network_id, timeout, fail):
    
    if fail is True:
        raise Exception("User-forced failure")

    sleep(int(timeout))

if __name__ == '__main__':
    do_run()
