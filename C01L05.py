from base import get_token, get_task, send_answer, send_question, openai_create


task_name = "liar"

token = get_token(task_name)
task = get_task(token)
print(task)
text = "How laser works?"
answer = send_question(text, token)
print(answer)

system_template = """
Answer only by one word.
Answer only YES or NO.
Verify if the answer is true answer for below question:
"How laser works?"
"""
human_template = answer['answer']
response = openai_create(system_template, human_template)
print(response)
result = response["choices"][0]["message"]["content"]
print(result)
send_answer(result, token)
