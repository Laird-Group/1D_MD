import numpy as np

def harmonic(pparams):
    k = float(pparams[0])
    def force(x):
        return -k*x
    return force

def quartic(pparams):
    k = float(pparams[0])
    def force(x):
        return -k*(x**3) + k*x
    return force

def morse(pparams):
    D_e = float(pparams[0])
    nu_e = float(pparams[1])
    mu = float(pparams[2])
    x_e = float(pparams[3])
    def force(x):
        return 2*D_e*(np.pi*nu_e*(2*mu/D_e)**0.5)*(1-np.exp(-(np.pi*nu_e*(2*mu/D_e)**0.5)*(x-x_e)))
    return force

def free_particle(a):
    def force(x):
        return 0
    return force

potential_Dict = {'None': free_particle, 'Harmonic':harmonic, 'Quartic':quartic,  'Morse': morse}

def choose_potential(potential):
    return potential_Dict[potential]
