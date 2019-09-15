#
#Extrae unos puntos de una serie y los guarda en un fichero aparte
#si es necesario les aplica un desplazamiento, ademas pasa a lineal
#

def extract_resonance(name_in,extract, desplazamiento):
	from read_ring import read_data

	data, nombres = read_data(name_in)

	Lambda = data[extract][0] + desplazamiento
	Norm = 10**(data[extract][1]/10.)

	return Lambda, Norm

if __name__ == '__main__':
	import pylab as p
	#simulando la res en 1605.47 nm
	name_in = 'addrop_7_G275G300.dat'
	extract = 5           #serie que deseamos extraer
	desplazamiento = 57.22

	Lambda, Norm = extract_resonance(name_in, extract, desplazamiento)

	p.plot(Lambda, Norm)
	p.show()
