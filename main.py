#!/usr/bin/python -d
# -*- coding: utf-8 -*-

# H:\PYTHON_PROGRAMS\PySignalGenerator\main.py

# GUI INTERFACE INCLUDES:
# label
# label_2
# label_3
# label_4
# pushButton
# pushButton_2
# pushButton_3
# verticalSlider




import myaudioclass
from PyQt4 import QtCore, QtGui
from maingui import Ui_Form 
import sys




#Global variable
counter = 0

class MyForm(QtGui.QMainWindow):

  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_Form()
    self.ui.setupUi(self)
    
    self.ctimer = QtCore.QTimer() # constant timer
    #self.ctimer.stop()
    #self.ctimer.start(duration)
    # Generates an event when the timer rolls over
    #self.ctimer.start(500) # Preloads value in milliseconds
        
    self.distance = 20  # Default position of slider
    self.interval = 500 # Milliseconds between beeps, updated by slider
    self.tone = 400  	# Default audio tone
    self.length = 0.3	# Default tone length (0.1 to 0.7 seconds maximum?)
    
    self.ctimer.start(self.interval) # Preloads value in milliseconds
    self.muted = False	# Local variable to hold state of the audio output
    
#     self.p = pyaudio.PyAudio()
#     self.stream = self.p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)
    
    QtCore.QObject.connect(self.ctimer,QtCore.SIGNAL("timeout()"),self.do_function_one)
    QtCore.QObject.connect(self.ui.radioButton,QtCore.SIGNAL("pressed()"),self.do_function_three)
   # QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.do_function_one)
   # QtCore.QObject.connect(self.ui.pushButton_2, QtCore.SIGNAL("clicked()"), self.do_function_two)
   # QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL("clicked()"), self.do_function_three)
    QtCore.QObject.connect(self.ui.verticalSlider, QtCore.SIGNAL('valueChanged(int)'), self.sliderMoved)
    
#==============================================================================
# FUNCTIONS:
#==============================================================================
    


#==============================================================================
  def do_quit(self):
      print "Exit requested"
      #p.terminate()
      sys.exit() #OK

#============================================================================== 
  def do_function_one(self):      
      #print "Beep...", self.distance
      self.ctimer.start(self.interval) 
      if self.muted == False:
          self.do_function_two()
      else:
          return
      
#==============================================================================

  def do_function_two(self):
      #print "Button 2 pressed, attempt to play audio..."
      myaudioclass.playmysound(self.tone,self.length) # Frequency, Length(seconds)
      # This works

#==============================================================================      

  def do_function_three(self):
      print "Radio Button",
      if self.ui.radioButton.isChecked():
          print "SOUND ON"
          self.muted = False
      else:
          print "MUTED"
          self.muted = True
#==============================================================================

  def sliderMoved(self):
      a = self.ui.verticalSlider.value() # This works
      self.tone = a *20 + 200
      self.interval = 1010 - (a*10) # 
      self.length = 0.3	# Default tone length (0.1 to 0.7 seconds maximum?)
      
      # DEBUG 
      print "Tone: ", self.tone,
      print "Interval: ", self.interval,
      print "Length: ", self.length
      
      #self.interval = 2.0 - (a / 50.0)
      #print "Slider moved"
      
#==============================================================================      
# END OF QT CLASS
#==============================================================================  

# Now in a separate class file
# import math
# import numpy
# import pyaudio

# def sine(frequency, length, rate):
#     length = int(length * rate)
#     factor = float(frequency) * (math.pi * 2) / rate
#     return numpy.sin(numpy.arange(length) * factor)


# def play_tone(stream, frequency=440, length=1, rate=44100):
#     chunks = []
#     chunks.append(sine(frequency, length, rate))
#     chunk = numpy.concatenate(chunks) * 0.25
#     stream.write(chunk.astype(numpy.float32).tostring())
#     
#     
# def playmysound():
#     p = pyaudio.PyAudio()
#     stream = p.open(format=pyaudio.paFloat32,channels=1, rate=44100, output=1)
#     play_tone(stream)
#     stream.close()
#     p.terminate()    
#         
#----------------------------------------------------------------------
# Usage example for pyaudio
# a = AudioFile("1.wav")
# a.play()
# a.close()
    
#------------------------------------------------------------------------
 
    
#-------------------------------------------------------------------------
 

 


#============================================================ 
# Finishing off with the code to launch the graphical interface

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = MyForm()
  myapp.show()  
  sys.exit(app.exec_())
#=============================================================


