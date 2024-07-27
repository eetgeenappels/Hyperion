from django.http import StreamingHttpResponse
import json
import requests
backend = "ollama"
current_ollama_model = "dolphin"


# Create your views here.
def generate_chat_message_streaming(request):

    def generate(request):

        request_data = json.loads(request.body)

        # get the chat log
        with open("chat_logs/metadata.json", 'r') as f:
            current_file = json.loads(f.read())["current"]

        with open(f"chat_logs/{current_file}", 'r') as f:
            data = json.loads(f.read())

        data["log"].append(
            {
                "role": "user",
                "content": request_data["prompt"]
            }
        )

        chat_log = data["log"]

        payload = {
            "messages": chat_log,
            "model": current_ollama_model,
            "stream": True
        }

        # stream ollama

        url = 'http://localhost:11434/api/chat'

        s = requests.Session()

        is_first = True

        with s.post(url, json=payload, stream=True) as resp:
            for line in resp.iter_lines():
                if line:
                    if is_first:
                        is_first = False
                        # add message to chat log
                        data["log"].append(
                            {"role": "assistant", "content": ""}
                        )

                    chat_add = json.loads(line)["message"]["content"]

                    data["log"][-1]["content"] += chat_add

                yield json.dumps(data)

        # save new data to file
        with open(f"chat_logs/{current_file}", 'w') as f:
            f.write(json.dumps(data))

    return StreamingHttpResponse(generate(request))
