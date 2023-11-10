from base import get_token, get_task, send_answer, openai_moderation


task_name = "moderation"

token = get_token(task_name)
task = get_task(token)
result = []
for text in task['input']:
    print("TEXT", text)
    response = openai_moderation(text)
    print("RESPONSE", response)
    result.append(int(response["results"][0]["flagged"]))
    print("RESULT", result)
send_answer(result, token)
