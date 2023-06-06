import requests
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def chatbot(request):
    title = 'Chatbot'
    return render(request, 'chatbot.html', {'title': title})


def question(request, question):
    url = 'http://backend:3000/api/chatgpt/'
    header = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    payload = {
        "prompt": question,
        "model": "<custom-model>",
        "max_tokens": 2000,
        "temperature": 0.7,
        "n": 1
    }

    response = requests.request(method='post', url=url, headers=header, json=payload)

    if response.status_code == 200:
        return JsonResponse(response.json(), safe=False)
    else:
        return JsonResponse(
            {
                "response": "'Não foi possível processar sua consulta. Falha de comunicação com o ChatGPT!'"
            }, safe=False
        )

