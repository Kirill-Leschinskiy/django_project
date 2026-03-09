from django.shortcuts import render


def home(request):
    """Контроллер для главной страницы"""
    return render(request, 'home.html')


def contacts(request):
    """Контроллер для страницы контактов"""
    context = {}

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print(f'Получено сообщение от {name}: {message}, телефон: {phone}')

        context['success'] = 'Сообщение успешно отправлено!'

    return render(request, 'contacts.html', context)
