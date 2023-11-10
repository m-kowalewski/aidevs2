from base import get_token, get_task, send_answer, openai_create, download_txt_from_url


task_name = "scraper"

token = get_token(task_name)
task = get_task(token)
print(task)
msg = task['msg']
url = task['input']
question = task['question']
system_template = msg + "\n ### \n" + download_txt_from_url(url)
human_template = question
if not human_template:
    quit()
response = openai_create(system_template, human_template)
print(response)
result = response["choices"][0]["message"]["content"]
send_answer(result, token)
