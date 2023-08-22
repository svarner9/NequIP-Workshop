# Process
Before training, we must process the data into ```extxyz``` format, which is the most easily read format by NequIP. If you trajectory is already in ASE's ```traj``` format, then this is very easy to do as shown in [traj_to_xyz.py](./traj_to_xyz.py).

The trajectory [train.traj](./train.traj) contains 560 frames of 128 water molecules in a cubic box with periodic boundary conditions. The frames are from AIMD simulations in CP2K using the revPBE XC-functional with D3 dispersion corrections. The TZV2P basis set was used with GTH pseudopotentials. An energy cutoff of 380 Ry was used, and an SCF tolerance of 1e-5. The simulations were run at 300 K with a timestep of 1.0 fs. The frames in the training trajectory are 250 fs apart.

You can process the data into the proper format by running the following command:
```
python traj_to_xyz.py
```
