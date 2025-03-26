# pyright: basic
import click
import mido
from pythonosc import udp_client

from config_file import get_config


@click.command()
def run():
    """Command to run the process"""
    config = get_config()
    assert config is not None, "No config file found"
    click.echo("Running")
    client = udp_client.SimpleUDPClient("192.168.1.77", 8005)

    with mido.open_input(name=config.midi_name, virtual=True) as midi_port:  # pyright: ignore[reportAttributeAccessIssue]
        for msg in midi_port:
            click.echo(f"Received message {msg}")
            for message in config.messages:
                if message.midi == msg.type:
                    osc_command = message.osc
                    for param, value in msg.dict().items():
                        osc_command = osc_command.replace(f":{param}", str(value))
                    click.echo(f"Sending message {osc_command}")
                    client.send_message(osc_command, 0)
