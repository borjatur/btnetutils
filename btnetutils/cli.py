"""Console script for btnetutils."""
import sys
import click
from btnetutils.btnetutils import get_my_ip


@click.group()
def btnet(args=None):
    """
    Simple CLI for dealing with net configs
    """
    pass

@btnet.command()
def ip():
    """
    return your current external ip
    """
    click.echo(get_my_ip())

if __name__ == "__main__":
    sys.exit(btnet())
