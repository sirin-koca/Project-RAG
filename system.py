import graphviz

# Create the graph
graph = graphviz.Digraph(format='png')

# Define system components with box style
graph.attr('node', shape='box', style='rounded,filled', color='lightblue', fontname='Helvetica', fontsize='10')

# Add nodes to the graph
graph.node('UI', 'User Interface (UI)\nUser interacts with the chatbot.')
graph.node('EmbedQ', 'Embedding Model (Query)\nEmbeds the user query into vectors.')
graph.node('Retriever', 'Retriever Module\nFinds relevant document embeddings.')
graph.node('EmbedD', 'Embedding Model (Documents)\nConverts documents into vector embeddings.')
graph.node('VectorDB', 'Vector Database (FAISS/Chroma)\nStores and retrieves document embeddings.')
graph.node('LLM', 'LLM (Mistral7B)\nGenerates a response using retrieved data.')
graph.node('Response', 'Response Generation\nCombines retrieved data and LLM output.')
graph.node('Feedback', 'Feedback Loop\nMonitors performance, accuracy, and hallucination rate.')

# Define the flow between components
graph.edge('UI', 'EmbedQ', label='User submits query')
graph.edge('EmbedQ', 'Retriever', label='Query converted to vector')
graph.edge('Retriever', 'VectorDB', label='Fetches relevant document vectors')
graph.edge('VectorDB', 'Retriever')
graph.edge('Retriever', 'LLM', label='Passes relevant data')
graph.edge('LLM', 'Response', label='LLM generates response')
graph.edge('EmbedD', 'VectorDB', label='Documents embedded and stored')
graph.edge('Response', 'UI', label='Returns response to user')
graph.edge('Response', 'Feedback', label='Tracks performance')

# Render the diagram and save as PNG
graph.render('NAVATAR_helper_RAG_Architecture', view=True)
