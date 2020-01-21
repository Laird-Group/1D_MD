import numpy as np

def velocity_verlet(params,F):
    """
    This is a standard velocity verlet integrator
    """
    x=params["xo"] + params["dt"]*params["vo"]+ params["dt"]**2./(2.0*params["m"])*F(params["xo"])
    v=params["vo"] + params["dt"]/(2.0*params["m"])*(F(params["xo"]) + F(x))
    params["xo"],params["vo"] = x,v
    return

def A(params,F):
    """
    This is the friction kernal
    """
    kb=0.0019872041
    epsilon = np.random.normal()
    theta = np.random.normal()
    gamma=float(params["thermoparams"][0])
    T = float(params["thermoparams"][1])
    s=np.sqrt(2.0*kb*T*gamma/params["m"])
    a=0.5*params["dt"]**2.*(F(params["xo"])/params["m"]-gamma*params["vo"]) + s*params["dt"]**(3./2.)*(0.5*epsilon+1/(2.0*np.sqrt(3.0))*theta)
    return a, epsilon, theta, gamma, s

def langevin(params,F):
    """
    This is a langevin integrator
    """
    a, eps, thet, gam, sig = A(params,F)
    x = params["xo"] + params["dt"]*params["vo"] + a
    v = params["vo"] + 0.5*params["dt"]/params["m"]*(F(x)+F(params["xo"]))-params["dt"]*gam*params["vo"]+sig*np.sqrt(params["dt"])*eps-gam*a
    params["xo"],params["vo"] = x,v
    return

# def Nose_Hoover(params,F):


def int_choice(integrator):
    choose = { "vverlet":velocity_verlet, "langevin":langevin}
    return choose[integrator]
