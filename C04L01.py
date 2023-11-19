from base import get_token, get_task, openai_create, currency_nbp, country_details, send_answer


task_name = "knowledge"

token = get_token(task_name)
task = get_task(token)
print(task)
question = task['question']
system_template = """
Skategoryzuj pytania.
Masz 3 kategorie: kurs walut, populacja, wiedza ogólna.
Jeżeli jest to kurs walut to w odpowiedzi dodaj skrót waluty np. pln, usd, sek.
Jeżeli jest to populacja to w odpowiedzi dodaj nazwę kraju w języku angielskim.
Jeżeli jest to wiedza ogólna to nic nie dodawaj.
###
jaki jest teraz kurs dolara? -> kurs walut, usd
ile ludzi mieszka w Polsce? -> populacja, Poland
jaka jest stolica Peru? -> wiedza ogólna"""
human_template = question
response = openai_create(system_template, human_template)
print(response)
result = response["choices"][0]["message"]["content"]
result_splitted = result.split(', ')
if result_splitted[0] == "kurs walut":
    currency = result_splitted[1]
    exchange_rate = currency_nbp(currency)['rates'][0]['mid']
    print("Kurs waluty:", exchange_rate)
    result = str(exchange_rate)
elif result_splitted[0] == "populacja":
    country_name = result_splitted[1]
    country = country_details(country_name)
    population = country[0]['population']
    print("Populacja:", population)
    result = str(population)
elif result_splitted[0] == "wiedza ogólna":
    response = openai_create(human_template)
    print(response)
    result = response["choices"][0]["message"]["content"]

send_answer(result, token)
