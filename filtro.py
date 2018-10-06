import numpy
from scipy import signal
from matplotlib import pyplot

b=numpy.array([0.003646,0.01094,0.01094,0.003646])
a=numpy.array([1,-2.503,2.239,-0.7071])

phi=numpy.arange(-numpy.pi,numpy.pi,numpy.pi/100)

w,H=signal.freqz(b,a,phi)

pyplot.plot(phi,numpy.abs(H))
pyplot.show()

#---------------------------------------------------------------------

#import numpy
#from scipy import signal
#from numpy import pi
#from numpy import sin
#from matplotlib import pyplot
#
#fs=22050.0
#fn=fs/2
#
##sañel cuadrada limitada a 700 Khz
#
#t=numpy.arange(0,3e-3,1.0/fs)
#x=sin(2*pi*1000*t)+(1.0/3)*sin(2*pi*3000*t)+(1.0/5)*sin(2*pi*5000*t)+(1.0/7)*sin(2*pi*7000*t)

