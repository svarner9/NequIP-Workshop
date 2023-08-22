# nequip-examples
A tutorial with examples of how to train and use the Allegro (NequIP) machine learning force field.

## Program installation
We will be using conda to install the necessary python packages that will be used in conjunction with the Allegro (NequIP) machine learning force field. Install conda now if you do not have it already.

### Conda Packages
Once you have installed conda, make a clean conda environment for Nequip to sit in:
```
conda create -n nequip
conda activate nequip
```
Install ASE which will be needed for many things in the tutorial:
```
conda install -c conda-forge ase
```
Install the CUDA-capable version of PyTorch. Note that at the time of making this tutorial, NequIP works well with version 1.11.0, however, check the [NequIP github page](https://github.com/mir-group/nequip) for the latest version that is recommended. You can obtain the appropriate Conda command from the [PyTorch website]
```
conda install pytorch=1.11.0 pytorch-cuda=11.8 -c pytorch -c nvidia
```
Note that you don't need torchvision or torchaudio, so you can skip those if you want.


### Nequip
You can find instructions for installing Nequip at the [NequIP github page](https://github.com/mir-group/nequip). After following the steps above, you are now ready to install NequIP:
```
pip install nequip
```

### Allegro
Allegro is the newest most advanced architecture provided for NequIP, and you must install in in addition NequIP itself. Thankfully, this is also very easy to do. Instructions can be found at the [Allegro github page](https://github.com/mir-group/allegro).

Once you have installed NequIP as above, you can install Allegro by running the following:
```
git clone --depth 1 https://github.com/mir-group/allegro.git
cd allegro
pip install .
```
### Finish
You are now all set to train Allegro machine learned potentials and use them in MD simulations. The rest of this tutorial will walk you through how to do this.

## Running the example
The example walks you through how to train, test, and use a machine learned potential (MLP) for a simple system of water molecules. The steps, and the order you want to do them in are as follows:
1. Process your training data
2. Bencharm the MLP (optional)
3. Train the MLP
4. Evaluate the MLP
5. Use the MLP in MD simulations

You will find in-depth examples of how to do each of these in the ```water``` folder.
