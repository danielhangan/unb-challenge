# Unbabel CLI

This is a command-line tool that calculates the moving average of 'translation_delivered' events.

## Installation

This tool is packaged using setuptools, which allows you to install it and run it as a command-line tool.

1. Clone the repository:

```bash
git clone https://github.com/danielhangan/unb-challenge.git
```

2. Navigate to the cloned directory:

```bash
cd unbabel_cli
```

3. Install the package. It's recommended to use a virtual environment:

```bash
python3 -m venv env
. env/bin/activate
pip3 install -r requirements.txt
pip3 install -e .
```

## Usage

```bash
unbabel_cli --input_file events.json --window_size 10
```

Replace events.json with the path to your actual input file.

## Testing

Just run the following command in your terminal

```bash
pytest
```
