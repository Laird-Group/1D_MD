import numpy as np

def harm_osc_soln(params):
    k=float(params["potparams"][0])
    print(k)
    w=np.sqrt(k/params["m"])
    x=[]
    p=[]
    t_an=[]
    for step in range(params["run"]):
        t=step*params["dt"]
        x.append(params["xo"]*np.cos(w*t)+params["vo"]/w*np.sin(w*t))
        p.append(params["m"]*params["vo"]*np.cos(w*t)-params["m"]*w*params["xo"]*np.sin(w*t))
        t_an.append(t)
    np.savetxt("traj_analytical.dat", np.c_[t_an, x,p])
    return
