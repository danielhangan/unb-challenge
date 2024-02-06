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
cd unb-challenge
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
The cli only accepts a list of objects in a json file format.
Example:
```json
[
  {
    "timestamp": "2018-12-26 18:11:08.509654",
    "translation_id": "5aa5b2f39f7254a75a00",
    "source_language": "fr",
    "target_language": "de",
    "client_name": "fast-delivery",
    "event_name": "translation_failed",
    "nr_words": 78,
    "duration": 30
  },
  {
    "timestamp": "2018-12-26 18:11:20.509654",
    "translation_id": "5aa5b2f39f7254a75a01",
    "source_language": "fr",
    "target_language": "en",
    "client_name": "hotel-paradise",
    "event_name": "translation_started",
    "nr_words": 75,
    "duration": 30
  }
]
```
The window size should be between `10` and `25`. Otherwise it will throw an error.

## Testing

Just run the following command in your terminal

```bash
pytest
```
