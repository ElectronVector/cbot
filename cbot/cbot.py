import click


@click.group()
def cli():
    pass


@click.command()
@click.argument('directory')
def new(directory):
    """ Create a new cbot project

    DIRECTORY is where the new project will be created
    """
    click.echo(f'running new on {directory}...')


cli.add_command(new)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cli()
