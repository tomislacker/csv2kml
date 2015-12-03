# CSV to KML Converter

## About
***@TODO***

## Usage
### Install

```sh
git clone git@github.com:tomislacker/csv2kml.git && cd csv2kml
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

### Help

```sh
$ ./csv2kml.py -h

This utility will spit out a KML file from a CSV of locations

Usage:
    csv2kml.py [options]

Options:
    -c, --csv FILE      Input CSV
    -o, --output FILE   Ouput KML (Default stdout)
    -n, --name INDEX    Column index for name
    -l, --lat INDEX     Column index for latitude
    -L, --long INDEX    Column index for longitude
```

