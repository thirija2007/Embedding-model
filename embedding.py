from sentence_transformers import SentenceTransformer


# 1. Load the embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding model loaded successfully.")


# 2. Input text
sentences = [
    "I enjoy coding in Python.",
    "I love programming in Python.",
    "I am learning artificial intelligence.",
    "Machine learning is interesting.",
    "I like creating AI projects."
]


# 3. Convert text into numerical embeddings
embeddings = model.encode(sentences)


# 4. Display the numerical embeddings
for i, sentence in enumerate(sentences):

    print("\nSentence:", sentence)

    print("Numerical Embedding:")
    print(embeddings[i])

    print("Number of dimensions:", len(embeddings[i]))


print("\nText has been successfully converted into numerical vectors.")
