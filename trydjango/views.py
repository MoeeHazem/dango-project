import random 
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article




def home_view (request,id=None, *args, **kwargs):
    print(id)
    number = random.randint(10,12321)
    name = "mohammed"
    random_id = random.randint(1,2)
    article_obj = Article.objects.get(id= random_id)
    article_queryset = Article.objects.all()
    context = {
        "object_list" : article_queryset,
        "object" : article_obj,
        "title" : article_obj.title,
        "content" : article_obj.content
    }
    HTML_STRING = render_to_string("home_view.html", context=context)
    #<hi> {title} ! </hi>
    #<P> {content} ! </P>
    #""".format(**context)
    print(100 * 1000)
    return HttpResponse(HTML_STRING)