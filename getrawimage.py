#!/usr/bin/env python3
"""
Demo of reading raw Bayer 10-bit data from Raspberry Pi camera chip using PiCamera module.
Notes:
1) can only read full chip, no binning or ROI: 2592x1944 pixel image with current imaging chip
2) captures a single image
3) sudo apt-get install python3-picamera python3-scipy

Basis from Michael Hirsch https://scivision.co
Inspiration from Camera Particle Detector (Magdalen College School) 

Pieter Kuiper
"""
from __future__ import division,absolute_import
from time import sleep,time
from scipy.misc import bytescale,imsave
from matplotlib.pyplot import figure,draw,pause

#
from picamera import PiCamera
#
from params import getparams,setparams
from rawbayer import grabframe

def pibayerraw(fn,exposure_sec,bit8):
    with PiCamera() as cam: #load camera driver
        print('camera startup gain autocal')
        #LED automatically turns on, this turns it off
        cam.led = False
        sleep(0.75) # somewhere between 0.5..0.75 seconds to let camera settle to final gain value.
        setparams(cam,exposure_sec) #wait till after sleep() so that gains settle before turning off auto
        getparams(cam)
        counter = 1
#%% main loop
        while True:
#            tic = time()
            img10 = grabframe(cam)
#            print('{:.1f} sec. to grab frame'.format(time()-tic))
#%% linear scale 10-bit to 8-bit
            if bit8:
                img = bytescale(img10,0,1024,255,0)
            else:
                img = img10
#%% write to PNG or JPG or whatever based on file extension
            max_value = img.max()
            print(max_value)
            if max_value > 100:
                imsave(fn+'%03d' % counter +'.png',img)
                counter = counter + 1
#                break
    return img
if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='Raspberry Pi Picamera demo with raw Bayer data')
    p.add_argument('-e','--exposure',help='exposure time [seconds]',type=float)
    p.add_argument('-8','--bit8',help="convert output to 8-bit",action='store_true')
    p.add_argument('filename',help='output filename to write [png,jpg]',nargs='?')
    p = p.parse_args()
   
    try:
        print('press Ctrl c  to end program')
        img = pibayerraw(p.filename, p.exposure,p.bit8)
    except KeyboardInterrupt:
        pass
