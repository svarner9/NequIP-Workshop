#!/bin/bash
#SBATCH --job-name=benchmark
#SBATCH -p gpu
##SBATCH -N 1
#SBATCH --gres=gpu:1
#SBATCH -t 20
#SBATCH -A nano-soft-assembly
##SBATCH --mail-user=svarner@anl.gov
##SBATCH --mail-type=ALL
##SBATCH -o Report-%j.out

module load cuda

nequip-benchmark ../train/train.yaml