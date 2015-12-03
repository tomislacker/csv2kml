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

## References
- [[PythonHosted.org] Welcome to pyKML](http://pythonhosted.org/pykml/)
- [[igismap.com] Upload KML File on Google Maps](http://www.igismap.com/upload-kml-file-google-map/)
- [[display-kml.appspot.com] View Your KML Directly on a Google Map](http://display-kml.appspot.com/)
- [[docs.pythong.org] 19.7 xml.etree.ElementTree](https://docs.python.org/2/library/xml.etree.elementtree.html#)
