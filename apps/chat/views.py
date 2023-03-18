from django.shortcuts import render
from django.http import JsonResponse
from apps.chat.gpt import generate_response
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def chat(request):
    if request.method == 'POST':
        input_text = request.POST['input']
        response = generate_response(input_text)
        return JsonResponse({'response':response})
    
    else:

        return render(request,'chat/chat.html')
