# Open Docs #

I am doing a Documentation of the Files of "pytorch_geometric" repository.This is the part of my Task-06 in amfoss pravashan 2024.


# pytorch_geometric #

## Setup Instructions ##

### 1 Clone the Repository: ###

\'''
git clone https://github.com/pyg-team/pytorch_geometric.git
\'''
After doing this,The repository is cloned into your system. 
\'''
cd pytorch_geometric
\'''

### 2 Prerequisites ###
You system consists of Python from 3.8 to 3.12 any of them is ok. And you should also install the PyTorch on your system.
You can verify your PyTorch installation with:
\'''
python -c "import torch; print(torch.__version__)"
\'''

### 3 Installation Methods ###
You can install PyG directly using pip: 
\'''
pip install torch_geometric
\'''

### 4 Optional Libraries ###
You should want some Optional Libraries such as torch_scatter, torch_sparse, torch_cluster, and torch_spline_conv:
\'''
pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-${TORCH}+${CUDA}.html
\'''
Replace ${TORCH} and ${CUDA} with your specific versions of PyTorch and CUDA​((PyTorch Geometric).


You can also install this from the source.


## This is how you can set up pytorch_geometric in your system. ##
