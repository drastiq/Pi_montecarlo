import numpy as np
import matplotlib.pyplot as plt
from numpy import random,sqrt,pi
def unsigned(n):
	return n & 0xFFFFFFFF


try:
	r = int(input('Promien: '))
	n = int(input('Liczba testow: '))
	anim = int(input('Wykres interaktywny? (1=tak 0=nie): '))
	if (r==0 or n ==0 or (anim!= 0 and anim!= 1)) :
		print "Podano nie prawidlowe wartosci."

	else:
		p = 2 * r * random.random_sample((n, 2)) - r

		inCircle = sqrt(p[:, 0] ** 2 + p[:, 1] ** 2) <= r
		plt.axis([-r, r, -r, r])
		plt.ion()
		circle = plt.Circle((0, 0), r, fill = False)
		plt.gca().add_patch(circle)


		inCounter=0
		outCounter=0
		for i in inCircle:
			if i:
				plt.scatter(p[inCircle, 0][inCounter],p[inCircle, 1][inCounter],color="blue")
				inCounter+=1
				if anim == 1:
					plt.pause(0.001)

			if not i:
				plt.scatter(p[inCircle== False, 0][outCounter],p[inCircle== False, 1][outCounter],color="red")
				outCounter+=1
				if anim == 1:
					plt.pause(0.001)

			
		while True:
			print "***********************************"
			_pi =(sum(inCircle).astype('double') / n * 4)
			print 'Orzymana wartosc pi = ''%0.16f' % _pi
			print 'wartosc rzeczywista %0.16f' % pi
			print 'Blad wynosi %0.16f' %(abs((pi - _pi)))
			print "W okregu: ",; print inCounter
			print "Poza okregiem: ",;print outCounter
			print "***********************************"
			plt.pause(1000)
except(ValueError, NameError, AttributeError, SyntaxError):
	print "Podano nie prawidlowe wartosci. "
except:
	print ""