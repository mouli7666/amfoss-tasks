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


## Describing what each module does

