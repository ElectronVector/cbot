import subprocess
from pathlib import Path
import click
import cbot.defaults


@click.group()
def test():
    """ Run the tests.
    """
    click.echo(f"Running tests...")


@click.command()
def generate_runners():
    click.echo('Generating runners...')


test.add_command(generate_runners)
