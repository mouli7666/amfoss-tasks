# Open Docs 

I am doing a Documentation of the Files of "pytorch_geometric" repository.This is the part of my Task-06 in amfoss pravashan 2024.


# pytorch_geometric 

## Setup Instructions


1.**Clone the Repository:**

   ```bash
   git clone https://github.com/pyg-team/pytorch_geometric.git
   cd pytorch_geometric

After doing this,The repository is cloned into your system. 



2.**Prerequisites:**
-You system consists of Python from 3.8 to 3.12 any of them is ok. And you should also install the PyTorch on your system.
-You can verify your PyTorch installation with:
   ```bash
   python -c "import torch; print(torch.__version__)"


3.**Installation Methods:**
-You can install PyG directly using pip: 
   ```bash
   pip install torch_geometric


4.**Optional Libraries:**
-You should want some Optional Libraries such as torch_scatter, torch_sparse, torch_cluster, and torch_spline_conv:
   ```bash
   pip install pyg_lib torch_scatter torch_sparse torch_cluster torch_spline_conv -f https://data.pyg.org/whl/torch-${TORCH}+${CUDA}.html

Replace ${TORCH} and ${CUDA} with your specific versions of PyTorch and CUDA​((PyTorch Geometric).


You can also install this from the source.


## Contribution Guidelines 
-Reporting Issues: Please report any issues or bugs using the GitHub Issues tab.
-Submitting Pull Requests: Fork the repository, make your changes, and submit a pull request with a description of your changes.

