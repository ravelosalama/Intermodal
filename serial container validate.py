
# Programa para validar serial de contenedores segun digito de verificacion.
# Fuente del proceso y formulas:https://es.wikipedia.org/wiki/Contenedor#Identificaci%C3%B3n
# Codificado por:Jose Ravelo / Mayo 2020.

#Asignacion de valores sincronos de dos Tuplas para generar un diccionario.
k = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
v = (10,12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	23,	24,	25,	26,	27,	28,	29,	30,	31,	32,	34,	35,	36,	37,	38)

d = {}

#Llenado de Diccionario basado en tuplas k - Key y v - Value.
c=0
for i in k:
    
    d[k[c]]=v[c]
    #print (k[c],v[c],i,' ',c, len(k), len(v))
    c=c+1
print ('Diccionario generado')
print ('----------0----------0--------0--------')
print (d)
print (d['V'],' ',d['E'], type(d['U']))
print ('----------0----------0--------0--------')

#Validaciones de entradas por codificar.
#Crear bucle indeterminado de ingreso de dato.
serial=input('INGRESE UN SERIAL:')
#serial=serial.upper
dvt=serial #Codificar extraccion de digito de verificacion ingresado.
t=0
c=0
for i in serial:
      if c>=4:
          #print (t,type(t))
          t=t+(int(i)) * 2**c     
      else:
          t=t+d[i]*2**c
          #print (t,type(t),type(i))
      c=c+1
      print (i,c,t)
print ('este es el valor de t:',t)
t1=int(t/11)
t2=t1*11
dv=t-t2

if dv==10:
    dv=0

if dv==dvt:
   r='el serial fue validado satisfactoriamente'
else:
   r='hay un problema con el serial, reviselo de nuevo'

print ('El digito de verificacion calculado es: ',dv)
print ('El digito de verificacion Transcrito es:',r)



