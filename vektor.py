import math
import matplotlib.pyplot as plt



def Vektor2Dsum(x1, y1, x2, y2):
    v1 = plt.arrow(0,0, x1, y1, head_width=0.1, head_length=0.1, length_includes_head=True, color="green")
    v2 = plt.arrow(x1,y1, x2, y2, head_width=0.1, head_length=0.1, length_includes_head=True, color="yellow")
    resultX = x1 + x2
    resultY = y1 + y2
    result = plt.arrow(0,0, resultX, resultY, head_width=0.1, head_length=0.1, length_includes_head=True, color="blue")
    VektorViser()
    return (resultX, resultY)


def Vektor2Dminus(x1, y1, x2, y2):
    resultx = x1 - x2
    resulty = y1 - y2
    a = resultx - x1
    b = resulty - y1
    v1 = plt.arrow(0,0, x1, y1, head_width=0.1, head_length=0.1, length_includes_head=True, color="green")
    v2 = plt.arrow(x1,y1, a, b, head_width=0.1, head_length=0.1, length_includes_head=True, color="yellow")
    result = plt.arrow(0,0, resultx, resulty, head_width=0.1, head_length=0.1, length_includes_head=True, color="red")
    VektorViser()
    return(resultx, resulty)


def Vektor2Dskalar(x1, y1, s):
    x = x1 * s
    y = y1 * s
    v1=plt.arrow(0,0, x, y, head_width=0.1, head_length=0.1, length_includes_head=True, color="black")
    VektorViser()
    return(x, y)

def Vektor2Dlengde(x1, y1):
    return(math.sqrt(x1**2 + y1**2))

def Vektor2Dvinkel(x1, y1):
    vinkel=(math.degrees(math.atan2(y1, x1)))
    return vinkel


def PolaerKoordinater(x, y):
    r = math.sqrt(x**2 + y**2)
    vinkel = math.atan2(y, x)
    v1= plt.arrow(0,0, x, y, head_width=0.1, head_length=0.1, length_includes_head=True, color="black")
    VektorViser()
    return (r, math.degrees(vinkel))


def KartesianKordinater (vinkel, lengde):

    x=lengde * math.cos(vinkel)
    y=lengde * math.sin(vinkel)

    return(x, y)



def Vektor2Dprikprodukt(x1, y1, x2, y2):
    resultx = x1 * x2
    resulty = y1 * y2
    result= resultx + resulty
    v1=plt.arrow(0,0, resultx, resulty, head_width=0.1, head_length=0.1, length_includes_head=True, color="black")
    VektorViser()
    return (result)



def Vektor2Denhedsvektor(x1, y1):

    lengde = Vektor2Dlengde(x1, y1)


    if lengde == 0:
        return ("Nulvektor har ingen enhedsvektor")
    
    enhedsvektorX = x1 / lengde
    enhedsvektorY = y1 / lengde
    
    
    v1=plt.arrow(0, 0, x1, y1, head_width=0.1, head_length=0.1, length_includes_head=True, color="black")

    e1=plt.arrow(0, 0, enhedsvektorX, enhedsvektorY, head_width=0.1, head_length=0.1, length_includes_head=True, color="red")

    VektorViser()


    return(enhedsvektorX, enhedsvektorY)


def PunktTilVektor(p1x, p1y, p2x, p2y):
    x=p1x-p2x
    y=p1y-p2y

    v1=plt.arrow(p1x, p1y, x, y, head_width=0.1, head_length=0.1, length_includes_head=True, color="black")
    VektorViser()

    return(x, y)



def Vektorvinkelimellem2D(x1, y1, x2, y2):
    
    prik = Vektor2Dprikprodukt(x1, y1, x2, y2)
    lengde1 = Vektor2Dlengde(x1, y1)
    lengde2 = Vektor2Dlengde(x2, y2)

    if lengde1 == 0 or lengde2 == 0:
        return "Man kan ikke finde vinklen med en nulvektor"

    vinkel = math.acos(prik / (lengde1 * lengde2))
    return math.degrees(vinkel)
    

#############################################################
# Vektor3D funktioner
# fig = papir
# ax = kordinantsystemet
#############################################################
fig = None
ax = None


def Scale(x,y,z,x1,y1,z1,x2,y2,z2):
    scaleBack=min(0,x,y,z,x1,y1,z1,x2,y2,z2)
    scaleForward=max(0,x,y,z,x1,y1,z1,x2,y2,z2)

    ax.set_xlim(scaleBack, scaleForward)
    ax.set_ylim(scaleBack, scaleForward)
    ax.set_zlim(scaleBack, scaleForward)


def plot ():
    global fig, ax
    if fig == None:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")



def Vektor3Dsum(x1, y1, z1, x2, y2, z2):
    plot()

    # Første vektor
    ax.quiver(0, 0, 0, x1, y1, z1, color="green")

    # Anden vektor starter der hvor første slutter
    ax.quiver(x1, y1, z1, x2, y2, z2, color="yellow")

    resultX = x1 + x2
    resultY = y1 + y2
    resultZ = z1 + z2

    # Resultatvektor
    ax.quiver(0, 0, 0, resultX, resultY, resultZ, color="blue")

    Scale(resultX, resultY, resultZ, x1, y1, z1, x2, y2, z2)
    VektorViser3D()

    return (resultX, resultY, resultZ)



def Vektor3Dminus(x1, y1, z1, x2, y2, z2):
   global fig, ax
   plot()

 # Første vektorer
   ax.quiver(0,0,0,x1,y1,z1, color="green")


 # anden vektorer
   ax.quiver(x1, y1, z1, -x2, -y2, -z2, color="yellow")


   resultx=x1 - x2
   resulty=y1 - y2
   resultz=z1 - z2

   #resultvektorer
   ax.quiver(0,0,0,resultx,resulty,resultz, color="blue")

   Scale(resultx, resulty, resultz, x1, y1, z1, x2, y2, z2)

   VektorViser3D()

   return(resultx, resulty, resultz)





def Vektor3Dskalar(x1, y1, z1, s):
    global fig,ax
    plot()

    #første vektorer
    ax.quiver(0,0,0,x1,y1,z1, color="green")
   
    #scalar vektorer

    scalx=x1*s
    scaly=y1*s
    scalz=z1*s
   
    v1=ax.quiver(0,0,0,scalx,scaly,scalz,color="red")

    Scale(scalx, scaly, scalz, x1, y1, z1, 0, 0, 0)

    VektorViser3D()

    return(scalx, scaly, scalz)





def Vektor3Dlengde(x1, y1, z1):
     
    lengde=math.sqrt(x1**2 + y1**2 + z1**2)

    return(lengde)




def Vektor3Dprikprodukt(x1, y1, x2, y2, z1, z2):
    global fig, ax
    plot()

    #første vektorer
    ax.quiver(0, 0, 0, x1, y1, z1, color="green")


    #anden vektorer
    ax.quiver(0, 0, 0, x2, y2, z2, color="yellow")

    prikx= x1 * x2
    priky= y1 * y2
    prikz= z1 * z2

    result= prikx + priky + prikz

    v1=ax.quiver(0,0,0,prikx, priky, prikz, color="blue")
    Scale(prikx, priky, prikz, x1, y1, z1, x2, y2, z2)
    VektorViser3D()
    return(result)

    

def Vektor3Denhedsvektor(x1, y1, z1):
    global fig, ax
    
    plot()

    #lengde
    lengde=math.sqrt(x1**2 + y1**2 + z1**2)

    

    #første vektorer
    ax.quiver(0, 0, 0, x1, y1, z1, color="green")

    enhedx= x1 / lengde
    enhedy= y1 / lengde
    enhedz= z1 / lengde

    #enheds vektorer
    ax.quiver(0, 0, 0, enhedx, enhedy, enhedz, color="red")

    Scale(x1, y1, z1, enhedx, enhedy, enhedz, 0, 0, 0)
    VektorViser3D()
    return(enhedx, enhedy, enhedz)



def PunktTilVektor3D (p1x, p1y, p1z, p2x, p2y, p2z):
    global fig, ax
    plot()
    
    kordx= p2x - p1x
    kordy= p2y - p1y
    kordz= p2z - p1z

    #vektor
    ax.quiver(p1x, p1y, p1z, p2x, p2y, p2z, color="green")

    Scale(p1x, p1y, p1z, p2x, p2y, p2z, kordx, kordy, kordz)
    VektorViser3D()

    return(kordx, kordy, kordz)

    



def Krydsprodukt(x1, y1, z1, x2, y2, z2):
    global fig, ax
    plot()

    #første vektorer
    ax.quiver(0, 0, 0, x1, y1, z1, color="green")

    #anden vektorer
    ax.quiver(0, 0, 0, x2, y2, z2, color="yellow")

    krydsx= (y1 * z2) - (z1 * y2)
    krydsy= (z1 * x2) - (x1 * z2)
    krydsz= (x1 * y2) - (y1 * x2)

    #slut vektor
    ax.quiver(0, 0, 0, krydsx, krydsy, krydsz, color="blue")
    Scale(krydsx, krydsy, krydsz, x1, y1, z1, x2, y2, z2)
    VektorViser3D()

    return(krydsx, krydsy, krydsz)


def VektorViser():
    plt.autoscale()

    plt.grid()
    plt.show()


def VektorViser3D():
    plot()
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.grid()
    plt.show()