from base import get_token, get_task, send_answer


task_name = "helloapi"

token = get_token(task_name)
task = get_task(token)
cookie = task['cookie']
send_answer(cookie, token)
