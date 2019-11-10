## Repository of AutoML benchmark in kaggle datasets

## Run experiments

Install anaconda in: https://www.anaconda.com/distribution/#download-section

Install git (Debian based):

`sudo apt install git`

Install git (Arch based):

`pacman -S git`


Clone this repository:

`git clone https://github.com/Sette/automl-notebooks-benchmark`

`cd automl-notebooks-benchmark`

Create conda env:

`conda env create -f automl.yml`

This env contains:
- auto-sklearn==0.5.2
- autokeras==0.4.0
- h2o==3.26.0.5
- hpsklearn==0.1.0
- tpot==0.10.2

Run experiments:

`jupyter notebook`

