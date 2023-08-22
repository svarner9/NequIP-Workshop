# Benchmark
You can benchmark the speed of the MLP at [../train/train.yaml](../train/train.yaml) by running the following command:
```
sbatch benchmark.sh
```
If you are not using Slurm, then you can just run the following command:
```
conda activate nequip
nequip-benchmark ../train/train.yaml
```

Note that you can benchmark the model before you even train it, which is helpful if you want to see how fast it will be before spending resources to train.

You can see additional options for the benchmark command by running:
```
nequip-benchmark --help
```
