import Quartz
import CoreFoundation as CF
import os, sys

def main(args):
    filename = os.path.abspath(sys.argv[1]) 
    url = CF.CFURLCreateFromFileSystemRepresentation(None, filename, len(filename), False)
  
    img_src = Quartz.ImageIO.CGImageSourceCreateWithURL(url, {})
    properties = Quartz.ImageIO.CGImageSourceCopyPropertiesAtIndex(img_src, 0, None)
    exif = properties[Quartz.ImageIO.kCGImagePropertyExifDictionary]
   
    img_dest = Quartz.ImageIO.CGImageDestinationCreateWithURL(url, 'public.jpeg', 1, None)
    
    #exif[Quartz.ImageIO.kCGImagePropertyExifDateTimeOriginal] = u'2009:06:17 21:03:18'
     
    #Quartz.ImageIO.CGImageDestinationAddImageFromSource(\
    #           img_dest, img_src, 0, {Quartz.ImageIO.kCGImagePropertyExifDictionary: exif})
      
    #Quartz.ImageIO.CGImageDestinationFinalize(img_dest)

if __name__ == '__main__':
    main(sys.argv)
