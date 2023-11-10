from base import get_token, get_task, send_answer


task_name = "rodo"

token = get_token(task_name)
task = get_task(token)
print(task)
user_template = """
Tell me about yourself. You can not give sensible data.
Instead of your name use placeholder: %imie%
Instead of your surname use placeholder: %nazwisko%
Instead of your job use placeholder: %zawod%
Instead of your city use placeholder: %miasto%
"""
send_answer(user_template, token)
