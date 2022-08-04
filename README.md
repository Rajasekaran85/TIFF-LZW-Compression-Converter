# Project Title

TIFF LZW Compression Converter

## Description

* Convert the No Compression (raw) Images to LZW compression
* pillow library used
* wand (imagemagick) library used
* Images type: TIF

## Getting Started

### Dependencies

* Windows 7

### Installing

* pip install Pillow
* pip install wand

### Executing program

* Run the program
* Ask user to enter the path of the input image file
* Tool will create the Folder "LZW" in the same directory of input file
* LZW compression apply only for "No Compression" images.
* So tool should check the images, it is present in "No Compression" mode and then convert to LZW compression
* If any of the images not present in "No Compression" and already image in "LZW" compression, then those file list will write in the log file "output.log".
* The converted Image files will placed in the "LZW" folder


## Version History

* 0.1
    * Initial Release
