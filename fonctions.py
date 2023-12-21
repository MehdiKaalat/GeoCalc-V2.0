from scipy.integrate import quad
import math
import numpy
import mpmath as mp

a = 6378249.2
b = 6356515
e2 = (a**2 - b**2)/a**2
E = 4 * ((b * b) * math.pi * 1.00465)

def M(phi):
    phi = math.radians(phi)
    M = (a*(1-e2)) / (1 - e2 * (math.sin(phi)) ** 2) ** (3 / 2)
    return M
def N(phi):
    phi = math.radians(phi)
    M = a / math.sqrt(1 - e2 * (math.sin(phi)) ** 2)
    return M

# fonction 1 :longueur d'arc de meridien ( input : phi1 et phi2)
def longueur_arc_meridien(phi1, phi2):
    phi1_rad = math.radians(phi1)
    phi2_rad = math.radians(phi2)
    def f(phi):
        return (1 - e2 * math.sin(phi) ** 2) ** (-3 / 2)
    result_phi1 = quad(f, 0, phi1_rad)
    result_phi2 = quad(f, 0, phi2_rad)
    S_phi1 = a * (1 - e2) * result_phi1[0]
    S_phi2 = a * (1 - e2) * result_phi2[0]
    S = S_phi2 - S_phi1
    S_km = S/1000
    return  S_km
def LongueurArcParallele(phi, lambda1, lambda2):
    phi_rad = math.radians(phi)
    lambda1_rad = math.radians(lambda1)
    lambda2_rad = math.radians(lambda2)
    W = math.sqrt(1-e2*math.sin(phi_rad)**2)
    N= a/W
    Rp = N*math.cos(phi_rad)
    deltaLambda = abs(lambda2_rad - lambda1_rad)
    L = Rp*deltaLambda
    L_km = L/1000
    return L_km

# Fonction 3 : Calcul de surface sur l’ellipsoïde

def surfaceSurEllipsoide(phi1, phi2, lambda1, lambda2):
    phi1_rad = math.radians(phi1)
    phi2_rad = math.radians(phi2)
    lambda1_rad = math.radians(lambda1)
    lambda2_rad = math.radians(lambda2)

    def f(phi):
        return math.cos(phi)*(1-e2*math.sin(phi)**2)**(-2)
    result, error = quad(f,phi1_rad,phi2_rad)
    Z = b**2*abs(lambda2_rad-lambda1_rad)*result
    Z_km2 = Z/1000000
    return Z_km2


# Fonction 4 : calcul des latitudes
# phi donnée
def dePhiAPsi_affichage(phi,a_ellipse,b_ellipse):
    phi_rad = math.radians(phi)
    psi_deg =math.degrees(math.atan(((b_ellipse**2) / (a_ellipse**2)) * math.tan(phi_rad)))
    return psi_deg
def dePhiABeta_affichage(phi,a_ellipse,b_ellipse):
    phi_rad = math.radians(phi)
    beta_deg = math.degrees(math.atan(b_ellipse * math.tan(phi_rad) / a_ellipse))
    return beta_deg
def dePhiAPsi(phi):
    e2 = (a ** 2 - b ** 2) / a ** 2
    phi_rad = math.radians(phi)
    psi_deg =math.degrees(math.atan((1 - e2) * math.tan(phi_rad)))
    return psi_deg
def dePhiABeta(phi):
    phi_rad = math.radians(phi)
    beta_deg = math.degrees(math.atan(b * math.tan(phi_rad) / a))
    return beta_deg

# beta donnée
def deBetaAPhi_affichage(Beta,a_ellipse,b_ellipse):
    beta_rad = math.radians(Beta)
    phi_deg = math.degrees(math.atan(a_ellipse * math.tan(beta_rad) / b_ellipse))
    return phi_deg
def deBetaAPsi_affichage(Beta,a_ellipse,b_ellipse):
    beta_rad = math.radians(Beta)
    psi_deg = math.degrees(math.atan(b_ellipse * math.tan(beta_rad) / a_ellipse))
    return psi_deg

def deBetaAPhi(Beta):
    beta_rad = math.radians(Beta)
    phi_deg = math.degrees(math.atan(a * math.tan(beta_rad) / b))
    return phi_deg
def deBetaAPsi(Beta):
    beta_rad = math.radians(Beta)
    psi_deg = math.degrees(math.atan(b * math.tan(beta_rad) / a))
    return psi_deg

# psi donnée
def dePsiABeta_affichage(Psi,a_ellipse,b_ellipse):
    psi_rad = math.radians(Psi)
    beta_deg = math.degrees(math.atan(a_ellipse * math.tan(psi_rad) / b_ellipse))
    return beta_deg
def dePsiAPhi_affichage(Psi,a_ellipse,b_ellipse):
    psi_rad = math.radians(Psi)
    phi_deg = math.degrees(math.atan((a_ellipse**2) * math.tan(psi_rad) / (b_ellipse**2)))
    return phi_deg

def dePsiABeta(Psi):
    psi_rad = math.radians(Psi)
    beta_deg = math.degrees(math.atan(a * math.tan(psi_rad) / b))
    return beta_deg
def dePsiAPhi(Psi):
    psi_rad = math.radians(Psi)
    phi_deg = math.degrees(math.atan((a**2) * math.tan(psi_rad) / (b**2)))
    return phi_deg


# Fonction 5 : probleme direct ellipsoide :
def pbDirectEllipsoidePuissant_rigoureuse(Phi1, lam1, S, A12):
    Phi1 = math.radians(Phi1)
    lam1 = math.radians(lam1)
    A12 = math.radians(A12)
    M1 = M(Phi1)
    N1 = N(Phi1)
    deltaPhiPrime = (
            S * math.cos(A12) / N1
            - (S / N1) ** 2 / 2 * math.tan(Phi1) * math.sin(A12) ** 2
            - (S / N1) ** 3 / 6 * math.cos(A12) * math.sin(A12) ** 2 * (1 + 3 * math.tan(Phi1) ** 2)
    )

    B = 1 / M1
    C = 3 / 2 * e2 * math.sin(Phi1) * math.cos(Phi1) / (1 - e2 * math.sin(Phi1) ** 2)
    D = math.tan(Phi1) / (2 * M1 * N1)
    E = (1 + 3 * math.tan(Phi1) ** 2) / (6 * N1 ** 2)
    h = S * math.cos(A12) / M1
    sigmaPhi = N1 * deltaPhiPrime / M1

    deltaPhi = (
            S * math.cos(A12) * B
            - S ** 2 * math.sin(A12) ** 2 * D
            - h * S ** 2 * math.sin(A12) ** 2 * E
            - C * sigmaPhi ** 2
    )
    Phi2 = Phi1 + deltaPhi

    N2 = N(Phi2)
    deltaLam = (
            S
            / N2
            * math.sin(A12)
            / math.cos(Phi2)
            * (1 - 6 * (S / N2) ** 2 * (1 - (math.sin(A12) / math.cos(Phi2)) ** 2))
    )
    lam2 = lam1 + deltaLam

    PhiMoyenne = (Phi1 + Phi2) / 2
    deltaAzimut = 2 * math.atan(1/(math.cos(deltaPhi / 2) / math.sin(PhiMoyenne) * 1/math.tan(deltaLam / 2)))

    # A21 = A12 + deltaAzimut + pi
    A21 = A12 + deltaAzimut + math.pi
    # if A21 >= 2 * pi:
    #     A21 -= 2 * pi
    Phi2 = math.degrees(Phi2)
    lam2 = math.degrees(lam2)
    A21 = math.degrees(A21)
    return Phi2, lam2, A21
    # A21 = A12 + deltaAzimut

    return Phi2 , lam2 , (2 * pi - A21)

def pbDirectEllipsoidePuissant_simplifie(Phi1, lam1, S, A12):
    Phi1 = math.radians(Phi1)
    lam1 = math.radians(lam1)
    A12 = math.radians(A12)
    M1 = M(Phi1)
    N1 = N(Phi1)
    deltaPhiPrime = (
        S * math.cos(A12) / N1
        - (S / N1) ** 2 / 2 * math.tan(Phi1) * math.sin(A12) ** 2
        - (S / N1) ** 3 / 6 * math.cos(A12) * math.sin(A12) ** 2 * (1 + 3 * math.tan(Phi1) ** 2)
    )
    B = 1 / M1
    C = 3 / 2 * e2 * math.sin(Phi1) * math.cos(Phi1) / (1 - e2 * math.sin(Phi1) ** 2)
    D = math.tan(Phi1) / (2 * M1 * N1)
    sigmaPhi = N1 * deltaPhiPrime / M1

    deltaPhi = S * math.cos(A12) * B - (S * math.sin(A12)) ** 2 * D - sigmaPhi**2 * C
    Phi2 = Phi1 + deltaPhi

    N2 = N(Phi2)
    deltaLam = S * math.sin(A12) / (N2 * math.cos(Phi2))

    lam2 = lam1 + deltaLam

    PhiMoyenne = (Phi1 + Phi2) / 2
    deltaAzimut = deltaLam * math.sin(PhiMoyenne)

    A21 = A12 + deltaAzimut + math.pi
    Phi2 = math.degrees(Phi2)
    lam2 = math.degrees(lam2)
    A21 = math.degrees(A21)
    return Phi2 , lam2 , A21


def pbDirectEllipsoideGauss(Phi1, lam1, S, A12, erreurPhi, erreurLam, erreurA):

    deltaLam = []

    # étape 0
    deltaA = [0]
    deltaPhi = [0]
    Mm = (float(a) * (1 - e2)) / ((1 - e2 * math.sin(Phi1) ** 2) ** (3 / 2))
    Nm = (float(a)) / ((1 - e2 * math.sin(Phi1) ** 2) ** (1 / 2))

    Phim = Phi1

    deltaLam.append(S * math.sin(A12 + deltaA[-1] / 2) / (Nm * math.cos(Phim)))
    deltaA.append(2 * math.atan(math.tan(deltaLam[-1] / 2) * math.sin(Phim) / math.cos(deltaPhi[-1] / 2)))
    deltaPhi.append(S * math.cos(A12 + deltaA[-1] / 2) / (Mm * math.cos(deltaLam[-1] / 2)))

    Phi2 = [Phi1]
    lam2 = [lam1]
    A21 = [A12]

    Phi2.append(deltaPhi[-1] + Phi2[-1])
    lam2.append(deltaLam[-1] + lam2[-1])
    if deltaA[-1] + A21[-1] > math.pi:
        A21.append(deltaA[-1] + A21[-1] - math.pi)
    else:
        A21.append(deltaA[-1] + A21[-1] + math.pi)

    while (
            abs(Phi2[-2] - Phi2[-1]) > erreurPhi
            or abs(lam2[-2] - lam2[-1]) > erreurLam
            or abs(A21[-2] - A21[-1]) > erreurA
    ):
        Nm = ((float(a)) / ((1 - e2 * math.sin(Phi2[-1]) ** 2) ** (1 / 2)) + (float(a)) / (
                    (1 - e2 * math.sin(Phi1) ** 2) ** (1 / 2))) / 2
        Phim = (Phi2[-1] + Phi1) / 2
        Mm = ((float(a) * (1 - e2)) / ((1 - e2 * math.sin(Phi2[-1]) ** 2) ** (3 / 2)) + (float(a) * (1 - e2)) / (
                    (1 - e2 * math.sin(Phi1) ** 2) ** (3 / 2))) / 2

        deltaLam.append(S * math.sin(A12 + deltaA[-1] / 2) / (Nm * math.cos(Phim)))
        deltaA.append(
            2 * math.atan(math.tan(deltaLam[-1] / 2) * math.sin(Phim) / math.cos(deltaPhi[-1] / 2))
        )
        deltaPhi.append(S * math.cos(A12 + deltaA[-1] / 2) / (Mm * math.cos(deltaLam[-1] / 2)))

        Phi2.append(deltaPhi[-1] + Phi1)
        lam2.append(deltaLam[-1] + lam1)
        A21.append(deltaA[-1] + A12)


    phi2_VF = Phi2[-1]
    lam2_VF = lam2[-1]
    A21_VF = A21[-1] + 180
    return phi2_VF, lam2_VF, A21_VF

# Fonction 5 : probleme inverse ellipsoide :
def pbInverseEllipsoideGauss(phi1, lam1, phi2, lam2):
    phi1 = math.radians(phi1)
    phi2 = math.radians(phi2)
    lam1 = math.radians(lam1)
    lam2 = math.radians(lam2)
    deltaPhi = phi2 - phi1
    PhiMoyenne = (phi1 + phi2) / 2
    deltaLam = lam2 - lam1
    Nm = (N(phi2) + N(phi1)) / 2
    Mm = (M(phi2) + M(phi1)) / 2

    deltaA = 2 * math.atan(1/(math.cos(deltaPhi / 2) / math.sin(PhiMoyenne) * 1/math.tan(deltaLam / 2)))
    A12 = (
        math.atan(math.cos(PhiMoyenne) * math.tan(deltaLam / 2) / math.sin(Mm * deltaPhi / (2 * Nm)))
        - deltaA / 2
    )
    S = deltaPhi * Mm * math.cos(deltaLam / 2) / math.cos(A12 + deltaA / 2)

    A21 = A12 + deltaA + math.pi

    A12 = A12 * 180/math.pi
    A21 = A21 * 180/math.pi

    return A12, A21, S
# prb direct sur sphere :
def probleme_direct_sphere(phi1, lambda1, S, A12, rayon_choisi):
    phi1 = math.radians(phi1)
    lambda1 = math.radians(lambda1)
    A12 = math.radians(A12)
    if rayon_choisi == "Rayon moyen de Gauss":
        rayon = calcul_rayon_Gauss()
        sigma12 = S / rayon
    elif rayon_choisi == "Rayon moyen des demi-axes":
        rayon = calcul_rayon_moyen()
        sigma12 = S / rayon
    elif rayon_choisi == "Rayon d’une sphère de même superficie que l’ellipsoïde":
        rayon = calcul_rayon_a()
        sigma12 = S / rayon
    elif rayon_choisi == "Rayon d’une sphère de même volume que l’ellipsoïde":
        rayon = calcul_rayon_v()
        sigma12 = S / rayon
    # DETERMINATION DE LA LATITUDE DU POINT P2
    sinphi2 = math.sin(phi1) * math.cos(sigma12) + math.cos(phi1) * math.sin(sigma12) * math.cos(A12)
    phi2_degre = math.asin(sinphi2)
    # DETERMINATION DE LA Longitude DU POINT P2

    cot_delta_lambda = 1 / math.sin(A12) * (mp.cot(sigma12) * math.cos(phi1) - math.sin(phi1) * math.cos(A12))
    lambda_2_degre = lambda1 + mp.acot(cot_delta_lambda)

    # DETERMINATION DE L'AZIMUT DU POINT P2
    cot_A21 = (1 / math.sin(A12)) * (math.cos(sigma12) * math.cos(A12) - math.tan(phi1) * math.sin(sigma12))
    A21_degre =  math.pi/2 - math.atan(cot_A21)

    phi2_degre = (phi2_degre)*180/math.pi
    lambda_2_degre = (lambda_2_degre)*180/math.pi
    A21_degre = A21_degre*(180/math.pi) + 180
    return phi2_degre, lambda_2_degre, A21_degre
# prb inverse sur sphere :
def probleme_inverse_sphere(phi1,lambda1, phi2,lambda2):
    phi1 = math.radians(phi1)
    lambda1 = math.radians(lambda1)
    phi2 = math.radians(phi2)
    lambda2 = math.radians(lambda2)

    # Calcul de distance entre P1 et P2:
    delta_lambda = lambda2 - lambda1
    sigma12 = math.acos((math.sin(phi1) * math.sin(phi2) + math.cos(phi1) * math.cos(phi2) * math.cos(delta_lambda)))

    # Détermination de l’azimut A12
    cot1 = ((math.tan(phi2) * math.cos(phi1)) / math.sin(delta_lambda)) - ((math.sin(phi1)) * (1 / math.tan(delta_lambda)))
    A12 = (math.pi / 2) - (math.atan(cot1))

    # Détermination de l’azimut A21
    cot2 = -(((math.tan(phi1) * math.cos(phi2)) / math.sin(delta_lambda)) - (math.sin(phi2) * (1 / math.tan(delta_lambda))))
    A21 = (math.pi / 2) - math.atan(cot2)

    A12 = A12 * 180/math.pi
    A21 =A21 * 180/math.pi + 180
    sigma12 = sigma12 * 180/math.pi
    return A12, A21, sigma12

def calcul_rayon_moyen () :
    Rm=(2*a+b)/3
    return Rm

def calcul_rayon_a ():
    Ra= math.sqrt(E/4*math.pi)
    return Ra

def calcul_rayon_v ():
    Rv=(a*a*b)**(1/3)
    return Rv

def calcul_rayon_Gauss () :
    e = math.sqrt(a*a-b*b)/a
    phi = 45
    M = a*(1-e*e)/(1-e*e*(math.sin(phi)**2))**(3/2)
    N = a/math.sqrt(1-e*e*(math.sin(phi)**2))
    Rg= math.sqrt(M*N)
    return Rg

def coordGeo2Lambert(phi, L, zone):
    phi = phi * math.pi / 180
    L = L * math.pi / 180
    a = 6378249.2
    b = 6356515.0
    e2 = 1 - (pow(float(b), 2) / pow(float(a), 2))
    u = math.log(math.tan(math.pi / 4 + phi / 2)) - (e2 / 2) * math.log((1 + math.sqrt(e2) * math.sin(phi)) / (1 - math.sqrt(e2) * math.sin(phi)))

    if zone == "Zone 1":
        X0 = 500000
        Y0 = 300000
        L0 = -6 * math.pi / 200
        phi_0 = 37 * math.pi / 200
        K0 = 0.999625769
        u0 = math.log(math.tan(math.pi / 4 + phi_0 / 2)) - (e2 / 2) * math.log(
            (1 + math.sqrt(e2) * math.sin(phi_0)) / (1 - math.sqrt(e2) * math.sin(phi_0)))
        N0 = a / math.sqrt(1 - e2 * math.sin(phi_0) ** 2)
        e0 = K0 * N0 / (math.tan(phi_0))
        dU = (u - u0)
        dL = (L - L0)

    elif zone == "Zone 2":
        X0 = 500000
        Y0 = 300000
        L0 = -6 * math.pi / 200
        phi_0 = 33 * math.pi / 200
        K0 = 0.999615596
        u0 = math.log(math.tan(math.pi / 4 + phi_0 / 2)) - (e2 / 2) * math.log(
            (1 + math.sqrt(e2) * math.sin(phi_0)) / (1 - math.sqrt(e2) * math.sin(phi_0)))
        N0 = a / math.sqrt(1 - e2 * math.sin(phi_0) ** 2)
        e0 = K0 * N0 / (math.tan(phi_0))
        dU = (u - u0)
        dL = (L - L0)
    elif zone == "Zone 3":
        X0 = 1200000
        Y0 = 400000
        L0 = -6 * math.pi / 200
        phi_0 = 29 * math.pi / 200
        K0 = 0.999616304
        u0 = math.log(math.tan(math.pi / 4 + phi_0 / 2)) - (e2 / 2) * math.log(
            (1 + math.sqrt(e2) * math.sin(phi_0)) / (1 - math.sqrt(e2) * math.sin(phi_0)))
        N0 = a / math.sqrt(1 - e2 * math.sin(phi_0) ** 2)
        e0 = K0 * N0 / (math.tan(phi_0))
        dU = (u - u0)
        dL = (L - L0)
    elif zone == "Zone 4":
        X0 = 1500000
        Y0 = 400000
        L0 = -6 * math.pi / 200
        phi_0 = 25 * math.pi / 200
        K0 = 0.999616437
        u0 = math.log(math.tan(math.pi / 4 + phi_0 / 2)) - (e2 / 2) * math.log(
            (1 + math.sqrt(e2) * math.sin(phi_0)) / (1 - math.sqrt(e2) * math.sin(phi_0)))
        N0 = a / math.sqrt(1 - e2 * math.sin(phi_0) ** 2)
        e0 = K0 * N0 / (math.tan(phi_0))
        dU = (u - u0)
        dL = (L - L0)

    X = e0 * math.exp(-dU * math.sin(phi_0)) * math.sin(math.sin(phi_0) * dL) + X0
    Y = -e0 * (math.exp(-dU * math.sin(phi_0)) * math.cos(math.sin(phi_0) * dL) - 1) + Y0
    return X,Y

def lambert2Geo(X, Y, zone):
    if zone == "Zone 1":
        X = X - 500000
        Y = Y - 300000
        L0 = -6 * math.pi / 200
        phi_0 = 37 * math.pi / 200
        K0 = 0.999625769

    if zone == "Zone 2":
        X = (X - 500000)
        Y = Y - 300000
        L0 = -6 * math.pi / 200
        phi_0 = 33 * math.pi / 200
        K0 = 0.999615596

    if zone == "Zone 3":
        X = X - 1200000
        Y = Y - 400000
        L0 = -6 * math.pi / 200
        phi_0 = 29 * math.pi / 200
        K0 = 0.999616304

    if zone == "Zone 4":
        X = X - 1500000
        Y = Y - 400000
        L0 = -6 * math.pi / 200
        phi_0 = 25 * math.pi / 200
        K0 = 0.999616437

    # u0 = U(a, b, phi_0)
    u0 = math.log(math.tan(math.pi / 4 + phi_0 / 2)) - (e2 / 2) * math.log(
        (1 + math.sqrt(e2) * math.sin(phi_0)) / (1 - math.sqrt(e2) * math.sin(phi_0)))
    N0 = a / math.sqrt(1 - e2 * math.sin(phi_0) ** 2)
    e0 = K0 * N0 / math.tan(phi_0)

    # longitude Lambda
    L_c = (1 / (math.sin(phi_0))) * (math.atan(X / (e0 - Y)))
    L = (L_c + L0) * (180 / math.pi)

    # Latitude phi
    du = (1 / (2 * math.sin(phi_0))) * math.log(e0 ** 2 / (X ** 2 + (e0 - Y) ** 2))
    u = abs(du + u0)
    # E = log(tan((pi/4) + (phi_0/2))) - u

    E = (e2 / 2) * (math.log((1 + math.sqrt(e2) * math.sin(phi_0)) / (1 - math.sqrt(e2) * math.sin(phi_0))))

    phi = 2 * math.atan((math.exp(u + E) - 1) / (math.exp(u + E) + 1))
    liste_phi = [phi_0, phi]
    # print(liste_phi[0])
    # print(liste_phi[-1]*200/pi)

    while abs(liste_phi[-1] - liste_phi[-2]) >= 10 ** (-10):
        E = (e2 / 2) * (math.log((1 + math.sqrt(e2) * math.sin(liste_phi[-1])) / (1 - math.sqrt(e2) * math.sin(liste_phi[-1]))))
        phi = 2 * math.atan((math.exp(u + E) - 1) / (math.exp(u + E) + 1))
        liste_phi.append(phi)
    fi = (liste_phi[-1]) * (180 / math.pi)

    return L, fi

def dePhiAisometrique(phi):
    phi = math.radians(phi)
    U = math.log(math.tan((math.pi / 4) + (phi / 2))) - (e2 / 2) * math.log((1 + math.sqrt(e2) + math.sin(phi)) / (1 - math.sqrt(e2) + math.sin(phi)))
    return math.degrees(U)
def deIsometriqueAPhi(U,erreur_donnee):
    U = math.radians(U)
    e = math.sqrt(e2)
    phi_0 = 2 * math.atan(math.exp(U)) - math.pi / 2
    phi_1 = 2 * math.atan(((1 + e * math.sin(phi_0)) / (1 - e * math.sin(phi_0))) ** (e / 2) * math.exp(U)) - (math.pi / 2)
    erreur = abs(phi_0 - phi_1)
    while erreur > erreur_donnee:
        phi_0 = phi_1
        phi_1 = 2 * math.atan((1 + e * math.sin(phi_0)) / (1 - e * math.sin(phi_0)) ** (e / 2) * math.exp(U)) - (math.pi / 2)
        erreur = abs(phi_0 - phi_1)
    return math.degrees(phi_1)
