import math
import matplotlib.pyplot as plt

def Vektor2Dsum(x1, y1, x2, y2):
    v1 = plt.arrow(0,0, x1, y1, head_width=0.1, head_length=0.1, length_includes_head=True, color="green")
    v2 = plt.arrow(x1,y1, x2, y2, head_width=0.1, head_length=0.1, length_includes_head=True, color="yellow")
    resultX = x1 + x2
    resultY = y1 + y2
    result = plt.arrow(0,0, resultX, resultY, head_width=0.1, head_length=0.1, length_includes_head=True, color="blue")
    return (resultX, resultY)



def Vektor2Dminus(x1, y1, x2, y2):
    resultx = x1 - x2
    resulty = y1 - y2
    a = resultx - x1
    b = resulty - y1
    v1 = plt.arrow(0,0, x1, y1, head_width=0.1, head_length=0.1, length_includes_head=True, color="green")
    v2 = plt.arrow(x1,y1, a, b, head_width=0.1, head_length=0.1, length_includes_head=True, color="yellow")
    result = plt.arrow(0,0, resultx, resulty, head_width=0.1, head_length=0.1, length_includes_head=True, color="red")
    return(resultx, resulty)


def Vektor2Dskalar(x1, y1, s):
    x = plt.arrow(0,0, x1 * s, y1 * s, head_width=0.1, head_length=0.1, length_includes_head=True, color="black")
    y = plt.arrow(0,0, 0, y1 * s, head_width=0.1, head_length=0.1, length_includes_head=True, color="black")

    return(x, y)

def Vektor2Dlengde(x1, y1):
    return(math.sqrt(x1**2 + y1**2))

def Vektor2Dvinkel(x1, y1):
    return (math.degrees(math.atan(y1/x1)))


def PolaerKoordinater(x, y):
    r = math.sqrt(x**2 + y**2)
    vinkel = math.atan2(y, x)
    v1= plt.arrow(0,0, x, y, head_width=0.1, head_length=0.1, length_includes_head=True, color="black")

    return (v1)


def Vektor2Dprikprodukt(x1, y1, x2, y2):
    resultx = x1 * x2
    resulty = y1 * y2
    v1=plt.arrow(0,0, resultx, resulty, head_width=0.1, head_length=0.1, length_includes_head=True, color="black")
    return (x1 * x2) + (y1 * y2)

def Vektor2Denhedsvektor(x1, y1):

    
    v1=plt.arrow(0,0, x1, y1, head_width=0.1, head_length=0.1, length_includes_head=True, color="black")
    enhedsvektorX = x1 / Vektor2Dlengde(x1, y1)
    enhedsvektorY = y1 / Vektor2Dlengde(x1, y1)
    e1=plt.arrow(0,0, enhedsvektorX, enhedsvektorY, head_width=0.1, head_length=0.1, length_includes_head=True, color="red")



    return(enhedsvektorX, enhedsvektorY )


def Vektorvinkelimellem2D(x1, y1, x2, y2):

    return(math.acos(Vektor2Dprikprodukt(x1, y1, x2, y2) / (Vektor2Dlengde(x1, y1) * Vektor2Dlengde(x2, y2))))




def Vektor3Dsum(x1, y1, z1, x2, y2, z2):
    x = plt.arrow(0,0, x1, y1, head_width=0.1, head_length=0.1, length_includes_head=True, color="black")
    y = plt.arrow(0,0, x2, y2, head_width=0.1, head_length=0.1, length_includes_head=True, color="black")
    z = plt.arrow(0,0, 0, 0, head_width=0.1, head_length=0.1, length_includes_head=True, color="black")

    return(x, y, z)



def Vektor3Dminus(x1, y1, z1, x2, y2, z2):
    x = plt.arrow(0,0, x1, y1, head_width=0.1, head_length=0.1, length_includes_head=True, color="black")
    y = plt.arrow(0,0, x2, y2, head_width=0.1, head_length=0.1, length_includes_head=True, color="black")
    z = plt.arrow(0,0, 0, 0, head_width=0.1, head_length=0.1, length_includes_head=True, color="black")

    return(x, y, z)
    


def Vektor3Dskalar(x1, y1, z1, s):
    x = plt.arrow(0,0, x1 * s, y1 * s, head_width=0.1, head_length=0.1, length_includes_head=True, color="black")
    y = plt.arrow(0,0, 0, y1 * s, head_width=0.1, head_length=0.1, length_includes_head=True, color="black")
    z = plt.arrow(0,0, 0, z1 * s, head_width=0.1, head_length=0.1, length_includes_head=True, color="black")

    return(x, y, z)

def Vektor3Dlengde(x1, y1, z1):
     return(math.sqrt(x1**2 + y1**2 + z1**2))



def vektor3Dvinkel(x1, y1, z1):
    return (math.degrees(math.atan(y1, x1)))


def Vektor3DpolaerKoordinater(x, y, z):
    r = math.sqrt(x**2 + y**2 + z**2)
    vinkel = math.atan(y, x)
    phi = math.acos(z / r)

    return (r, vinkel, phi)


def Vektor3Dprikprodukt(x1, y1, x2, y2, z1, z2):
    return (x1 * x2) + (y1 * y2) + (z1 * z2)

    

def Vektor3Denhedsvektor(x1, y1, z1):

    enhedsvektorX = x1 / Vektor3Dlengde(x1, y1, z1)
    enhedsvektorY = y1 / Vektor3Dlengde(x1, y1, z1)
    enhedsvektorZ = z1 / Vektor3Dlengde(x1, y1, z1)



    return(enhedsvektorX, enhedsvektorY, enhedsvektorZ)


def Krydsprodukt(x1, y1, z1, x2, y2, z2):
    krydsproduktX = (y1 * z2) - (z1 * y2)
    krydsproduktY = (z1 * x2) - (x1 * z2)
    krydsproduktZ = (x1 * y2) - (y1 * x2)

    return(krydsproduktX, krydsproduktY, krydsproduktZ)