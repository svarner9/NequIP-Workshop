# Train
Once the data has been processed, you are ready to train. The model setup is done in the [train.yaml](./train.yaml) file. This file contains all of the information needed to train the model, including the location of the data, the model architecture, and the training parameters. The file is commented to explain what each parameter does. You can also find more information about each parameter in the [NequIP documentation](https://nequip.readthedocs.io/en/latest/).

The provided training file is an edited version of the template provided in the Allegro documentation.

Once you have edited the training file to your liking, you can start training by running the following command:
```
sbatch train.sh
```
Note that you will have to edit the Slurm sbatch file to match your system and account.

If you are not using Slurm, then you can just run the following command:
```
conda activate nequip
nequip-train train.yaml
```

The results of the training are stored in the [results folder](../results/). You can train lots of different models and all results will be stored there under the model name provided in the training file.