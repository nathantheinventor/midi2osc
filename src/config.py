import click

from config_file import Message, save_config, Config


@click.command()
@click.option("--midi-name", type=str)
@click.option("--osc-address", type=str)
@click.option("--osc-port", type=int)
@click.option("--midi-command", type=str)
@click.option("--osc-command", type=str)
def config(
    midi_name: str | None,
    osc_address: str | None,
    osc_port: int | None,
    midi_command: str | None,
    osc_command: str | None,
):
    """Command to set up the config file"""
    if midi_name is None:
        midi_name = click.prompt("MIDI Name")
    if osc_address is None:
        osc_address = click.prompt("OSC Address")
    if osc_port is None:
        osc_port = click.prompt("OSC Port", type=int, default=8005)

    midi_command = midi_command or click.prompt("MIDI Message", default="note_on")
    osc_command = osc_command or click.prompt("OSC Message (use :note/:channel/etc. to insert the MIDI value)")
    assert midi_command and osc_command
    messages = [Message(midi=midi_command, osc=osc_command)]
    while click.confirm("Add another message?", default=False):
        messages.append(Message(midi=click.prompt("MIDI Message"), osc=click.prompt("OSC Message")))

    assert midi_name and osc_address and osc_port
    save_config(Config(midi_name=midi_name, osc_address=osc_address, osc_port=osc_port, messages=messages))
    click.echo("Configuration saved")
