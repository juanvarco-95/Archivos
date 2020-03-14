#Basado en: https://recursospython.com/codigos-de-fuente/enviar-archivo-via-socket/
#import
import zmq
import os
import hashlib

#Socket
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5558")
c1=0
mensaje = "Recibido correctamente"
file = 'File'

#Imprime el Hash del archivo
def hash(files):
    files_hash = hashlib.sha1()
    with open(files, 'rb') as f:
        fb = f.read()
        while len(fb) > 0:
            files_hash.update(fb)
            fb = f.read()
    print (files_hash.hexdigest())

while True:
    message = socket.recv()
    nombre="archivo"+str(c1)+".part"
    f = open(nombre, "wb+")
    f.write(message)
    print("Se recibió archivo correctamente")
    hash(file)
    f.close()

    socket.send(mensaje.encode("utf-8"))
    c1=c1+1
