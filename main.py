""" Integrator for a single one dimensional particle in an external
potential """

import numpy as np
import argparse
import force
import integrator
import traj_py
from analytic import harm_osc_soln

parser = argparse.ArgumentParser()
parser.add_argument('-xo', help='Initial Position')
parser.add_argument('-vo', help='Initial Velocity')
parser.add_argument('-run', default=int(100), help='Number of MD steps')
parser.add_argument('-dt', default=float(0.1), help='Timestep')
parser.add_argument('-potparam', default=[1.0], nargs='+',
                    help='Potential Parameters')
parser.add_argument('-thermoparams', default=[1.0], nargs='+',
                    help='Thermostat parameters')
parser.add_argument('-integrator', default="vverlet", type=str,
                    help='Choose an integrator to use. Currently available:'+\
                    '\n vverlet, langevin')
parser.add_argument('-m', default=float(1.0), help='Mass')
parser.add_argument('-potential', default="None",
                    help="External potential the particle feels. Choices:" +\
                    "\n Harmonic, Quartic, Morse")
parser.add_argument('-traj', default="trajectory.dat",
                    help="Name of the trajectory file")
args = parser.parse_args()

if args.xo == None:
    args.xo = np.random.rand()
if args.vo == None:
    args.vo = np.random.rand()

params = { "xo":float(args.xo), "vo":float(args.vo), "run":int(args.run),
          "dt":float(args.dt), "potparams":args.potparam,
          "m":float(args.m), "integrator":args.integrator,
          "potential": str(args.potential),
          "trajectory":str(args.traj), "thermoparams":args.thermoparams}

tfile = open(params["trajectory"], 'w')
integrate = integrator.int_choice(params["integrator"])
force = force.choose_potential(params['potential'])
force_eval = force(params["potparams"])
harm_osc_soln(params)

traj_py.traj(params, tfile, 0)
for i in range(params["run"]):
    integrate(params, force_eval)
    t=i*params["dt"]
    traj_py.traj(params, tfile,t)

tfile.close()
