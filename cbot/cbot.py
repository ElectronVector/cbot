import click


@click.group()
def cli():
    pass


@click.command()
def new():
    print('running new...')


@click.command()
def module():
    print('running module...')


cli.add_command(new)
cli.add_command(module)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cli()
