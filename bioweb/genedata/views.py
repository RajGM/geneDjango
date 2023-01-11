from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic import DetailView 
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from .models import *

def index(request):
    return render(request,'genedata/index.html',{"test":"Test"})

# Create your views here.
class GeneList(DetailView):
    
    #def get_template_names(self):
    #    return render('genedata/index.html')
    
    def get_template_names(self):
        if True:
            return 'genedata/list.html'
        return 'genedata/index.html'


    '''
    model = Gene
    context_object_name = 'master_genes'
    #template_name = 'genedata/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        if "poslist" in self.request.get_full_path():
            context['genes'] = Gene.objects.filter(entity__exact='Chromosome').filter(sense__startswith='+')
        if 'type' in self.kwargs:
            if "Chromosome" in self.kwargs['type'] or "Plasmid" in self.kwargs['type']:
                context['genes'] = Gene.objects.filter(entity__exact=self.kwargs['type'])
            return context
    
    def get_template_names(self):
        if "poslist" in self.request.get_full_path():
            return 'genedata/list.html'
        if 'type' in self.kwargs:
            if "Chromosome" in self.kwargs['type'] or "Plasmid" in self.kwargs['type']:
                return 'genedata/list.html'
        return 'genedata/index.html'

    '''


'''
class GeneDetail(DetailView):
    model = Gene
    context_object_name = 'gene'
    template_name = 'genedata/gene.html'    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context

class GeneDelete(DeleteView):
    model = Gene
    success_url = "/"
    #template_name_suffix = '_confirm_delete'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context

def create_ec(request):
    master_genes = Gene.objects.all()
    if request.method == 'POST':
        form = ECForm(request.POST)
        if form.is_valid():
            ec = EC()
            ec.ec_name = form.cleaned_data['ec_name']
            ec.save()
            return HttpResponseRedirect('/create_ec/')
    else:
        ecs = EC.objects.all()
        form = ECForm()
    return render(request, 'genedata/ec.html', {'form': form,'ecs': ecs, 'master_genes': master_genes})    

class GeneCreate(CreateView):
    model = Gene
    template_name = 'genedata/create_gene.html'
    form_class = GeneForm
    success_url = "/create_gene/"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context

class GeneUpdate(UpdateView):
    model = Gene
    fields = fields = ['gene_id', 'entity', 'start', 'stop','sense', 'start_codon','sequencing', 'ec']
    template_name_suffix = '_update_form'
    success_url = "/"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context

'''
'''
class GeneList(ListView):
    model = Gene
    context_object_name = 'master_genes'
    template_name = 'genedata/index.html'
'''


'''
def create_gene(request):
    master_genes = Gene.objects.all()
    if request.method == 'POST':
        form = GeneForm(request.POST)
        if form.is_valid():
            gene = form.save()
            return HttpResponseRedirect('/create_ec/')
        else:
            return render(request, 'genedata/create_gene.html', {'error':"failed", 'master_genes': master_genes, 'form': form})
    else:
        form = GeneForm()
        master_genes = Gene.objects.all()
    return render(request, 'genedata/create_gene.html', {'form':form, 'master_genes': master_genes})
'''

'''
def gene(request, pk):
    gene = Gene.objects.get(pk=pk)
    gene.access += 1
    print("Gene record:", pk, "access count:", str(gene.access))
    gene.save()
    master_genes = Gene.objects.all()
    return render(request, 'genedata/gene.html', {'gene': gene, 'master_genes': master_genes})
'''

'''
def delete(request, pk):
    GeneAttributeLink.objects.filter(gene_id=pk).delete()
    Gene.objects.filter(pk=pk).delete()
    return HttpResponseRedirect("/")
'''


'''
def index(request):
    master_genes = Gene.objects.all()
    return render(request, 'genedata/index.html', {'master_genes': master_genes})
'''

'''
def list(request, type):
    genes = Gene.objects.filter(entity__exact=type)
    master_genes = Gene.objects.all()
    return render(request, 'genedata/list.html', {'genes': genes, 'type': type,'master_genes': master_genes})
'''

'''
class GeneList(ListView):
    model = Gene
    context_object_name = 'master_genes'
    template_name = 'genedata/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        if 'type' in self.kwargs:
            if "Chromosome" in self.kwargs['type'] or "Plasmid" in self.kwargs['type']:context['genes'] = Gene.objects.filter(entity__exact=self.kwargs['type'])
            return context
    
    def get_template_names(self):
        if 'type' in self.kwargs:
            if "Chromosome" in self.kwargs['type'] or "Plasmid" in self.kwargs['type']:
                return 'genedata/list.html'
        return 'genedata/index.html'
'''


'''
def poslist(request):
    genes = Gene.objects.filter(
        entity__exact='Chromosome').filter(sense__startswith='+')
    master_genes = Gene.objects.all()
    return render(request, 'genedata/list.html', {'genes': genes, 'type':
                                                  'PosList','master_genes': master_genes})

'''