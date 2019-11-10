# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 08:00:38 2019

@author: artov
"""

from tkinter import *
import serial, time
time.sleep(4)
lectura1 = []
arduino = serial.Serial('COM8' , 9600)



def leer():
    try:
        datos = int(entrada.get())
        entrada.delete(0,datos)
        datos = int(datos)
        arduino.write(b'e')
        for i in range(datos):
            lectura1.append(arduino.readline())
        messagebox.showinfo('Operacíon exitosa', message = 'Datos leidos')
        print(lectura1)
        arduino.close()
    except (ValueError):
        messagebox.showerror('Error', message = 'tipos de datos inválidos')
        
def guardar():
    try:
        nombrearch = entrada2.get()
        print(nombrearch)
        if len(lectura1)!=0 and nombrearch != None:
            archivo =  open(nombrearch + '.txt', 'w')
            esc = ''
            for i in range(len(lectura1)):
                lectura1[i] = str(lectura1[i]).replace('b', '').replace("'", '').replace('r', '').replace('\\', '').replace('n','')
                esc+=lectura1[i] + '\n'
            archivo.write(esc)
            archivo.close()
            entrada2.delete(0,len(nombrearch))
            messagebox.showinfo('Éxito al guardar', message = 'Se guardó con éxito')
            
        else:
            0/0
            
    except (ZeroDivisionError):
        messagebox.showerror('Error', message = 'No hay datos que guardar o no hay nombre de Archivo')
        
        
        
root = Tk()

frame = Frame(root)
frame.pack()

button = Button(frame, text = 'Leer', command = leer)
button.pack(side = BOTTOM)

entrada = Entry(frame)
entrada.pack(side = RIGHT)

etiqueta = Label(frame, text = 'Número de datos')
etiqueta.pack(side = BOTTOM)

#---------------------------------------------------------------------------
frame2 = Frame(root)
frame2.pack()
button2 = Button(frame2, text = 'Guardar', command = guardar)
button2.pack(side = BOTTOM)

entrada2 = Entry(frame2)
entrada2.pack(side = RIGHT)

etiqueta2 = Label(frame2, text = 'Nombre del archivo')
etiqueta2.pack(side = BOTTOM)

root.mainloop()
