from base import get_token, get_task, send_answer, openai_embedding, qdrant_client, qdrant_search


task_name = "search"

token = get_token(task_name)
task = get_task(token)
print(task)
embedding = openai_embedding(task['question'])
print(embedding)
query_result = qdrant_search(qdrant_client(), "C03L04", embedding)
result = query_result[0].payload['content']['url']
send_answer(result, token)
