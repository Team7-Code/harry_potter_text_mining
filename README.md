# harry_potter_text_mining

###### Short description: 
Our project deals with understanding the characters of a book and then visualize the finding in a comprehensible manner to convey the entity relationships. Thus, giving us the power to analyze and understand the contents of a book to greater depths.
The aforementioned outcomes are planned to be achieved through Text Mining on a particular novel or book in order to extract the different characters and their importance with respect to each other. For visualization and some graph level analysis we would be focusing on Subgraph Mining and Network Analysis on the obtained data for a deeper insight into the characters’ popularity, how does it change over the time and the factors that may be affecting it.

###### Mining topic: 
Text Mining and Subgraph Analysis

###### Dataset Characteristics:
We would be using the Harry Potter book series for our initial data mining process. The text data, once tokenized by each sentence had around 3500 to 8000 rows.

###### Data Preparation:
We collected our data from two different sources for which the processing was done in KNIME – 
* Data Extraction – using text files and Potter API for sourcing the data
* Data Processing – KNIME to tokenize files, convert to documents data type and removal of any trailing spaces
* Data Transformation – using Stemmers and Lemmatizers  along with Stop Words for filtering out the data which do not add any value to our text analysis
* Data Enrichment – using Stanford NLP tagger to tag Person, Location and Organizations in the text. Since the taggers weren’t identifying all the desired characters, we have used a Dictionary Tagger for tagging some of the commonly missed entities by the tagger.
* Bag of Words – the main target for all the preparation was to create a Bag of Words which contains all the tagged characters

###### Methodology: 
The methodology used in our project is broken into three parts where the analysis and processing was done on 3 different platforms –
* KNIME Workflows – We use this for the following tasks and analysis – 
	* Processing the text file and using text enrichment to obtain the tags
	* Using the tags identified we created a bag of words which are filtered for Person, Location and Organizations to create the Tag Cloud visualization and proceed with further analysis
	* Feeding the tags to Apriori Analysis to create 2-item sets with a minimum support value of 3
	* The item sets of size 2 identified by the above analysis were sourced into the Graph analysis
	* A separate workflow was created for addressing different observations which we wanted to capture
		* Network analysis for identifying relationships between entities
		* An analysis was done to obtain sub-graphs and hierarchical clustering
* Python Codes – Following are the tasks that were carried out in python – 
	* Using the output from Apriori analysis to create nodes and undirected edges with item support value as the weight on those edges
	* Using NetworkX to create and analyze graphs for finding the Neighbors, Cliques and Betweenness Centrality to determine the highly related nodes, close-knit communities(cliques) and the popularity of a character respectively
	* Using graph visualization in NetworkX to visualize the following – 
		* Neighborhood Plots for analyzing the closest connected nodes
		* Maximal Cliques identification
		* Relationships among the protagonists to see how their relationship progressed throughout the series

###### Repo Description:
1. KNIME Workflows - This contains the workflows designed for mining the textual data in KNIME
1. KNIME Processed - This contains the output from workflows which are then processed in python
1. Python Scripts - This contains the scripts for graph analysis using NetworkX libraries
1. Plots - visualizations
1. Relationship plots - more visualizations
