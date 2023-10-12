from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog, messagebox



########################################################################
raiz = Tk()
raiz.title('LFP Proyecto 2 | 201906795')
raiz.geometry('1000x800')

Label(raiz, pady=0,text='PROYECTO 2 | 201906795', font=("Consolas",14)).place(x=50,y=20)
Button(raiz,text='Abrir', bg='#DBE6A1', fg='#000000',font=("Consolas",12)).place(x=500,y=20, width=90, height= 35)
Button(raiz,text='Actualizar', bg='#DBE6A1', fg='#000000',font=("Consolas",12)).place(x=610,y=20, width=120, height= 35)


opcionesarchivo = ['Reportes','opcion1','opcion2','opcion3', 'Salir']
listaopciones = Combobox(raiz, text='Archivo', values = opcionesarchivo, font=("Consolas",11))
listaopciones.place(x=750,y=20, width=130, height= 35)
listaopciones.current(0)



raiz.mainloop()
