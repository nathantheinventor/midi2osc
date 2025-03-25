import click

from config import config
from config_file import get_config
from run import run


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx: click.Context):
    """Main function of the CLI"""
    if ctx.invoked_subcommand:
        return
    if get_config() is None:
        config()
    else:
        run()


cli.add_command(config)
cli.add_command(run)
