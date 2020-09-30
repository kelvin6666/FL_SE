from django.shortcuts import render,redirect
from .models import Tutorial,FilesAdmin
from django.contrib.auth.models import User
from django.views.generic import ListView,TemplateView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm
# Create your views here.








def home(request):
    context={
        
        }
    return render(request,'tutorial/homepage.html',context)




class TutorialListView(ListView):
    model = Tutorial #choosing the database 
    template_name = 'tutorial/home.html' #specifying the template
    context_object_name = 'Tutorial' #the object name in the template
    ordering = ['-date_published'] #to arrange the post from the latest date published
    paginate_by = 5 #to limit 5 question per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['file'] = FilesAdmin.objects.all()
        return context


class TutorialDetailView(DetailView): 
    model = Tutorial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['file'] = FilesAdmin.objects.all()
        return context

@login_required
def search(request):
    error = False # Initially no error
    if 'search' in request.GET: # To check there is ‘search’ exist in request.GET/Verify that there is non-empty value  
        search = request.GET['search'] # To Define that search is in the request.GET
        if not search: # If submit empty value
            error = True # It will display error messages
        else:
            users = User.objects.filter(username__icontains=search)
            tutorials = Tutorial.objects.filter(title__icontains=search) # It will show/filter questions based on the keyword
            context = {
                'tutorials': tutorials,
                'users' :users,
                 'query': search,
                'file' : FilesAdmin.objects.all()
            }
            return render(request, 'tutorial/search_results.html', context)
    context = {
        'error': error,
        'file' : FilesAdmin.objects.all()
    }
    return render(request, 'tutorial/search_results.html', context) 

@login_required
def download(request,path):
	file_path=os.path.join(settings.MEDIA_ROOT,path)
	if os.path.exists(file_path):
		with open(file_path,'rb')as fh:
			response=HttpResponse(fh.read(),content_type="application/adminupload")
			response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
			return response
	raise Http404

def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = request.FILES.get('files')
            FilesAdmin(file=newdoc)
            form.save()
            return redirect('tutorial')
        else:
            message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page

    # Render list page with the documents and the form
    context = {'file' : FilesAdmin.objects.all(), 'form': form}
    return render(request, 'tutorial/notes_upload.html', context)