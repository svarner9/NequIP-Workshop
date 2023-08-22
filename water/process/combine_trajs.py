from ase.io.trajectory import Trajectory
from ase.io import write

file1 = '/lcrc/project/nano-soft-assembly/svarner/ASE-blues/128H2O/revPBE-2/prod.traj'
file2 = '/lcrc/project/nano-soft-assembly/svarner/ASE-blues/128H2O/revPBE-2/2/prod.traj'

traj1 = Trajectory(file1)
traj2 = Trajectory(file2)

traj = Trajectory('train.traj', 'w')

for atoms in traj1[::25]:
    traj.write(atoms)
for atoms in traj2[::25]:
    traj.write(atoms)

print(len(traj))
traj.close()
