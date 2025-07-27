from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import item
from django.template import loader
from .forms import itemform
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.

def index(request):
    item_list = item.objects.all()   # --> all the objects item model have will be stored inside the list
    template = loader.get_template('food/index.html')
    context = {
        'item_list': item_list,
    }
    return HttpResponse(template.render(context,request))

class IndexClassView(ListView):
    model = item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

def detail(request,item_id):
    Item = item.objects.get(pk=item_id)
    template = loader.get_template('food/detail.html')
    context = {
        'Item': Item,
    }
    return HttpResponse(template.render(context,request))

class fooddetail(DetailView):
    model = item
    template_name = 'food/detail.html'
    context_object_name = 'Item'

def create_item(request):
    form = itemform(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item_form.html', {'form': form})

class CreateItem(CreateView):
    model = item
    fields = ['item_name','item_desc','item_price','item_image']
    template_name = 'food/item_form.html'
    
    def form_valid(self, form):
        form.instance.user_name = self.request.user               # who is currently logged in 
        return super().form_valid(form)


def update_item(request,item_id):
    Item = item.objects.get(pk=item_id)
    form = itemform(request.POST or None,instance=Item)
    
    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request,'food/item_form.html', {'form': form,'Item':Item})
    
def delete_item(request,item_id):
    Item = item.objects.get(pk=item_id)
    
    if request.method == 'POST':
        Item.delete()
        return redirect('food:index')
    
    return render(request,'food/item_delete.html', {'Item': Item})


