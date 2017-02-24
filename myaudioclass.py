#!/usr/bin/python -d
# -*- coding: utf-8 -*-

# Path to files....
# H:\PYTHON_PROGRAMS\PySignalGenerator\ 

import math
import numpy
try:
    import pyaudio
except:
    print "Requires PYAUDIO library, Please install it from"
    print "https://people.csail.mit.edu/hubert/pyaudio/"
        


def sine(frequency, length, rate):
    length = int(length * rate)
    factor = float(frequency) * (math.pi * 2) / rate
    return numpy.sin(numpy.arange(length) * factor)


def play_tone(stream, frequency=440, length=1, rate=44100):
    chunks = []
    chunks.append(sine(frequency, length, rate))
    chunk = numpy.concatenate(chunks) * 0.25
    stream.write(chunk.astype(numpy.float32).tostring())
    
    
def playmysound(frequency,length):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,channels=1, rate=44100, output=1)
    play_tone(stream, frequency, length)
    stream.close()
    p.terminate()   