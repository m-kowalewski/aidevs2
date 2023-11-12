from base import  download_json_from_url, qdrant_client, QdrantDataClass, qdrant_create_collection
from qdrant_client.http.models import Batch

collection_name = "C03L04"
qdrant = qdrant_client()
qdrant_create_collection(collection_name, qdrant)

try:
    indexed = qdrant.get_collection(collection_name=collection_name)
except:
    print("Could not get collection.")

task_name = "search"
data_url = "https://unknow.news/archiwum.json"

data_json = download_json_from_url(data_url)
if not data_json:
    quit()
print("Start saving...")
for index, article in enumerate(data_json):
    if index > 300:
        print("Finished")
        quit()
    qdrant_data = QdrantDataClass(collection_name=collection_name, content=article)
    qdrant.upsert(
        collection_name=collection_name,
        points=Batch(
            ids=[qdrant_data.id],
            vectors=[qdrant_data.vector],
            payloads=[qdrant_data.payload],
        )
    )
    print("Saved element number: {} and id: {}".format(index, qdrant_data.id))
print("Finished")