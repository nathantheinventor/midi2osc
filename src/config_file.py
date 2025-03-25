from pathlib import Path

import pydantic
import yaml

CONFIG_FILE = Path(__file__).parent / "config.yaml"


class Message(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(use_attribute_docstrings=True, frozen=True)

    midi: str
    """The MIDI message to listen for"""
    osc: str
    """The OSC message to send. Use `:note` to insert the MIDI value."""


class Config(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(use_attribute_docstrings=True, frozen=True)

    midi_name: str
    """The name of the MIDI device to expose to Proclaim or other software"""
    osc_address: str
    """IP Address of the OSC server"""
    osc_port: int
    """Port of the OSC server"""
    messages: list[Message]
    """List of messages to listen for and send"""


def get_config() -> Config | None:
    """Get the current configuration."""
    if not CONFIG_FILE.exists():
        return None
    return Config.model_validate(yaml.safe_load(CONFIG_FILE.read_text()))


def save_config(config: Config) -> None:
    """Save the configuration."""
    CONFIG_FILE.write_text(yaml.dump(config.model_dump()))
