import openai
import os
import requests
import urllib.request
import time

from dotenv import load_dotenv
from urllib.error import HTTPError


load_dotenv()


def get_token(task_name):
    api_key = os.getenv('API_KEY')
    payload = {"apikey": api_key}
    token_url_base = os.getenv('TOKEN_URL')
    token_url = token_url_base + task_name
    print("get_token", token_url)
    r = requests.post(token_url, json=payload)
    print("get_token", r)
    r_json = r.json()
    return r_json['token']


def get_task(token):
    task_url_base = os.getenv('TASK_URL')
    task_url = task_url_base + token
    print("get_task", task_url)
    r = requests.get(task_url)
    print("get_task", r)
    return r.json()


def send_answer(result, token):
    answer_url_base = os.getenv('ANSWER_URL')
    answer_url = answer_url_base + token
    print("get_answer", answer_url)
    payload = {"answer": result}
    r = requests.post(answer_url, json=payload)
    print("get_answer", r)
    r_json = r.json()
    for k, v in r_json.items():
        print("{}: {}".format(k, v))


def send_question(text, token):
    task_url_base = os.getenv('TASK_URL')
    task_url = task_url_base + token
    print("send_question", task_url)
    r = requests.post(task_url, data={'question': text})
    print("send_question", r)
    return r.json()


def openai_create(system_template, human_template, model="gpt-3.5-turbo"):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": system_template},
            {"role": "user", "content": human_template},
        ]
    )
    return response


def openai_create_chat(messages, model="gpt-3.5-turbo"):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )
    return response['choices'][0]['message']['content']


def update_chat_messages(messages, role, content):
    messages.append({'role': role, 'content': content})
    return messages


def openai_embedding(text):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    embeddings = response['data'][0]['embedding']
    return embeddings


def openai_moderation(payload):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    response = openai.Moderation.create(input=payload)
    return response


def openai_audio_to_text(path):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    audio_file = open(path, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript


def download_txt_from_url(url):
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
    )
    for x in range(1, 10):
        try:
            response = urllib.request.urlopen(req)
            print("SUCCESS, status={}".format(response.status))
            url_data = response.read().decode('utf-8')
            print("===== URL DATA =====:", url_data)
            return url_data
        except HTTPError as e:
            print("UNSUCCESS, status={}, next try in {} seconds".format(e.status, x*x))
            time.sleep(x*x)
    print("Could not connect with {}".format(url))
    return None
