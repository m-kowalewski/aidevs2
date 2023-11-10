from base import get_token, get_task, send_answer, openai_audio_to_text


task_name = "whisper"

token = get_token(task_name)
task = get_task(token)
print(task)
# TODO: add mp3 download function
path = "mateusz.mp3"
transcript = openai_audio_to_text(path)['text']
print(transcript)
send_answer(transcript, token)
