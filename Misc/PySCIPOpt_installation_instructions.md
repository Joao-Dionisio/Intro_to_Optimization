# PySCIPOpt installation instructions

## Using Anaconda

- Install Anaconda (Windows): https://docs.anaconda.com/anaconda/install/windows/ (Download an run the setup executable)
- Create new conda environment: https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands 
    - On command line type: conda create --name myenv      (myenv is a name of your choosing, e.g. pyscipopt)
- Activate the new environmet
    - Activate environment: conda activate myenv      (or conda activate pyscipopt) 
- Install PySCIPOpt: https://pypi.org/project/PySCIPOpt/
    - On command line type: conda install --channel conda-forge pyscipopt


## Activate PySCIPOpt with VSCode

- On VSCode, press "Ctrl+Shift+P"
- Type "Python: Select Interpreter"
- Choose the Anaconda environment you created (E.g. Python 3.x ('pyscipopt'))


Should be all ready to go :)