#!/bin/bash
#SBATCH --job-name=example
#SBATCH -p gpu
##SBATCH -N 1
#SBATCH --gres=gpu:1
#SBATCH -t 1-0
#SBATCH -A nano-soft-assembly
##SBATCH --mail-user=svarner@anl.gov
##SBATCH --mail-type=ALL
#SBATCH -o Report-%j.out

module purge
module load cuda

nequip-train train.yaml