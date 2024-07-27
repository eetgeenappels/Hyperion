from django.shortcuts import render
import json
from . import forms


def index(request):

    # open metadate file
    with open("chat_logs/metadata.json", 'r') as f:
        current_file = json.loads(f.read())["current"]

    with open(f"chat_logs/{current_file}", 'r') as f:
        data = json.loads(f.read())

    if request.method == 'POST':
        form = forms.Prompt(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data as required
            prompt = form.cleaned_data['prompt']
            form = forms.Prompt()

            # send prompt to textgen backend

    else:
        form = forms.Prompt()

    rendering = render(request, "chat.html", {"chat_data": data, "form": form})

    print(str(rendering.content, "UTF-8"))

    return rendering
