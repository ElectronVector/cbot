import click

import cbot.build_command
import cbot.run_command
from cbot.new_command import new


@click.group()
def cli():
    pass


cli.add_command(cbot.new_command.new)
cli.add_command(cbot.build_command.build)
cli.add_command(cbot.run_command.run)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cli()
