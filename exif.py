#!/usr/bin/env python

import Quartz
import CoreFoundation as CF
import os, sys

def extract_exif(filename):
    url = CF.CFURLCreateFromFileSystemRepresentation(None, filename, len(filename), False)
  
    img_src = Quartz.ImageIO.CGImageSourceCreateWithURL(url, {})
    properties = Quartz.ImageIO.CGImageSourceCopyPropertiesAtIndex(img_src, 0, None)
    return properties[Quartz.ImageIO.kCGImagePropertyExifDictionary]

def process_file(filename):
    absfilename = os.path.abspath(filename)
    exif = extract_exif(absfilename)
    print "%s\t%s" %(filename,exif[Quartz.ImageIO.kCGImagePropertyExifDateTimeOriginal])

def main(args):
    filename = args[1]
    process_file(filename)
   
    #img_dest = Quartz.ImageIO.CGImageDestinationCreateWithURL(url, 'public.jpeg', 1, None)
    
    #exif[Quartz.ImageIO.kCGImagePropertyExifDateTimeOriginal] = u'2009:06:17 21:03:18'
     
    #Quartz.ImageIO.CGImageDestinationAddImageFromSource(\
    #           img_dest, img_src, 0, {Quartz.ImageIO.kCGImagePropertyExifDictionary: exif})
      
    #Quartz.ImageIO.CGImageDestinationFinalize(img_dest)

if __name__ == '__main__':
    main(sys.argv)
