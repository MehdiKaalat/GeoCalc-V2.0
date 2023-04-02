from math import *
#Pour la conversion des coordonnees
def dms2rad (d,m,s) :
    Degree = float(d+(m+s/60)/60)
    Rad=Degree*(pi/180)
    return Rad


def rad2dms2(S):
    seconde = float(180 * S / pi * 3600)
    s = seconde % 60
    m = seconde // 60
    d = m // 60
    m = m % 60
    return (d,m,s)

#Pour  la resolution des problèmes geodesiques
def dms2rad2(degrees, minutes, seconds):
    if degrees < 0:
        dd = float(degrees) - (float(minutes) / 60) - float(seconds) / (60 * 60)
    else:
        dd = float(degrees) + (float(minutes) / 60) + float(seconds) / (60 * 60)

    Rad = dd * (pi / 180)
    return Rad


def rad2dms(W):
    d = float(180 * W / pi )
    if d<0:
        md = d - (int(d))
        m =(md * 60)*-1
        mf = int(m)
        ss =( m - int(m))
        s = (ss * 60)
        dd = int(d)
    else :
        md =d-(int(d))
        m = md * 60
        mf=int(m)
        ss = m -int(m)
        s=ss * 60
    dd=int(d)
    return (dd,mf,s)

