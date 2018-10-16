from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

from itertools import chain
from django.views.generic import ListView

from persons.models import Post


class SearchView(ListView):
    template_name = 'search/index.html'
    model = Post
    context_object_name = 'posts'  # Default: object_list
    paginate_by = 20
    queryset = Post.objects.all()  # Default: Model.objects.all()

    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super(SearchView, self).get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            blog_results = Post.objects.search(query)

            # combine querysets
            queryset_chain = chain(
                    blog_results,
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)    # since qs is actually a list
            return qs
        return Post.objects.none()  # just an empty queryset as default


def detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'search/details.html', {'post': post})


def send_email(request):
    sujet = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if sujet and message and from_email:
        try:
            send_mail(sujet, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
