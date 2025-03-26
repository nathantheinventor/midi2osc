# MIDI to OSC

This is a simple Python script that recieves MIDI messages and sends them as OSC messages. It uses the `mido` and `python-osc` libraries.
The main purpose of this script is to interface between my church's slide presentation software, Proclaim, and my church's lighting control board, a ColorSource AV 20.

## Installation

This app can be installed simply with `pipx` or `pip` (First you must install [Python 3.12+](https://www.python.org/downloads/) and [pipx](https://pipx.pypa.io/stable/installation/)):

```bash
pipx install midi2osc

# To run the app:
midi2osc
```

The first time you run the app, it will prompt you for configuration, which it will save in a `config.yaml` file alongside the code. This config file takes the following structure:

```yaml
midi_name: "MIDI Device Name"  # The name of the MIDI device to expose to Proclaim or other software
osc_address: "1.2.3.4" # IP address of the OSC server
osc_port: 8005 # Port of the OSC server
messages:
  - midi: "note_on" # The MIDI message to listen for
    osc: "/cs/playback/gotocue/:note" # The OSC message to send; will replace `:note`/`:channel`/etc. with the parameter sent in the MIDI message
```
