# Water
This folder contains a tutorial with in-depth instructions on how to train, validate,and use a machine learned potential (MLP) for a simple system of water molecules. Each of the necessary steps have their own folder, and they should be read (and run) in the following order:
1. [Process your training data](./process)
2. [Benchmark the MLP (optional)](./benchmark)
3. [Train the MLP](./train)
4. [Evaluate the MLP](./evaluate)
5. [Use the MLP in MD simulations](./md)

During training, you also have the option to track the learning curves, which is done with the analysis code at [./results/analyze.ipynb](./analysis). This is not necessary, but it can be useful to see how the training is progressing, especially when comparing different models.