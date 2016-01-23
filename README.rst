======================
raspberrypi_muon_microscope
======================
Acquire RAW images with Raspberry Pi camera (before demosaicking) with the
purpose of looking for muon traces. The sensor is in the dark, colour filters
are unimportant, so this uses the full resolution of 1944 x 2592.

With inspiration from the Camera Particle Detector (Magdalen College School). Based on the raw Bayer capture method of 
Michael Hirsch https://scivision.co

.. contents::

Prereqs
=======
::
    
    sudo apt-get install python3-scipy python3-picamera

Examples
========
There are more efficient ways to do this.

Would like to get better control of fixed exposure times.

RAW Bayer filtered image stream displayed on screen via Matplotlib
--------------------------------------------------------------------------------
::

    ./getrawimage.py -p

RAW Bayer filtered image save to disk
---------------------------------------------
::

    ./getrawimage.py out.png

Command-Line Options
===================

-p                      use Matplotlib for live (5 seconds per frame) display
-e exp_sec      manually set exposure time, up to one second (TODO there are still some auto-set gains)
-8                      output 8-bit array instead of default 10-bit array


Reference
========
In contrast to the 3-D array returned by the `picamera.array.PiBayerArray method <http://picamera.readthedocs.org/en/release-1.10/_modules/picamera/array.html#PiArrayOutput>`_ method, 
Hirsch's program collects the raw Bayer data and puts it into a  2-D matrix (not demosaicked). 
The sensor contains 1944 x 2592 pixels. Pixel size is 1.4 x 1.4 micrometer.

The program writes images of 50x50 pixels to disc, centered on the brightest pixel. Close to the edges, the area is reduced.
