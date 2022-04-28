
#
#Leer la salida de los archivos generados por los barridos del
#programa de Claudio
#
#
########Formato de los archivos de entrada##############
# fila con los nombres de las columnas separadas por tabuladores y comentada
# resto de filas sin numeros comentadas tambien
# numeritos 
#

def read_data(name_in):
	from numpy import genfromtxt, isnan, any

	with open(name_in, 'r') as infile:
		names = infile.readline()
	names = names.lstrip('#').split('\t')

	#Aqui se leen los datos numericos
	data = genfromtxt(name_in, delimiter='\t', comments='#', unpack=True)

	#Aqui se organizan los datos correctamente
	series, series_names = [],[]

	for i in range(len(data)/3):
		serie_aux = []
		serie_aux += [data[i   + i*2][~isnan(data[i   + i*2])]]
		serie_aux += [data[i+1 + i*2][~isnan(data[i+1 + i*2])]]
		serie_aux += [data[i+2 + i*2][~isnan(data[i+2 + i*2])]]

		series += [serie_aux]

		serie_aux = []
		serie_aux += [names[i   + i*2]]
		serie_aux += [names[i+1 + i*2]]
		serie_aux += [names[i+2 + i*2]]

		series_names += [serie_aux]

	return series,series_names

#a[~isnan(a)]

if __name__ == '__main__':
	#El nombre del fichero de entrada y otras cosas
	name_in = 'medidas_nuevas.DAT'
	Lineal = False   #dBm->False; mW->True

	import pylab as p

	data, nombres = read_data(name_in)
	print nombres


	if Lineal == False:
		for j in range(len(data)):
			p.ylabel('dBm')
			p.plot(data[j][0],data[j][1],label=nombres[j][1])
	else:
		for j in range(len(data)):
			p.ylabel('mW')
			data[j][1] = 10**(data[j][1]/10.)
			p.plot(data[j][0],data[j][1],label=nombres[j][1])


	p.xlabel('lambda (nm)')
	p.grid(True)
	#p.legend()
	p.show()

