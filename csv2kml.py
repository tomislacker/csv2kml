#!/usr/bin/env python
"""

This utility will spit out a KML file from a CSV of locations

Usage:
    csv2kml.py [options]

Options:
    -c, --csv FILE      Input CSV
    -o, --output FILE   Ouput KML (Default stdout)
    -n, --name INDEX    Column index for name
    -l, --lat INDEX     Column index for latitude
    -L, --long INDEX    Column index for longitude
"""
import csv
import os
import pwd
import time
from lxml import etree
from pykml.factory import KML_ElementMaker as KML

CSV_PATH = "test.csv"
KML_PATH = "test.kml"
CSV_INDEX_NAME = 0
CSV_INDEX_LAT = 1
CSV_INDEX_LONG = 2


def get_username():
    return pwd.getpwuid(os.getuid())[0]


def get_comment(csv_name):
    return "Prepared by @{username} at {stamp} from '{csv}'".format(
        username=get_username(),
        stamp=time.ctime(),
        csv=csv_name
    )


def get_csv_doc(csv_path, index_name=None, index_lat=None, index_long=None,
                altitude=0):
    index_name = int(index_name) or CSV_INDEX_NAME
    index_lat = int(index_lat) or CSV_INDEX_LAT
    index_long = int(index_long) or CSV_INDEX_LONG

    print "Indexes: {n}, {l}, {L}".format(
        n=index_name,
        l=index_lat,
        L=index_long
    )
    print "Reading from '{c}'".format(c=csv_path)

    doc = KML.kml(KML.Document(
        KML.name("Property List"),
        etree.Comment(get_comment(csv_path)),
        KML.Style(
            KML.IconStyle(
                KML.scale(1.0),
                KML.Icon(
                    KML.href("http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png"),
                ),
                id="mystyle"
            ),
            id="pushpin"
        ),
    ))

    with open(csv_path, 'r') as csvin:
        reader = csv.reader(csvin)
        for row in reader:
            print "'{}' @ ({}, {})".format(
                row[index_name],
                row[index_lat],
                row[index_long]
            )

            doc.append(KML.Placemark(
                KML.name(row[index_name]),
                KML.Point(
                    KML.altitudeMode('relativeToGround'),
                    KML.styleUrl("#pushpin"),
                    KML.coordinates("{},{},{}".format(
                        row[index_long],row[index_lat], altitude
                    ))
                )
            ))

    return doc

if __name__ == '__main__':
    from docopt import docopt
    args = docopt(__doc__)

    kmldoc = get_csv_doc(
        args['--csv'],
        args['--name'],
        args['--lat'],
        args['--long'])

    if not args['--output']:
        # Print to stdout
        print etree.tostring(etree.ElementTree(kmldoc), pretty_print=True)
    else:
        # Write to file
        print "Writing to '{k}'".format(k=args['--output'])
        with open(args['--output'], 'w') as kmlout:
            kmlout.write(etree.tostring(etree.ElementTree(kmldoc),
                                        pretty_print=True))
