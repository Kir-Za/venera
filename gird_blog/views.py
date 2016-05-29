from django.shortcuts import render
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from gird_blog.models import SiteInfo, Newslenta, Event, Article, Keywords


# Create your views here.
def home(request):
    main_info = SiteInfo.objects.get(lable="О проекте")
    return render(request, 'index.html', {'main_info': main_info})

def newslenta(request):
    events = Event.objects.all().filter(time__gte=timezone.now())
    news_list = Newslenta.objects.all().filter(time__lte=timezone.now())
    paginator = Paginator(news_list, 20)
    page = request.GET.get('page')
    try:
        newslenta = paginator.page(page)
    except PageNotAnInteger:
        newslenta = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        newslenta = paginator.page(paginator.num_pages)
    return render(request, 'news.html', {'newslenta': newslenta, 'events': events})

def articles(request, tag_id=None):
    if tag_id == None:
        articles_list = Article.objects.all()
    else:
        articles_list = Article.objects.filter(keywords__pk = tag_id)
    tags = Keywords.objects.all().order_by('tag_word')
    paginator = Paginator(articles_list, 5)
    page = request.GET.get('page')
    try:
        articleslenta = paginator.page(page)
    except PageNotAnInteger:
        articleslenta = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results.
        articleslenta = paginator.page(paginator.num_pages)
    return render(request, 'articles.html', {'articleslenta': articleslenta, 'tags': tags})

def detail(request, article_id):
    article = Article.objects.get(pk=article_id)
    return render(request, 'detail.html', {'article': article})

def projects(request):
    return render(request, 'projects.html', {})

def contacts(request):
    contact_info = SiteInfo.objects.get(lable="Контакты")
    return render(request, 'contacts.html', {'contact_info': contact_info})
