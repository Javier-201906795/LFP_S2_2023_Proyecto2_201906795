

from tkinter import messagebox as MessageBox






def GetTokens(texto):
    #Validar tamaño del texto
    if len(texto) < 10:
        MessageBox.showerror('Error - lexico()','No hay informacion necesarioa para procesarlo')
        return 
    
    return [1,'hola','}']
