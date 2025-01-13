# Create your views here.

from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from .models import Table
from .forms import TableCreate


def create_view(request):
    form = TableCreate(request.POST or None)
    if form.is_valid():
        form.save()
        form = TableCreate()
    context = {'form': form}
    return render(request, 'create.html', context)


def home_view(request):
    return render(request, 'hello.html', {})


def update_view(request, pk):
    table_update = get_object_or_404(Table, pk=pk)
    form = TableCreate(request.POST or None, instance=table_update)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('read')
    
    form = TableCreate(request.GET or None, instance=table_update) # GET for the first pass
    context = {'form': form}
    return render(request, 'update.html', context)
    

def read_view(request):
    table_reads = Table.objects.all()
    context = {'table_reads': table_reads}
    return render(request, 'read.html', context)


def delete_view(request, pk):
    table_delete = get_object_or_404(Table, pk=pk)
    table_delete.delete()
    return redirect('read')
