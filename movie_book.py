import networkx as nx
import matplotlib.pyplot as plt

def create_graph(users, movies, user_movie_edges, user_user_edges):
    G = nx.Graph()
    G.add_nodes_from(users, bipartite=0)  # 0 for users
    G.add_nodes_from(movies, bipartite=1)  # 1 for movies/books
    G.add_edges_from(user_movie_edges)
    G.add_edges_from(user_user_edges)
    return G

def recommend_for_user(user, graph):
    friends = [n for n in graph.neighbors(user) if graph.nodes[n]['bipartite'] == 0]
    recommended_movies = set()
    user_movies = set([n for n in graph.neighbors(user) if graph.nodes[n]['bipartite'] == 1])
    for friend in friends:
        friend_movies = set([n for n in graph.neighbors(friend) if graph.nodes[n]['bipartite'] == 1])
        recommended_movies.update(friend_movies - user_movies)
    return recommended_movies

def evaluate_recommendation_system(graph, ground_truth):
    precision_vals = []
    recall_vals = []

    for user in users:
        if user not in ground_truth:
            continue

        recommended = recommend_for_user(user, graph)
        true_positive = recommended & ground_truth[user]
        
        precision = len(true_positive) / len(recommended) if recommended else 0
        recall = len(true_positive) / len(ground_truth[user])
        
        precision_vals.append(precision)
        recall_vals.append(recall)

        # Print stats
        print(f"User: {user}")
        print(f"Recommended Movies/Books: {recommended}")
        print(f"Precision for {user}: {precision}")
        print(f"Recall for {user}: {recall}\n")

    avg_precision = sum(precision_vals) / len(precision_vals)
    avg_recall = sum(recall_vals) / len(recall_vals)
    return avg_precision, avg_recall

def draw_graph(graph, user=None):
    pos = nx.bipartite_layout(graph, nodes=users, align='horizontal')
    if user:
        recommended_movies = recommend_for_user(user, graph)
        node_colors = [('yellow' if n == user else 'green' if n in recommended_movies else 'lightgray') for n in graph.nodes()]
    else:
        node_colors = ['green' if graph.nodes[n]['bipartite'] == 0 else 'lightgray' for n in graph.nodes()]
    nx.draw(graph, pos, with_labels=True, node_color=node_colors, node_size=1500, font_size=12)
    plt.show()

# Expanded sample data:
users = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"]
movies = ["Movie1", "Movie2", "Movie3", "Movie4", "Movie5", "Movie6"]
user_movie_edges = [
    ("Alice", "Movie1"), 
    ("Alice", "Movie2"), 
    ("Bob", "Movie1"), 
    ("Charlie", "Movie3"),
    ("David", "Movie4"),
    ("Eve", "Movie5"),
    ("Frank", "Movie6"),
    ("Frank", "Movie4")
]
user_user_edges = [
    ("Alice", "Bob"), 
    ("Bob", "Charlie"), 
    ("Charlie", "David"), 
    ("David", "Eve"),
    ("Eve", "Frank"),
    ("Frank", "Alice")
]

ground_truth = {
    "Alice": {"Movie3", "Movie4"},
    "Bob": {"Movie2", "Movie5"},
    "Charlie": {"Movie1", "Movie6"},
    "David": {"Movie2"},
    "Eve": {"Movie3"},
    "Frank": {"Movie1", "Movie5"}
}

# Execute
G = create_graph(users, movies, user_movie_edges, user_user_edges)
precision, recall = evaluate_recommendation_system(G, ground_truth)
print(f"Overall Precision: {precision}, Overall Recall: {recall}")

# Drawing the graph (Uncomment as required)
draw_graph(G)  # Draw the graph without any highlights
draw_graph(G, user="Alice")  # Highlight Alice's recommendations