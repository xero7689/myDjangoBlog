from django.shortcuts import render, get_object_or_404,  HttpResponseRedirect
from blog.models import Post, postTag
from work.models import Image
from django.utils import timezone
from django.views.generic.dates import YearArchiveView, MonthArchiveView
from django.views.generic import ListView
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from blog2.settings import MEDIA_URL
from blog.forms import ContactForm
from django.views.generic.edit import FormView
from calendar import month_name

allTags = postTag.objects.all()
allPubPosts = Post.objects.filter(published=True)

#Current Post
current_year = timezone.now().year
current_month = timezone.now().month
current_posts = Post.objects.filter(created__year=current_year, created__month=current_month)

#User Method
def get_archive_dict():
	archive_dict = {}
	for post in allPubPosts:
		if post.created.year not in archive_dict:
			archive_dict[post.created.year] = []
		if post.created.month not in archive_dict[post.created.year]:
			archive_dict[post.created.year].append(post.created.month)
	return archive_dict

archive = get_archive_dict()	


# Create your views here.
def index(request):

    return render(request, 'blog/index3.html', {'allPubPosts': allPubPosts, 'allTags': allTags, 'current_posts': current_posts, 'archive': archive})

def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    postTags = post.tags.all()
    return render(request, 'blog/post3.html', {'post':post, 'postTags':postTags, 'allTags':allTags,'current_posts': current_posts, 'archive': archive})

def tag(request, tagName):
    tag = get_object_or_404(postTag, tagName=tagName)
    tagPost = tag.post_tags.all()
    tagName = tag.tagName
    return render(request, 'blog/tag3.html', {'tagPost': tagPost, 'tagName': tagName,'allTags': allTags, 'current_posts': current_posts, 'archive': archive})

class tagList(ListView):
	model = postTag
	template_name = "blog/taglist.html"

def about(request):
    return render(request, 'blog/about.html')

class work(ListView):
	model = Image
	image = Image.objects.all()
	template_name = "work/work.html"
	
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {"image": self.image,"media_url": MEDIA_URL})

class archiveList(ListView):
	model = Post
	template_name = "blog/archive.html"
	
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {"archive": archive, "allPubPosts": allPubPosts})

class ContactView(FormView):
	template_name = "blog/contact.html"
	form_class = ContactForm
	
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/contactSuccess/')
		return render(request, self.template_name, {'form': form})

def ContactSuccess(request):
	return render(request, 'blog/contactSuccess.html')
	

class ArticleYearArchiveView(YearArchiveView):
	queryset = Post.objects.all()
	date_field = "created"
	make_object_list = True
	allow_future = True

class ArticleMonthArchiveView(MonthArchiveView):
	queryset = Post.objects.all()
	date_field = "created"
	make_object_list = True
	allow_future = True

