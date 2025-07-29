# AnimCLI

**AnimCLI** is a simple CLI tool that converts GIFs into ASCII animations for the terminal.

## Installation

Install via PyPI:

```bash
pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ animcli
```

## Usage

### List GIFs

```bash
animcli --list
```

### Convert GIF to ASCII

```bash
animcli --gif <gif-name> --cycles <cycles> --duration <frame-duration> --width <width> --columns <columns>
```

### Example

List GIFs:

```bash
animcli --list
```

Convert a GIF:

```bash
animcli --gif "lisa_dance"
```