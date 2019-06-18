from shotgun import *
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename

dnaFile = ""

#Ventana principal
window = Tk()
window.title("Ensamblaje de Fragmentos")
window.geometry("800x650")
window.resizable(width= NO,height = NO)
window.config(bg = "cadet blue")

title = Label(window, text = "Ensamblador de Fragmentos" , bg= "cadet blue", fg="white", font="Helvetica 36 bold italic").place(x=60, y=20)

varDna = StringVar()
lblDna = Label(window, text = "Texto de ADN:", bg = "cadet blue", fg = "white", font="Arial 12 bold").place(x=50, y=140)
entryDna = Entry (window,  bg = "#eef4f9", fg = "#1e395b", font = "Arial 10 italic", textvariable = varDna, width = 45).place (x = 180, y = 142)

btnSearchDna = Button(window, width=12, bg="Skyblue3", fg="white", text="Buscar", font="Helvetica 11 bold", command=lambda : search())
btnSearchDna.place(x=520, y=137)

lblErrors = Label(window, text = "Valores de Probabilidad de los Errores:" , bg= "cadet blue", fg="white", font="Arial 16 bold").place(x=20, y=218)

varSustitution = StringVar()
lblSustitution = Label(window, text = "Sustitución:" , bg= "cadet blue", fg="white", font="Arial 12 bold").place(x=20, y=260)
sustitution = Entry (window, textvariable = varSustitution, bg= "#eef4f9", fg="#1e395b", width = 5).place (x = 120, y = 263)

varInsertion = StringVar()
lblInsertion = Label(window, text = "Inserción:" , bg= "cadet blue", fg="white", font="Arial 12 bold").place(x=180, y=260)
insertion = Entry (window, textvariable = varInsertion, bg= "#eef4f9", fg="#1e395b", width = 5).place (x = 265, y = 263)

varDeletion = StringVar()
lblDeletion = Label(window, text = "Deleción:" , bg= "cadet blue", fg="white", font="Arial 12 bold").place(x=340, y=260)
deletion = Entry (window, textvariable = varDeletion, bg= "#eef4f9", fg="#1e395b", width = 5).place (x = 420, y = 263)

varChimeras = StringVar()
lblChimeras = Label(window, text = "Quimeras:" , bg= "cadet blue", fg="white", font="Arial 12 bold").place(x=480, y=260)
chimeras = Entry (window, textvariable = varChimeras, bg= "#eef4f9", fg="#1e395b", width = 5).place (x = 565, y = 263)

varInversion = StringVar()
lblInversion = Label(window, text = "Inversión:" , bg= "cadet blue", fg="white", font="Arial 12 bold").place(x=630, y=260)
inversion = Entry (window, textvariable = varInversion, bg= "#eef4f9", fg="#1e395b", width = 5).place (x = 710, y = 263)

lblOverlap = Label(window, text = "Rango de Traslape:" , bg= "cadet blue", fg="white", font="Arial 16 bold").place(x=20, y=320)

varMinOverlap = StringVar()
lblMinOverlap = Label(window, text = "Mínimo:" , bg= "cadet blue", fg="white", font="Arial 12 bold").place(x=100, y=370)
inversion = Entry (window, textvariable = varMinOverlap, bg= "#eef4f9", fg="#1e395b", width = 8).place (x = 170, y = 373)

varMinOverlap = StringVar()
lblMinOverlap = Label(window, text = "Mínimo:" , bg= "cadet blue", fg="white", font="Arial 12 bold").place(x=100, y=370)
minOverlap = Entry (window, textvariable = varMinOverlap, bg= "#eef4f9", fg="#1e395b", width = 8).place (x = 170, y = 373)

varMaxOverlap = StringVar()
lblMaxOverlap = Label(window, text = "Máximo:" , bg= "cadet blue", fg="white", font="Arial 12 bold").place(x=300, y=370)
maxOverlap = Entry (window, textvariable = varMaxOverlap, bg= "#eef4f9", fg="#1e395b", width = 8).place (x = 370, y = 373)

lblFragments = Label(window, text = "Configuración de Fragmentos:" , bg= "cadet blue", fg="white", font="Arial 16 bold").place(x=20, y=420)

varQuantityFragments = StringVar()
lblQuantityFragments = Label(window, text = "Cantidad:" , bg= "cadet blue", fg="white", font="Arial 12 bold").place(x=20, y=460)
quantityFragments = Entry (window, textvariable = varQuantityFragments, bg= "#eef4f9", fg="#1e395b", width = 10).place (x = 100, y = 462)

varSizeFragments = StringVar()
lblSizeFragments = Label(window, text = "Tamaño:" , bg= "cadet blue", fg="white", font="Arial 12 bold").place(x=200, y=460)
sizeFragments = Entry (window, textvariable = varSizeFragments, bg= "#eef4f9", fg="#1e395b", width = 10).place (x = 280, y = 462)

varCoverageFragments = StringVar()
lblCoverageFragments = Label(window, text = "Porcentaje de cobertura mínimo:" , bg= "cadet blue", fg="white", font="Arial 12 bold").place(x=380, y=460)
coverageFragments = Entry (window, textvariable = varCoverageFragments, bg= "#eef4f9", fg="#1e395b", width = 10).place (x = 650, y = 462)

btnGenerate = Button(window, width = 15, bg="Skyblue4",fg="white",text="GENERATE", font = "Helvetica 16 bold italic", command = lambda : buttonAtcion())
btnGenerate.place(x = 250, y = 520)

adn = PhotoImage(file="adn.png")
labelImage = Label(window, image = adn, bg = "cadet blue").place(x=650, y=500)

def ventanaSecundaria():
    windowSec = Tk()
    windowSec.title("Ensamblaje de Fragmentos")
    windowSec.geometry("500x500")
    windowSec.resizable(width= NO,height = NO)
    windowSec.config(bg = "cadet blue")

    btnOther = Button(windowSec, width = 15, bg="Skyblue4",fg="white",text="Generate Other", font = "Helvetica 16 bold italic", command = lambda : buttonOther())
    btnOther.place(x = 50, y = 100)

    btnGraph = Button(windowSec, width = 15, bg="Skyblue4",fg="white",text="View Graph", font = "Helvetica 16 bold italic", command = lambda : buttonAtcion())
    btnGraph.place(x = 50, y = 200)


def search():
    global dnaFile
    file = askopenfilename()
    dnaFile = file
    direction = file.split("/")
    varDna.set("[Archivo Cargado]: " + direction[-1])

def buttonAtcion():
    #generate(eval(varSustitution.get()), eval(varInsertion.get()), eval(varDeletion.get()), eval(varChimeras.get()), eval(varInversion.get()), eval(varMinOverlap.get()), eval(varMaxOverlap.get()), eval(varQuantityFragments.get()), eval(varSizeFragments.get()), eval(varCoverageFragments.get()), dnaFile)
    messagebox.showinfo("Éxito", "Proceso Completado")
    ventanaSecundaria()



