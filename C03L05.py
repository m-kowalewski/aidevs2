from base import get_token, get_task, send_answer, download_json_from_url, openai_create


def parse_question(question):
    system_template = """
    Znajdź imię i nazwisko w podanym pytaniu.
    ###
    Ulubiony kolor Krzysia Rozkaz, to?
    Krzysztof Rozkaz
    Gdzie mieszka Władek Kot?
    Władysław Kot
    Jaki jest ulubiony posiłek Eli Kaki?
    Elżbieta Kaka
    """
    human_template = question
    response = openai_create(system_template, human_template)
    return response['choices'][0]['message']['content']


def find_person(data, name, surname):
    for person in data:
        if person['imie'] == name and person['nazwisko'] == surname:
            return person
    return None


def answer_question(question, person):
    system_template = str(person)
    human_template = question
    response = openai_create(system_template, human_template)
    return response['choices'][0]['message']['content']


task_name = "people"

url = "https://zadania.aidevs.pl/data/people.json"
data = download_json_from_url(url)

token = get_token(task_name)
task = get_task(token)
print(task)
question = task['question']
question_person = list(parse_question(question).split(' '))
person = find_person(data, question_person[0], question_person[1])
if not person:
    print("Could not find")
    quit()
result = answer_question(question, person)
send_answer(result, token)
