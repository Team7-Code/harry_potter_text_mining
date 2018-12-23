import pandas as pd
import glob

fname_file = pd.read_csv("02 KNIME Processed/names-houses.csv")
fname_file['Names'] = fname_file['Names'].str.upper()
fname_file['House'] = fname_file['House'].str.upper()
fname_file.head()


# To remove self loops
for book_path in glob.glob("02 KNIME Processed/python_processed/book*.csv"):
    book = pd.read_csv(book_path, header='infer')
    book.head()
    book["merge1"] = book["node1"] + ' ' + book["node2"]
    book["merge2"] = book["node2"] + ' ' + book["node1"]

    book["compare1"] = [x in fname_file["Names"].values for x in book["merge1"].values]
    book["compare2"] = [x in fname_file["Names"].values for x in book["merge2"].values]
    book = book[book["compare1"].values | book["compare2"].values == False]

    book = book.drop(['merge1', 'merge2', 'compare1', 'compare2'], axis=1)

    book.to_csv(book_path)




