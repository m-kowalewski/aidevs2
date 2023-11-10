from base import get_token, get_task, send_answer, openai_create_chat, update_chat_messages


task_name = "whoami"

token = get_token(task_name)
system_template = """
Musisz odgadnąć o jakiej postaci jest mowa.
Zawsze jest mowa o tej samej osobie.
Możesz odpowiadać tylko na dwa sposoby:
1) gdy nie wiesz lub nie jesteś pewny to mówisz jedno słowo: NIE.
2) gdy jesteś całkowicie i absolutnie pewny to mówisz tylko i wyłącznie jak nazywa się ta postać.
Nie dodajesz nic więcej.
"""
messages = []
messages = update_chat_messages(messages, 'system', system_template)
for x in range(10):
    task = get_task(token)
    print("HINT", task['hint'])
    messages = update_chat_messages(messages, 'user', task['hint'])
    response = openai_create_chat(messages)
    print("ASSISTANT:", response)
    messages = update_chat_messages(messages, 'assistant', response)
    if not response.lower() == "nie." and not response.lower() == "nie":
        break
send_answer(response, token)
