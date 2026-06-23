import tkinter
import vektor
from tkinter import font

vindue1 = tkinter.Tk()
vindue1.title("mitVindue")
vindue1.configure(bg="#51355A")
vindue1.geometry('1200x650')

column1X = 20
column2X = 200
spacingY = 25
startY = 30
labelSpacing = 30

##########################################
#saetter standardfont til helvetica
default_font = font.nametofont("TkDefaultFont")
default_font.configure(family="Helvetica",size=10)

##########################################
#resultat label
resultat= tkinter.Label(vindue1, bg="#FFF8F0")
resultat.place(x=column1X, y=startY + spacingY * 15)

##########################################
#Beregningsfunktioner
def Vektor2Dsum():
    svar = vektor.Vektor2Dsum(float(X1.get()), float(Y1.get()), float(X2.get()), float(Y2.get()))
    resultat.config(text=f"resultat:\t {svar} ")
    
def Vektor2Dminus():
    svar = vektor.Vektor2Dminus(float(X1.get()), float(Y1.get()), float(X2.get()), float(Y2.get()))
    resultat.config(text=f"resultat:\t {svar} ")

def Vektor2Dskalar():
    svar = vektor.Vektor2Dskalar(float(X1.get()), float(Y1.get()), float(skalar.get()))
    resultat.config(text=f"resultat:\t {svar} ")

def Vektor2Dlengde():
    svar = vektor.Vektor2Dlengde(float(X1.get()), float(Y1.get()))
    resultat.config(text=f"resultat:\t {svar} ")

def Vektor2Dvinkel():
    svar = vektor.Vektor2Dvinkel(float(X1.get()), float(Y1.get()))
    resultat.config(text=f"resultat:\t {svar} ")

def PolaerKoordinater():
    svar = vektor.PolaerKoordinater(float(X1.get()), float(Y1.get()))
    resultat.config(text=f"resultat:\t {svar} ")

def Vektor2Dprikprodukt():
    svar = vektor.Vektor2Dprikprodukt(float(X1.get()), float(Y1.get()), float(X2.get()), float(Y2.get()))
    resultat.config(text=f"resultat:\t {svar} ")

def Vektor2Denhedsvektor():
    svar = vektor.Vektor2Denhedsvektor(float(X1.get()), float(Y1.get()))
    resultat.config(text=f"resultat:\t {svar} ")

def PunktTilVektor():
    svar = vektor.PunktTilVektor(float(X1.get()), float(Y1.get()), float(X2.get()), float(Y2.get()))
    resultat.config(text=f"resultat:\t {svar} ")

def Vektorvinkelimellem2D():
    svar = vektor.Vektorvinkelimellem2D(float(X1.get()), float(Y1.get()), float(X2.get()), float(Y2.get()))
    resultat.config(text=f"resultat:\t {svar} ")

def Vektor3Dsum():
    svar = vektor.Vektor3Dsum(float(X1.get()), float(Y1.get()), float(Z1.get()), float(X2.get()), float(Y2.get()), float(Z2.get()))
    resultat.config(text=f"resultat:\t {svar} ")

def Vektor3Dminus():
    svar = vektor.Vektor3Dminus(float(X1.get()), float(Y1.get()), float(Z1.get()), float(X2.get()), float(Y2.get()), float(Z2.get()))
    resultat.config(text=f"resultat:\t {svar} ")

def Vektor3Dskalar():
    svar = vektor.Vektor3Dskalar(float(X1.get()), float(Y1.get()), float(Z1.get()), float(skalar.get()))
    resultat.config(text=f"resultat:\t {svar} ")

def Vektor3Dlengde():
    svar = vektor.Vektor3Dlengde(float(X1.get()), float(Y1.get()), float(Z1.get()))
    resultat.config(text=f"resultat:\t {svar} ")

def Vektor3Dprikprodukt():
    svar = vektor.Vektor3Dprikprodukt(float(X1.get()), float(Y1.get()), float(Z1.get()), float(X2.get()), float(Y2.get()), float(Z2.get()))
    resultat.config(text=f"resultat:\t {svar} ")

def Vektor3Denhedsvektor():
    svar = vektor.Vektor3Denhedsvektor(float(X1.get()), float(Y1.get()), float(Z1.get()))
    resultat.config(text=f"resultat:\t {svar} ")

def Krydsprodukt():
    svar = vektor.Vektor3Dprikprodukt(float(X1.get()), float(Y1.get()), float(Z1.get()), float(X2.get()), float(Y2.get()), float(Z2.get()))
    resultat.config(text=f"resultat:\t {svar} ")

def PunktTilVektor3D():
    svar = vektor.PunktTilVektor3D(float(X1.get()), float(Y1.get()), float(Z1.get()), float(X2.get()), float(Y2.get()), float(Z2.get()))
    resultat.config(text=f"resultat:\t {svar} ")

##########################################
#inputs og labels til vektor 1

overskriftVektor1 = tkinter.Label(vindue1, text="Vektor/Punkt 1", bg="#FFF8F0")
overskriftVektor1.place(x=column1X, y=20)

X1 = tkinter.Entry(vindue1, bg="#FFF8F0" )
X1Label = tkinter.Label(vindue1, text="X1", bg="#DC6F69" )
X1.place(x=column1X + labelSpacing, y=startY + spacingY)
X1Label.place(x=column1X, y=startY + spacingY)

Y1 = tkinter.Entry(vindue1, bg="#FFF8F0" )
Y1Label = tkinter.Label(vindue1, text="Y1",  bg="#DC6F69" )
Y1.place(x=column1X + labelSpacing, y=startY + spacingY * 2)
Y1Label.place(x=column1X, y=startY + spacingY * 2)

Z1 = tkinter.Entry(vindue1, bg="#FFF8F0" )
Y1Label = tkinter.Label(vindue1, text="Z1",  bg="#DC6F69" )
Z1.place(x=column1X + labelSpacing, y=startY + spacingY * 3)
Y1Label.place(x=column1X, y=startY + spacingY * 3)

##########################################
#inputs og labels til vektor 2

overskriftVektor2 = tkinter.Label(vindue1, text="Vektor/Punkt 2", bg="#FFF8F0")
overskriftVektor2.place(x=column2X, y=20)

X2 = tkinter.Entry(vindue1, bg="#FFF8F0" )
X2Label = tkinter.Label(vindue1, text="X2",  bg="#DC6F69" )
X2.place(x=column2X + labelSpacing, y=startY + spacingY)
X2Label.place(x=column2X, y=startY + spacingY)

Y2 = tkinter.Entry(vindue1, bg="#FFF8F0" )
Y2Label = tkinter.Label(vindue1, text="Y2", bg="#DC6F69" )
Y2.place(x=column2X + labelSpacing, y=startY + spacingY * 2)
Y2Label.place(x=column2X, y=startY + spacingY * 2)

Z2 = tkinter.Entry(vindue1, bg="#FFF8F0" )
Z2Label = tkinter.Label(vindue1, text="Z2",  bg="#DC6F69" )
Z2.place(x=column2X + labelSpacing, y=startY + spacingY * 3)
Z2Label.place(x=column2X, y=startY + spacingY * 3)

##########################################
#inputs og labels til skalar
skalarLabel = tkinter.Label(vindue1, text="Skalar", bg="#DC6F69")
skalarLabel.place(x=column1X, y=startY + spacingY * 5)
skalar = tkinter.Entry(vindue1, bg="#FFF8F0")
skalar.place(x=column1X + 50, y=startY + spacingY * 5)

##########################################
#Opretter beregn-knapper ved at 
knap2DFrame = tkinter.Frame(vindue1, bg="#2A0C4E")
knap2DFrame.place(x=column1X, y=200)

knapper2D = [
    ("Sum2D", Vektor2Dsum),
    ("Diff2D", Vektor2Dminus),
    ("Skalar2D", Vektor2Dskalar),
    ("Længde2D", Vektor2Dlengde),
    ("Vinkel2D", Vektor2Dvinkel),
    ("Polær2D", PolaerKoordinater),
    ("Prik2D", Vektor2Dprikprodukt),
    ("Enheds2D", Vektor2Denhedsvektor),
    ("Imellem2D", Vektorvinkelimellem2D),
    ("PktVec", PunktTilVektor),
]
for i, (tekst, funktion) in enumerate(knapper2D):
    tkinter.Button(knap2DFrame, text=tekst, command=funktion, width=12, bg="#FFF8F0")\
        .grid(row=i // 4, column=i % 4, padx=2, pady=2)
    
knap3DFrame = tkinter.Frame(vindue1, bg="#2A0C4E")
knap3DFrame.place(x=column1X, y=300)

knapper3D = [
    ("Sum3D", Vektor3Dsum),
    ("Diff3D", Vektor3Dminus),
    ("Skalar3D", Vektor3Dskalar),
    ("Længde3D", Vektor3Dlengde),
    ("Prik3D", Vektor3Dprikprodukt),
    ("Enheds3D", Vektor3Denhedsvektor),
    ("Kryds", Krydsprodukt),
    ("PktVec3D", PunktTilVektor3D),
]
for i, (tekst, funktion) in enumerate(knapper3D):
    tkinter.Button(knap3DFrame, text=tekst, command=funktion, width=12, bg="#FFF8F0" )\
        .grid(row=i // 4, column=i % 4, padx=2, pady=2)

##########################################
#koerer programmet
vindue1.mainloop()