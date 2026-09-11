def search_similar(collection_name, query_vector, limit=5):
    return client.search(
        collection_name=collection_name,
        query_vector=query_vector,
        limit=limit
    )
