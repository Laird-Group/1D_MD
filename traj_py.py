def traj(params, tfile, t):
    tfile.write(f'{t} {params["xo"]} {params["vo"]} \n')
