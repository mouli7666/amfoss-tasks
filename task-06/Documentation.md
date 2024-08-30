# Documentation for pytorch_geometric

# Overview
  
  pytorch_geometric repository which is a popular open source library built on pyTorch. It is especially built for the designed for the deep learning of irregular data structures like graphs and point clouds it is mainly used by the researchers, students, scholars etc.

## Features
-**`Data Handling`** It is very much useful for handling and processing graph data, including loading data from popular graph datasets.
-**`Models and Tasks`** It has pre built models and utilities for common tasks like node classification, link prediction, and graph classification.
-**`Performance`** Efficient CPU and GPU operations for large-scale graph data using PyTorch’s tensor-based computations.
-**`Integration with PyTorch Ecosystem`** By Integration with PyTorch Ecosystem you can use pyTorch's deep learning experiences.

## Purpose
-Enables the implementation of Graph Neural Networks (GNNs) on irregular structures such as graphs, point clouds, and manifolds.
-visualizing graphs and tracking experiments.
-It simplifies working with graph data and performing tasks

## Documentation of the code

-**Train your own GNN model**
  ```bash
  import torch
  from torch import Tensor
  from torch_geometric.nn import GCNConv
  from torch_geometric.datasets import Planetoid

  dataset = Planetoid(root='.', name='Cora')

  class GCN(torch.nn.Module):
      def __init__(self, in_channels, hidden_channels, out_channels):
          super().__init__()
          self.conv1 = GCNConv(in_channels, hidden_channels)
          self.conv2 = GCNConv(hidden_channels, out_channels)

      def forward(self, x: Tensor, edge_index: Tensor) -> Tensor:
          # x: Node feature matrix of shape [num_nodes, in_channels]
          # edge_index: Graph connectivity matrix of shape [2, num_edges]
          x = self.conv1(x, edge_index).relu()
          x = self.conv2(x, edge_index)
          return x

  model = GCN(dataset.num_features, 16, dataset.num_classes)
  ``` 
-**Create your own GNN layer**
  ```bash
  import torch
  from torch import Tensor
  from torch.nn import Sequential, Linear, ReLU
  from torch_geometric.nn import MessagePassing

  class EdgeConv(MessagePassing):
      def __init__(self, in_channels, out_channels):
          super().__init__(aggr="max")  # "Max" aggregation.
          self.mlp = Sequential(
              Linear(2 * in_channels, out_channels),
              ReLU(),
              Linear(out_channels, out_channels),
          )

      def forward(self, x: Tensor, edge_index: Tensor) -> Tensor:
          # x: Node feature matrix of shape [num_nodes, in_channels]
          # edge_index: Graph connectivity matrix of shape [2, num_edges]
          return self.propagate(edge_index, x=x)  # shape [num_nodes, out_channels]
  
      def message(self, x_j: Tensor, x_i: Tensor) -> Tensor:
          # x_j: Source node features of shape [num_edges, in_channels]
          # x_i: Target node features of shape [num_edges, in_channels]
          edge_features = torch.cat([x_i, x_j - x_i], dim=-1)
          return self.mlp(edge_features)  # shape [num_edges, out_channels]
   ```

## Functioning of each module


1.### torch_geometric.data ###
-**`Purpose`**: Handles data structures and loading for graph data.
-**`Key Classes`**:
    - `Data`: A data object holding a single graph with attributes like node features, edge indices, labels, etc.
    - `Dataset`: An abstract class for creating graph datasets, handling downloading, processing, and access.
    - `DataLoader`: A DataLoader tailored for handling batches of graph data, supporting mini-batching.


2.### torch_geometric.nn ###
-**`Purpose`**: Implements a wide range of neural network layers and models specifically designed for graph data.
-**`Key Components`**:
    -`Convolutional Layers`
    -`Aggregation Operators`
    -`Normalization Layers`
    -`Pooling Layers`
    -`Unpooling Layers`
    -`Models`
    -`KGE Models`
    -`Encodings`

- This are the key components of module torch_geometric.nn.


3.### torch_geometric.transforms ###
-**`Purpose`**: Provides a set of transformation functions to modify and augment graph data, similar to data augmentation in computer vision.
-**`Key Transformations`**:
    -**`BaseTransform`** An abstract base class for writing transforms.
    -**`Center`** Centers node positions pos around the origin.
    -**`NormalizeRotation`** Rotates all points according to the eigenvectors of the point cloud.
    -**`NormalizeScale`** Centers and normalizes node positions to the interval .


4.### torch_geometric.utils ###
-**`Purpose`**: Utility functions for solving common operations on graph data.
-**`Key Utilities`**:
    -**`scatter`** 
    -**`cumsum`** Returns the cumulative sum of elements of x .
    -**`degree`** 
    -**`softmax`** Computes a sparsely evaluated softmax.



5.### torch_geometric.loader ###
-**`Purpose`**: It provides a software application where that moves data into a system for specific graph types etc.
-**`key Loaders`**:
    -**`Dataset`** The dataset from which to load the data.
    -**`batch_size`** It tells about how many samples per batch to load
    -**`shuffle`** If it is set to true then the data will be reshuffled at every epoch.
    -**`follow_batch`** Creates assignment batch vectors for each key in the list.



## implementation of Key Functions

1.### torch_geometric.data
-**` Implementation `**: This torch_geometric.data handles various graph data structures, providing an easy way to store and manipulate graph information.

2.### torch_geometric.nn
-**` Implementation `**: Implements the graph attention mechanism.

3.### torch_geometric.transforms 
-**` Implementation `**: Adjusts the edge_index tensor to include edges where each node connects to itself.

4.### torch_geometric.utils
-**` Implementation `**: Performs reduction operations (like sum, mean, max) on node features.

5.### torch_geometric.loader
-**` Implementation `**: Handles efficient mini-batching of multiple graphs.



## Uses


### 1.Graph Neural Network (GNN) Development
- PyG provides pre-implemented layers for various GNN architectures, such as Graph Convolutional Networks (GCN), Graph Attention Networks (GAT), GraphSAGE, and more. These layers simplify the process of building complex GNN models for tasks like node classification, link prediction, and graph classification.


### 2.Data Handling and Transformation
- It offers efficient data structures (Data, Batch, etc.) for representing graphs, and provides utilities for loading and processing popular graph datasets. This makes it easy to work with graph data of various types, including large-scale graphs, dynamic graphs, and heterogeneous graphs.

- PyG includes numerous data transformation tools that allow you to manipulate and prepare graph data for training, such as normalizing features, adding self-loops, and converting graphs between different formats.


### 3.Scalability
- PyTorch Geometric supports scaling GNNs to large graphs using techniques like neighbor sampling, graph partitioning, and mini-batch training. This enables users to train models on massive graphs that would otherwise be infeasible with traditional approaches.


### 4.Extensive Dataset Support
- PyG offers direct access to a wide range of graph datasets through its dataset module, including popular benchmarks like Cora, PubMed, and larger datasets from the TU Dortmund University repository. It also supports custom dataset loading and processing.


### 5.Support for Advanced GNN Variants
- Beyond basic GNN layers, PyG includes support for advanced variants like message passing neural networks (MPNNs), spectral methods, spatial methods, and beyond. This breadth allows users to apply the most suitable GNN variant to their specific problem.


### 6.Integration with PyTorch Ecosystem
- It integrates seamlessly with other PyTorch libraries and tools, such as PyTorch Lightning for training and PyTorch’s ecosystem of datasets, making it easy to plug into existing PyTorch workflows.
