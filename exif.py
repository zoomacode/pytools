#!/usr/bin/env python

import argparse
import logging
import Quartz
import CoreFoundation as CF
import os, sys

class ExifProcessor(object):
    """docstring for ExifProcessor"""
    def __init__(self, verbose=0, outdir=None, dateformat='%%Y-%%m/%%Y-%%m-%%d %%H-%%M-%%S'):
        super(ExifProcessor, self).__init__()
        self.verbose = verbose
        self.outdir = outdir
        self.dateformat = dateformat
        
    def extract_exif(self, filename):
        logging.debug('extract_exif(filename="%s"', filename)
        url = CF.CFURLCreateFromFileSystemRepresentation(None, filename, len(filename), False)      
        img_src = Quartz.ImageIO.CGImageSourceCreateWithURL(url, {})
        properties = Quartz.ImageIO.CGImageSourceCopyPropertiesAtIndex(img_src, 0, None)
        result = properties[Quartz.ImageIO.kCGImagePropertyExifDictionary]
        if self.verbose > 1:
            logging.debug('exif_dump\n%s', result)
        return result

    def process_file(self, filename):
        logging.debug('process_file(filename="%s"', filename)
        absfilename = os.path.abspath(filename)
        exif = self.extract_exif(absfilename)
        date_from_exif = exif[Quartz.ImageIO.kCGImagePropertyExifDateTimeOriginal]
        logging.debug('process_file date_from_exif="%s"', date_from_exif)
        print "%s\t%s" %(filename, date_from_exif)

    def process_files(self, files):
        logging.debug('process_files()')
        for v in files:
            v = v[:-1]
            if v:
                self.process_file(v)

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs='?',
                    help="name of file with photo, if empty then use stdin")
    parser.add_argument("-d", "--outdir", action="count",
                    help='print converted name of input file in format outdir/DateTime.jpg - DateTime from --dateformat option')
    parser.add_argument("-f", "--dateformat", action="store_true",
                    help='format for --outdir option (default="%%Y-%%m/%%Y-%%m-%%d %%H-%%M-%%S"', default='%%Y-%%m/%%Y-%%m-%%d %%H-%%M-%%S')    
    parser.add_argument("-v", "--verbose", action="count",
                    help="increase output verbosity")
    args = parser.parse_args()
    if args.verbose:
        logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    else:
        logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)

    ep = ExifProcessor(args.verbose, args.outdir, args.dateformat)
    if args.filename:
        ep.process_file(args.filename)
    else:
        ep.process_files(sys.stdin)
   
if __name__ == '__main__':
    main(sys.argv)
