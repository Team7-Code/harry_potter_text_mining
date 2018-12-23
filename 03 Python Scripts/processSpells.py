import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt


spells_file = '02 KNIME Processed\\spell_occurence.csv'
df = pd.read_csv(spells_file)
df2 = pd.DataFrame()
df2[['Book', 'Spell', 'Count']] = df[['Preprocessed Document','Term as String', 'TF abs']]
df2[['Book']] = [os.path.basename(n[1][0]) for n in df2.iterrows()]

df2[['Book']] = df2[['Book']].replace("harry potter sorcerers stonetxt", 1)
df2[['Book']] = df2[['Book']].replace("harry potter chamber secretstxt", 2)
df2[['Book']] = df2[['Book']].replace("harry potter prisoner azkabantxt", 3)
df2[['Book']] = df2[['Book']].replace("harry potter goblet firetxt", 4)
df2[['Book']] = df2[['Book']].replace("harry potter phoenixtxt", 5)
df2[['Book']] = df2[['Book']].replace("harry potter blood princetxt", 6)
df2[['Book']] = df2[['Book']].replace("harry potter deathly hollowstxt", 7)
df2.to_csv("02 KNIME Processed\\python_processed\\spell_list_by_book.csv")


# Plotting Spells
plot_dir = '04 Plots\\'

imp_spells = df2.groupby('Spell').sum()['Count']
famous_spells = imp_spells.index[imp_spells>=20]
least_used_spells = imp_spells.index

df2_famous_spell = df2[df2['Spell'].isin(famous_spells)]

df2_famous_spell.groupby(['Book', 'Spell']).sum()['Count'].unstack().plot(use_index=True)
plt.savefig(plot_dir+"spells.jpg")
plt.clf()
print("Spells plot saved in", plot_dir)

