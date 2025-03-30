import numpy as np 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Mise en eq du E progageant de l'inforâtion
# Determonation puissance et forme du signal recu par l'appareil
# Voir la dif si on ajoute des obstacles
# Visualisation

#####kx = 10**-1.5, w = 10**5.52


LAMBDA = 1
c = 3*10**8
EPSILON0 = 8.85*10**-12
MU0 = 4*np.pi*10**-7


def sigma(shape):
    return np.zeros(shape)


def mettre_a_x(G, n, x):
    # Vérification des dimensions
    if n < 0 or n > 2:
        raise ValueError("L'axe n doit être compris entre 0 et 2.")
    if len(G.shape) != 3:
        raise ValueError("Le tableau G doit être de dimension 3.")

    # Copie du tableau G pour éviter les modifications inattendues
    G_modifie = np.copy(G)

    # Mettre la première composante à zéro le long de l'axe n
    debut_slice = [slice(None)] * 3
    debut_slice[n] = 0
    G_modifie[tuple(debut_slice)] = x

    # Mettre la dernière composante à zéro le long de l'axe n
    fin_slice = [slice(None)] * 3
    fin_slice[n] = -1
    G_modifie[tuple(fin_slice)] = 0

    return G_modifie


def derivee(G,Coords = []):
    if len(Coords) == 0:
        return G 
    else:
        G = np.gradient(G, axis = Coords[0])
        G =  mettre_a_x(G,Coords[0],0)
        return derivee(G, Coords[1:])
    
def interpolate(X,Y):
    return np.polynomial.Polynomial.fit(X,Y,len(X)-1)

def prolongement(X,Y,z):
    return interpolate(X,Y)(z)

def integrale(Ensemble,G):
    SommeG = 0
    n = 0
    for nx,x in enumerate(Ensemble):
        for ny,y in enumerate(x):
            for nz,z in enumerate(y):
                if z:
                    SommeG += G[nx,ny,nz]
                    n +=1
    if n == 0:
        return 0
    return SommeG/n

#def vectoriel(a,b)

def rotationnel(G):
    # Calcul des dérivées partielles du champ vectoriel
    dG_dx = derivee(G, [0])
    dG_dy = derivee(G, [1])
    dG_dz = derivee(G, [2])
    
    # Calcul des composantes du rotationnel
    R_x = dG_dz[1] - dG_dy[2]
    R_y = dG_dx[2] - dG_dz[0]
    R_z = dG_dy[0] - dG_dx[1]
    
    # Empiler les composantes du rotationnel pour former un vecteur
    rotG = np.stack((R_x, R_y, R_z), axis=-1)
    
    # Retourner le rotationnel sous forme de vecteur
    return rotG

def plot_3d_array(array):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    x = np.arange(array.shape[1])
    y = np.arange(array.shape[0])
    X, Y = np.meshgrid(x, y)
    
    ax.plot_surface(X, Y, array)
    
    ax.set_xlabel('t')
    ax.set_ylabel('x')
    ax.set_zlabel('E')
    
    plt.show()

def divergence(G):
    # Calcul des dérivées partielles selon chaque dimension de G
    dG_dx = derivee(G, [0])
    dG_dy = derivee(G, [1])
    dG_dz = derivee(G, [2])
    
    # Somme des dérivées partielles pour obtenir la divergence
    divG = dG_dx[0] + dG_dy[1] + dG_dz[2]
    
    return divG

def laplacien(G):
    # Calcul des dérivées partielles premières du champ scalaire G
    d2Gdx = derivee(G,[0,0])
    d2Gdy = derivee(G,[1,1])
    d2Gdz = derivee(G,[2,2])

    # Empiler les composantes du laplacien 
    
    return d2Gdx + d2Gdy + d2Gdz

def laplacien_vectoriel(G):
    laplacien_G_x = laplacien(G[...,0])
    laplacien_G_y = laplacien(G[...,1])
    laplacien_G_z = laplacien(G[...,2])

    
    
    return np.stack((laplacien_G_x,laplacien_G_y,laplacien_G_z), axis = -1)

def propagation(E0, dE_dt0, Sigma, Temps = 100, dt = 10**-6):
    E = [E0]
    dE_dt = dE_dt0
    for t in range(Temps-1):
        d2E_dt2 = c**2*(laplacien_vectoriel(E[-1])-MU0*Sigma*dE_dt)*dt
        for j in range(3):
            for k in range(3):
                dE_dt[...,k] = mettre_a_x(dE_dt[...,k],j,0)
                E[-1][...,k] = mettre_a_x(E[-1][...,k],j,0)
        dE_dt = dE_dt + d2E_dt2*dt
        E.append(E[-1] + dE_dt*dt)
        #print(np.max(E[-1]))
    return E

def sinus(A,x,y,z,ky=0,kx=10**-1.5,kz=0):
    return A*np.sin(kx*x+ky*y+kz*z)

def sinus1(A,x,y,z,ky=0,kx=10**-1.5-10**-0.5,kz=0):
    return A*np.sin(kx*x+ky*y+kz*z)

def sinus2(A,x,y,z,ky=0,kx=10**+1.5-10**-0.5,kz=0):
    return A*np.sin(kx*x+ky*y+kz*z)

def cosinus(A,x,y,z,ky=0,kx = 10**-1.5,kz=0):
    return A*np.cos(kx*x+ky*y+kz*z)

def cosinus1(A,x,y,z,ky=0,kx=10**-1.5-10**-0.5,kz=0):
    return A*np.cos(kx*x+ky*y+kz*z)

def cosinus2(A,x,y,z,ky=0,kx=10**-1.5+10**-0.5,kz=0):
    return A*np.cos(kx*x+ky*y+kz*z)

def gauss(A, y, x, z, ky = 10**-1.5, kx = 10**0, kz = 0):
    return A*np.exp(-(x*kx)**2-(y*ky)**2-(z*kz)**2)

def unit(A,x,y,z):
    return A

def dirac(A,x,y,z):
    if (x,y,z == 0):
        return A 
    else:
        return 0

def enveloppe(A,x,y,z,ky=0,kx=10**-1.3,kz=0):
    return A*(1.1+np.sin(kx*x+ky*y+kz*z))*np.sin((kx*x+ky*y+kz*z)*10)

def onde(f = (unit,unit,sinus), X = (50,50,50,100) , Y = (50,50,50,100), Z = (50,50,50,100), A = (0,0,1)):
    return np.array([[[[f[p](A[p],i-X[p],j-Y[p],k-Z[p]) if i >= 80 else 0 for p in range(3)] for k in range(Z[3])] for j in range(Y[3])] for i in range(X[3])]) 

def animation(E, dt):
    fig, ax = plt.subplots()
    line, = ax.plot([], [])

    def init():
        ax.set_xlim(0, len(E[0]))
        ax.set_ylim(np.min(E), np.max(E))
        return line,

    def update(frame):
        line.set_data(range(len(E[0])), E[frame])
        return line,
    #print("b")
    anim = FuncAnimation(fig, update, frames=len(E), init_func=init, blit=True, interval=dt*1000)
    plt.show()

# Exemple d'utilisation

T = 250
X = 1000
Y = 5
Z = 5
cx = 4
cy = 2
cz = 2
E0 = onde((unit,unit,sinus), (X//cx,X//cx,X//cx,X) , (Y//cy,Y//cy,Y//cy,Y), (Z//cz,Z//cz,Z//cz,Z), (0,0,1))
dE_dt0 = onde((unit,unit,cosinus), (X//cx,X//cx,X//cx,X) , (Y//cy,Y//cy,Y//cy,Y), (Z//cz,Z//cz,Z//cz,Z), (0,0,10**5.52))

SIGMA = np.array([[[0 if i> 80 else 1 for k in range(Z)] for j in range(Y)] for i in range(X)])
#SIGMA = np.exp(-SIGMA**2)
SIGMA = SIGMA[..., np.newaxis]
X1,Y1 = np.meshgrid(list(range(X)),list(range(Y)))
E = np.array(propagation(E0,dE_dt0,SIGMA,T))
#E = np.array([E0]*100)
#print(E.shape)
E = E[:,:600,Y//cy,Z//cz,2]
print(E.shape)


"""E_ech = E[:,X//cx]
plt.plot(E_ech**2)
plt.show()"""

dt = 0.01  # Interval de temps entre chaque frame en secondes
animation(E, dt)
# Creating figure


plot_3d_array(E)
