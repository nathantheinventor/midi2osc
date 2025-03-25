import click

@click.command()
def config():
    click.echo("config")
    ...

@click.group()
def cli():
    click.echo("Hello, World!")
    pass

cli.add_command(config)