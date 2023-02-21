from django.shortcuts import redirect, render

from NewsInfo.models import NewsInformation


def INDEX(request):
    news = NewsInformation.objects.all()

    context = {
        'news':news,
    }
    return render(request, 'index.html', context)

def ADD(request):
    if request.method == "POST":
        title = request.POST.get('title')
        news_details = request.POST.get('news_details')
        cover_image = request.POST.get('cover_image')

        news = NewsInformation(
            title = title,
            news_details = news_details,
            cover_image = cover_image,
        )

        news.save()
        return redirect('home')

    return render(request, 'index.html')


def EDIT(request):
    news = NewsInformation.objects.all()

    context = {
        'news':news,
    }
    return redirect(request, 'index.html', context)


def UPDATE(request, id):
    if request.method == "POST":
        title = request.POST.get('title')
        news_details = request.POST.get('news_details')
        cover_image = request.POST.get('cover_image')

        news = NewsInformation(
            id = id,
            title = title,
            news_details = news_details,
            cover_image = cover_image,
        )

        news.save()
        return redirect('home')
    return redirect(request, 'index.html')


def DELETE(request, id):
    news = NewsInformation.objects.filter(id = id).delete()
    context = {
        'news':news,
    }
    return redirect('home')