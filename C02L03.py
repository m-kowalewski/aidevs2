from base import get_token, get_task, send_answer, openai_embedding


task_name = "embedding"

token = get_token(task_name)
task = get_task(token)
print(task)
text = "Hawaiian pizza"
embeddings = openai_embedding(text)
print(embeddings)
print(len(embeddings))
send_answer(embeddings, token)
