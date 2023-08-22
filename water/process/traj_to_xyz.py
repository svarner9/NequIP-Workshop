from ase.io.trajectory import Trajectory
from ase.io import write

traj = Trajectory('train.traj', 'r')
print(len(traj))
write('train.xyz', traj, format='extxyz')