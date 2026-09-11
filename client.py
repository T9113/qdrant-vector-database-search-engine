from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

client = QdrantClient("http://localhost:6333")

def init_collection(name="documents"):
    client.recreate_collection(
        collection_name=name,
        vectors_config=VectorParams(size=1536, distance=Distance.COSINE),
    )
    print(f"Collection {name} initialized.")

if __name__ == "__main__":
    init_collection()
