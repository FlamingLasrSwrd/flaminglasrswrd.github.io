"""
Script to take raw images from sorted project folders,
    rename images to proper format,
    create smaller images suitable for a website,
    and move small images to the correct folder in website files.

Usage:
From the directory with the image files:
$ python img.py
"""

import os
import sys
from PIL import Image
from datetime import datetime

import logging
logging.basicConfig(level=logging.INFO)

# Necessary
siteImgBaseDir = '/home/user/flaminglasrswrd.github.io/assets/img'
maxImgSize = (1024,1024)
thumbnailSize = None #(128,128)

# Optional
projectImgDir = None #  specify if different than current working directory
jpegSettings = {
    'quality': 95,
    'optimize': True,
    'progression': True,
    'subsampling': '4:2:2'
}

# get project image directory name
if not projectImgDir:
    projectImgDir = os.getcwd()

# project name matches the image directory
(_,projectName) = os.path.split(projectImgDir)

# site image dir matches project dir
siteImgProjectDir = os.path.join(siteImgBaseDir, projectName)

if not os.path.isdir(siteImgProjectDir):
    logging.info(f'Created new project directory {siteImgProjectDir}')
    os.mkdir(siteImgProjectDir)

# find image files
origImages = os.listdir(projectImgDir)
processedImages = os.listdir(siteImgProjectDir)

# Remove all non jpeg files
# TODO: Use glob?
origImages = [f for f in origImages if f.lower().endswith('jpeg') or f.lower().endswith('jpg')]

# skip images that haven't been renamed yet
origImages = [f for f in origImages if not 'DSC' in f]

for origImageFilename in origImages:
    # check if already processed
    if origImageFilename in processedImages:
        logging.info(f'{origImageFilename} already processed. Skipping.')
        continue

    try:
        img = Image.open(origImageFilename)
#        with Image.open(origImageFilename) as img:
        # grab image data before anything changes
        exif = img.info.get('exif')
        iccProfile = img.info.get('icc_profile')

        if not origImageFilename.startswith(projectName):
            newFilename = projectName + '-' + origImageFilename
            os.rename(origImageFilename, newFilename)
        else:
            newFilename = origImageFilename

#TODO: color correction

        # reduce the size while maintaining aspect ratio
        logging.info(f'Reducing {newFilename} to {maxImgSize}')
        img.thumbnail(maxImgSize)
        logging.info(f'Saving {newFilename} to {siteImgProjectDir}')
        processedImagePath = os.path.join(siteImgProjectDir, newFilename)
        img.save(processedImagePath, exif=exif, icc_profile=iccProfile, **jpegSettings)

        # create actual thumbnail
        if thumbnailSize:
            img.thumbnail(thumbnailSize)
            (base, type) = newFilename.split('.')
            processedImageThumbPath = base + '.thumb' + '.' + type
            img.save(processedImageThumbPath, exif=exif, icc_profile=iccProfile, **jpegSettings, quality=75)

    except OSError:
        logging.warning(f'PIL unable to open xor save {origImageFilename}. Skipping.')
        continue

    except:
        logging.warning(f'Unknown error {origImageFilename}. Skipping.')
        continue

    finally:
        img.close()

def humanExif(PILimage):
    from PIL.ExifTags import TAGS, GPSTAGS

    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)

        data = exifdata.get(tag_id)
        # decode bytes
        if isinstance(data, bytes):
            data = data.decode()
            print(f"{tag:25}: {data}")
