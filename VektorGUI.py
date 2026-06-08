import tkinter

vindue1 = tkinter.Tk()
vindue1.title("mitVindue")
vindue1.configure(bg="#16522D")
vindue1.geometry('1200x600')

column1X = 20
column2X = 200
spacingY = 25
startY = 30
labelSpacing = 30

##########################################
#inputs og labels til den vektor 1

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
#inputs og labels til den vektor 2

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








vindue1.mainloop()