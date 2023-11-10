from base import get_token, get_task, send_answer, openai_create


task_name = "inprompt"

token = get_token(task_name)
task = get_task(token)
task_data = task['input']
question = task['question']
print("QUESTION:", question)
system_template = """
W odpowiedzi podaj tylko jedno słowo.
Jakie imie zawarte jest w poniższym pytaniu?
"""
human_template = question
response = openai_create(system_template, human_template)
print(response)
name_result = response["choices"][0]["message"]["content"]
print(name_result)
for sentence in task_data:
    if name_result in sentence:
        name_data = sentence
        break
response_2 = openai_create(name_data, question)
print(response_2)
result = response_2["choices"][0]["message"]["content"]
send_answer(result, token)
