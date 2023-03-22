# -*- coding: utf-8 -*-
"""network_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11-HiNtdsVoNOOMdEhtEomeImKKjpiYS3
"""

import pandas as pd
import networkx as nx
import io
import matplotlib.pyplot as plt
import heapq


# Load the CSV file into a Pandas DataFrame
with open('influencers_data.csv', 'r', encoding='utf-8', errors='ignore') as file:
    lines = file.readlines()

# Remove the problematic row and join the remaining lines
lines = lines[:6861]
data = ''.join(lines)

# Create the DataFrame
df = pd.read_csv(io.StringIO(data))

import random
random.seed(123)  # set the seed to a fixed value

# Create a new graph
G = nx.Graph()
df['media_type'] = df['media_type'].fillna('unknown')

# Loop through each row in the DataFrame and add an edge for each pair of nodes
for index, row in df.iterrows():
    node1 = row['name']
    node2 = row['media_type']
    G.add_edge(node1, node2, weight=float(row['followers']))


# Draw the graph using a spring layout
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)

fig = plt.figure(figsize=(50,10))
# Show the graph
plt.show()
print(list(G.nodes()))
print(df['media_type'].unique())

import heapq

def dijkstra(graph, start, end):
    dist = {node: float('inf') for node in graph.nodes}
    dist[start] = 0
    pq = [(0, start)]
    prev = {node: None for node in graph.nodes}

    while pq:
        current_dist, current_node = heapq.heappop(pq)
        if current_node == end:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = prev[current_node]
            return path[::-1]

        if current_dist > dist[current_node]:
            continue

        for neighbor, edge in graph[current_node].items():
          distance = current_dist + edge['weight']
          #print(f'distance: {distance}, current_node: {current_node}, neighbor: {neighbor}, edge: {edge}')
          if distance < dist[neighbor]:
              dist[neighbor] = distance
              prev[neighbor] = current_node
              heapq.heappush(pq, (distance, neighbor))


    return None


print(dijkstra(G, 'Jonathan Wolfer', 'Karen Gross'))