from base import get_token, get_task, send_answer


task_name = "functions"

token = get_token(task_name)
task = get_task(token)
print(task)
addUser = {
    "name": "addUser",
    "description": "Add user",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
            },
            "surname": {
                "type": "string",
            },
            "year": {
                "type": "integer",
            }
        }
    }
}
send_answer(addUser, token)
