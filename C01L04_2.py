import json
from base import get_token, get_task, send_answer, openai_create


task_name = "blogger"

token = get_token(task_name)
task = get_task(token)
print(task)
system_template = """
Napisz wpis na bloga (w języku polskim) na temat przyrządzania pizzy Margherity. 
Jako wejście otrzymasz spis 4 rozdziałów, które muszą pojawić się we wpisie.
Napisz po 3 zdania do każdego rozdziału
Jako odpowiedź musisz zwrócić tablicę (w formacie JSON) złożoną z 4 pól reprezentujących te cztery rozdziały, 
np.: ["tekst 1","tekst 2","tekst 3","tekst 4"]

###
Przykładowe dane wejściowe:
['Wstęp: kilka słów na temat historii pizzy', 'Niezbędne składniki na pizzę', 'Robienie pizzy', 'Pieczenie pizzy w piekarniku']

###
Przykładowa wygenerowana odpowiedź:
["Pizza jest jednym z najbardziej popularnych dań na całym świecie....",
"Aby przygotować pyszną pizzę w domu, potrzebujemy kilku niezbędnych składników.... ",]
"""
chapters = task['blog']
human_template = str(chapters)
response = openai_create(system_template, human_template)
print(response)
result = response["choices"][0]["message"]["content"]
print(result)
send_answer(json.loads(result), token)
