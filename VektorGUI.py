import tkinter
import vektor

vindue1 = tkinter.Tk()
vindue1.title("mitVindue")
vindue1.configure(bg="#164A2B")
vindue1.geometry('1200x650')

column1X = 20
column2X = 200
spacingY = 25
startY = 30
labelSpacing = 30

##########################################
#resultat label

resultat= tkinter.Label(vindue1)
resultat.place(x=column1X, y=startY + spacingY * 8)

##########################################
#Beregningsfunktioner
def Vektor2Dsum():
    #henter ting til 2d vektorer.
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

def Vektorvinkelimellem2D():
    svar = vektor.Vektorvinkelimellem2D(float(X1.get()), float(Y1.get()), float(X2.get()), float(Y2.get()))
    resultat.config(text=f"resultat:\t {svar} ")


##########################################
#inputs og labels til vektor 1

overskriftVektor1 = tkinter.Label(vindue1, text="Vektor 1")
overskriftVektor1.place(x=column1X, y=20)

X1 = tkinter.Entry(vindue1)
X1Label = tkinter.Label(vindue1, text="X1")
X1.place(x=column1X + labelSpacing, y=startY + spacingY)
X1Label.place(x=column1X, y=startY + spacingY)

Y1 = tkinter.Entry(vindue1)
Y1Label = tkinter.Label(vindue1, text="Y1")
Y1.place(x=column1X + labelSpacing, y=startY + spacingY * 2)
Y1Label.place(x=column1X, y=startY + spacingY * 2)

Z1 = tkinter.Entry(vindue1)
Y1Label = tkinter.Label(vindue1, text="Z1")
Z1.place(x=column1X + labelSpacing, y=startY + spacingY * 3)
Y1Label.place(x=column1X, y=startY + spacingY * 3)

##########################################
#inputs og labels til vektor 2

overskriftVektor2 = tkinter.Label(vindue1, text="Vektor 2")
overskriftVektor2.place(x=column2X, y=20)

X2 = tkinter.Entry(vindue1)
X2Label = tkinter.Label(vindue1, text="X2")
X2.place(x=column2X + labelSpacing, y=startY + spacingY)
X2Label.place(x=column2X, y=startY + spacingY)

Y2 = tkinter.Entry(vindue1)
Y2Label = tkinter.Label(vindue1, text="Y2")
Y2.place(x=column2X + labelSpacing, y=startY + spacingY * 2)
Y2Label.place(x=column2X, y=startY + spacingY * 2)

Z2 = tkinter.Entry(vindue1)
Z2Label = tkinter.Label(vindue1, text="Z2")
Z2.place(x=column2X + labelSpacing, y=startY + spacingY * 3)
Z2Label.place(x=column2X, y=startY + spacingY * 3)

##########################################
#inputs og labels til skalar
skalarLabel = tkinter.Label(vindue1, text="Skalar")
skalarLabel.place(x=column1X, y=startY + spacingY * 5)
skalar = tkinter.Entry(vindue1)
skalar.place(x=column1X + 50, y=startY + spacingY * 5)

##########################################
#beregn knapper og output resultater

beregnVektor2Dsum = tkinter.Button(vindue1, command=Vektor2Dsum, text="Sum2D")
beregnVektor2Dsum.place(x=column1X , y=startY + spacingY * 6)

beregnVektor2Dminus = tkinter.Button(vindue1, command=Vektor2Dminus, text="Diff2D")
beregnVektor2Dminus.place(x=column1X + 50 , y=startY + spacingY * 6)

beregnVektor2Dskalar = tkinter.Button(vindue1, command=Vektor2Dskalar, text="Skalar2D")
beregnVektor2Dskalar.place(x=column1X + 100 , y=startY + spacingY * 6)

beregnVektor2Dskalar = tkinter.Button(vindue1, command=Vektor2Dskalar, text="Skalar2D")
beregnVektor2Dskalar.place(x=column1X + 100 , y=startY + spacingY * 6)

beregnVektor2Dlengde = tkinter.Button(vindue1, command=Vektor2Dlengde, text="Laengde2D")
beregnVektor2Dlengde.place(x=column1X + 100 , y=startY + spacingY * 6)
##########################################





vindue1.mainloop()