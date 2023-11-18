import click

import cbot.build_command
import cbot.run_command
import cbot.module_command
import cbot.new_command


@click.group()
def cli():
    pass


cli.add_command(cbot.new_command.new)
cli.add_command(cbot.build_command.build)
cli.add_command(cbot.run_command.run)
cli.add_command(cbot.module_command.module)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cli()
