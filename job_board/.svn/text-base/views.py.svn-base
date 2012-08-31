# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from job_board.forms import *
from django.template import RequestContext
from django.core.paginator import *
from django.db.models import Q
from job_board.models import *
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from urlparse import urlsplit
from datetime import datetime

def index(request):
    return render_to_response('job_board/index.html', {'title': 'Job Board Home'}, RequestContext(request))

def logout(request):
    auth.logout(request)
    return render_to_response("job_board/index.html", {"flash": 'You Have Successfully Logged Out!'}, RequestContext(request))

### Start Job Posting Views #####

def job_view(request, id=None):
    job=Job_Post.objects.get(pk=id)
    return render_to_response('job_board/job_view.html', {'job':job},RequestContext(request))

def job_list(request):
    search_term=request.GET.get('search_term', '')
    sort_by=request.GET.get('sort_by', 'id')
    search_list=search_term.split()
    jobs=Job_Post.objects.all().filter(is_active=True).filter(date_start_post__lte=datetime.now()).exclude(date_end_post__lte=datetime.now())
    for term in search_list:
        jobs=jobs.filter(Q(id__iregex=term) |
                         Q(job_description__iregex=term) |
                         Q(company__name__iregex=term) |
                         Q(job_title__iregex=term) )
    jobs=jobs.order_by(sort_by)
    paginator=Paginator(jobs, 50)
    try:
        page=int(request.GET.get('page', '1'))
    except ValueError:
        page=1
    try:
        jobs=paginator.page(page)
    except (EmptyPage, InvalidPage):
        jobs=paginator.page(paginator.num_pages)

    return render_to_response("job_board/job_list.html", {'job_board':jobs, "search_term":search_term, "sort_by":sort_by}, RequestContext(request))

@login_required()
def job_edit(request, id=None):
    if request.method=='POST':
        if id:
            job=Job_Post.objects.get(pk=id)
            form=Job_Post_Form(request.POST, instance=job)
        else:
            form=Job_Post_Form(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/job_board/job_list')
        else:
            return render_to_response("job_board/job_edit.html", {"form":form}, RequestContext(request))
    else:
        try:
            job=Job_Post.objects.get(pk=id)
            form=Job_Post_Form(instance=job)
        except:
            form=Job_Post_Form()
    return render_to_response("job_board/job_edit.html", {"form":form}, RequestContext(request))

def company_job_submit(request):
    if request.method=='POST':
        form=Job_Post_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/job_board/job_list')
        else:
            return render_to_response("job_board/job_edit.html", {"form":form}, RequestContext(request))
    else:
        form=Job_Post_Form()
    return render_to_response("job_board/job_edit.html", {"form":form}, RequestContext(request))



def job_delete(request, id=None):
    job=Job_Post.objects.get(pk=id)
    job.is_active=False
    job.save()
    return redirect(job_list)

####  Start Company Views  #######

def company_view(request, id=None):
    company=Company.objects.get(pk=id)
    return render_to_response('job_board/company_view.html', {'company':company},RequestContext(request))

def company_list(request):
    search_term=request.GET.get('search_term', '')
    sort_by=request.GET.get('sort_by', 'id')
    search_list=search_term.split()
    companies=Company.objects.all().filter(is_active=True)
    for term in search_list:
        companies=companies.filter(Q(id__iregex=term) |
                         Q(name__iregex=term) |
                         Q(city__iregex=term) |
                         Q(state__iregex=term) )
    companies=companies.order_by(sort_by)
    paginator=Paginator(companies, 50)
    try:
        page=int(request.GET.get('page', '1'))
    except ValueError:
        page=1
    try:
        companies=paginator.page(page)
    except (EmptyPage, InvalidPage):
        companies=paginator.page(paginator.num_pages)

    return render_to_response("job_board/company_list.html", {'companies':companies, "search_term":search_term, "sort_by":sort_by}, RequestContext(request))

@login_required()
def company_edit(request, id=None):
    if request.method=='POST':
        if id:
            company=Company.objects.get(pk=id)
            form=Company_Form(request.POST, instance=company)
        else:
            form=Company_Form(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/job_board/company_list')
        else:
            return render_to_response("job_board/company_edit.html", {"form":form}, RequestContext(request))
    else:
        try:
            company=Company.objects.get(pk=id)
            form=Company_Form(instance=company)
        except:
            form=Company_Form()
    return render_to_response("job_board/company_edit.html", {"form":form}, RequestContext(request))

def company_delete(request, id=None):
    company=Company.objects.get(pk=id)
    company.is_active=False
    company.save()
    return redirect(job_list)
