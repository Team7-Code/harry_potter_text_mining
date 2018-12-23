import pandas as pd
import networkx as nx
import numpy as np

# needs to be changed in order to process the files
dir = "02 KNIME Processed\\python_processed"


# Read all the books
books_list = []
for path in glob.glob("02 KNIME Processed\\python_processed\\book*.csv"):
    books_list.append(path)

G_book1 = nx.Graph()

books = []

# Create graphs from all the books and store into a list
for book_name in books_list:
    book = pd.read_csv(book_name)
    G_book = nx.Graph()
    for _, edge in book.iterrows():
        G_book.add_edge(edge['node1'], edge['node2'], weight=edge['weight'])
    books.append(G_book)


# degree centrality
graphs = books
deg_central = []
for i in graphs:
    x = nx.degree_centrality(i)
    x = sorted(x.items(), key=lambda x: x[1], reverse=True)
    deg_central.append(x)
centrality = np.array(deg_central)

print(centrality[0][:10])
top_10_chars = []
for i in range(len(graphs)):
    top_10_chars.append(centrality[i][:10])

print(top_10_chars)
x = np.array(range(1,8))
y = []
z = []
for i in range(0,7):
    for j in range(0,10):
        y.append(top_10_chars[i][j][0])
        z.append(top_10_chars[i][j][1])
y = np.array(y)
print(y.shape)
y = y.reshape(7, 10)
z = np.array(z)
z = z.reshape(7, 10)
import matplotlib.pyplot as plt
import pandas as pd

y_df = pd.DataFrame(y)
z_df = pd.DataFrame(z)

#output needs to be specified as well
y_df.to_csv("02 KNIME Processed/python_processed/y_df.csv")
z_df.to_csv("02 KNIME Processed/python_processed/z_df.csv")

#####################################################################
