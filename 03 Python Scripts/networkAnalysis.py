import glob
from heapq import nlargest

import matplotlib.pyplot as plt
import networkx as nx
import nxviz as nv
import pandas as pd
import os

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

deg_cent_all_book = [nlargest(5, G_book1, key=nx.degree_centrality(G_book1).get) for g in books]


# Explore the graphs
deg_cent = [nx.degree_centrality(g) for g in books]
deg_cent = pd.DataFrame.from_records(deg_cent)

bw_cent = [nx.betweenness_centrality(g) for g in books]
bw_cent = pd.DataFrame.from_records(bw_cent)

try:
    nx.average_shortest_path_length(books[5])
except:
    print('Cant find shortest path. Graph is not connected.')

nx.dijkstra_path(books[0], source="HARRY", target="HERMIONE")


# Analyzing cliques
clique_path = '04 Plots\\cliques\\'

if not os.path.exists(clique_path):
    os.mkdir(clique_path)

largest_clique_all_books = [sorted(nx.find_cliques(book), key=lambda x:len(x))[-1] for book in books]
for _, clique in enumerate(largest_clique_all_books):
    g = books[_].subgraph(largest_clique_all_books[_])
    nx.draw_shell(g, with_labels=True)
    plt.savefig(clique_path + str(_) + ".jpg")
    plt.clf()
print("Clique graphs saved in ", clique_path)


# Analyzing the neighbors
plot_dir = '04 Plots\\neighbour_plots\\'
if not os.path.exists(plot_dir):
    os.mkdir(plot_dir)

person = ['DUMBLEDORE', 'SNAPE', 'RON', 'HERMIONE', 'NEVILLE'] #Checking out important people
for _ in range(1,8):
    for n in person:
        try:
            g = books[_-1].subgraph(books[_-1].neighbors(n))
        except:
            print("Exception: The node ",n+" is not in graph ", _)
            continue
        nx.draw_shell(g, with_labels=True)
        # plt.show()
        plt.savefig(plot_dir + n + "'s neighbors in book " + str(_))
        plt.clf()
        plt.close()
print("Neighbor plots saved in ", plot_dir)

# Analyzing the relationship between main protagonists
harry_ron_hermione_df = pd.DataFrame(columns=['book', 'node1', 'node2', 'weight'])


for _, book_path in enumerate(glob.glob("02 KNIME Processed/python_processed/book*.csv")):
    book = pd.read_csv(book_path, header='infer', index_col= False)
    index = book.loc[(book['node1'].isin(['HARRY','HERMIONE'])) & book['node2'].isin(['HARRY','HERMIONE'])].index[0]
    harry_ron_hermione_df= harry_ron_hermione_df.append({'book':_, 'node1':book.iloc[index]['node1'], 'node2':book.iloc[index]['node2'], 'weight':book.iloc[index]['weight']}, ignore_index=True)

    index = book.loc[(book['node1'].isin(['RON', 'HERMIONE'])) & book['node2'].isin(['RON', 'HERMIONE'])].index[0]
    harry_ron_hermione_df = harry_ron_hermione_df.append(
        {'book': _, 'node1': book.iloc[index]['node1'], 'node2': book.iloc[index]['node2'],
         'weight': book.iloc[index]['weight']}, ignore_index=True)

    index = book.loc[(book['node1'].isin(['RON', 'HARRY'])) & book['node2'].isin(['RON', 'HARRY'])].index[0]
    harry_ron_hermione_df = harry_ron_hermione_df.append(
        {'book': _, 'node1': book.iloc[index]['node1'], 'node2': book.iloc[index]['node2'],
         'weight': book.iloc[index]['weight']}, ignore_index=True)

harry_ron_hermione_df['characters'] = harry_ron_hermione_df['node1']+" & " + harry_ron_hermione_df['node2']
harry_ron_hermione_df.drop(['node1', 'node2'], axis=1)
harry_ron_hermione_df["book"] = [int(x) + 1 for x in harry_ron_hermione_df["book"]]
harry_ron_hermione_df.groupby(['book', 'characters']).sum()['weight'].unstack().plot(use_index=True)
plt.savefig("04 Plots\\harry_hermione_ron.jpg")
plt.clf()
