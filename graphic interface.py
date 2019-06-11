from tkinter import *
from tkinter import messagebox

#Ventana principal
window = Tk()
window.title("Ensamblaje de Fragmentos")
window.geometry("800x500")
window.resizable(width= NO,height = NO)
window.config(bg = "cadet blue")

title = Label(window, text = "Ensamblador de Fragmentos" , bg= "cadet blue", fg="white", font="Helvetica 36 bold italic").place(x=60, y=20)

lblErrors = Label(window, text = "Valores de Probabilidad de los Errores:" , bg= "cadet blue", fg="white", font="Arial 16 bold").place(x=20, y=118)

varSustitution = StringVar()
lblSustitution = Label(window, text = "Sustitución:" , bg= "cadet blue", fg="white", font="Arial 12 bold").place(x=20, y=160)
sustitution = Entry (window, textvariable = varSustitution, bg= "#eef4f9", fg="#1e395b", width = 5).place (x = 120, y = 163)

varInsertion = StringVar()
lblInsertion = Label(window, text = "Inserción:" , bg= "cadet blue", fg="white", font="Arial 12 bold").place(x=180, y=160)
insertion = Entry (window, textvariable = varInsertion, bg= "#eef4f9", fg="#1e395b", width = 5).place (x = 265, y = 163)

varDeletion = StringVar()
lblDeletion = Label(window, text = "Deleción:" , bg= "cadet blue", fg="white", font="Arial 12 bold").place(x=340, y=160)
deletion = Entry (window, textvariable = varDeletion, bg= "#eef4f9", fg="#1e395b", width = 5).place (x = 420, y = 163)

varChimeras = StringVar()
lblChimeras = Label(window, text = "Quimeras:" , bg= "cadet blue", fg="white", font="Arial 12 bold").place(x=480, y=160)
chimeras = Entry (window, textvariable = varChimeras, bg= "#eef4f9", fg="#1e395b", width = 5).place (x = 565, y = 163)

varInversion = StringVar()
lblInversion = Label(window, text = "Inversión:" , bg= "cadet blue", fg="white", font="Arial 12 bold").place(x=630, y=160)
inversion = Entry (window, textvariable = varInversion, bg= "#eef4f9", fg="#1e395b", width = 5).place (x = 710, y = 163)

lblOverlap = Label(window, text = "Rango de Traslape:" , bg= "cadet blue", fg="white", font="Arial 16 bold").place(x=20, y=220)

varMinOverlap = StringVar()
lblMinOverlap = Label(window, text = "Mínimo:" , bg= "cadet blue", fg="white", font="Arial 12 bold").place(x=100, y=270)
inversion = Entry (window, textvariable = varMinOverlap, bg= "#eef4f9", fg="#1e395b", width = 8).place (x = 170, y = 273)

varMinOverlap = StringVar()
lblMinOverlap = Label(window, text = "Mínimo:" , bg= "cadet blue", fg="white", font="Arial 12 bold").place(x=100, y=270)
minOverlap = Entry (window, textvariable = varMinOverlap, bg= "#eef4f9", fg="#1e395b", width = 8).place (x = 170, y = 273)

varMaxOverlap = StringVar()
lblMaxOverlap = Label(window, text = "Máximo:" , bg= "cadet blue", fg="white", font="Arial 12 bold").place(x=300, y=270)
maxOverlap = Entry (window, textvariable = varMaxOverlap, bg= "#eef4f9", fg="#1e395b", width = 8).place (x = 370, y = 273)

lblFragments = Label(window, text = "Cantidad de Fragmentos:" , bg= "cadet blue", fg="white", font="Arial 16 bold").place(x=20, y=320)
varFragments = StringVar()
fragments = Entry (window, textvariable = varFragments, bg= "#eef4f9", fg="#1e395b", width = 10).place (x = 30, y = 360)

generate = Button(window, width = 15, bg="Skyblue4",fg="white",text="GENERATE", font = "Helvetica 16 bold italic")
generate.place(x = 250, y = 400)

adn = PhotoImage(file="adn.png")
labelImage = Label(window, image = adn, bg = "cadet blue").place(x=550, y=300)

