from django.shortcuts import render


def about(request):  # Представление страницы о сайте
    template = 'pages/about.html'
    return render(request, template)


def rules(request):  # Представление страницы правил
    template = 'pages/rules.html'
    return render(request, template)
