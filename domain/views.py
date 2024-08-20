from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Domain, Employee, Contact
from django.contrib import messages
from django.core.mail import send_mail


# Create your views here.

def index(request):
    domains = Domain.objects.order_by('-add_date').filter(is_sold =False)[:9]
    context = {'domains': domains}
    return render(request, 'pages/index.html', context)

    
def domains(request):
     domains = Domain.objects.order_by('-add_date').filter(is_sold =False)
     paginator = Paginator(domains, 12)
     page = request.GET.get('page')
     paged_domains = paginator.get_page(page)

     context = {
    'domains': paged_domains
  }
     return render(request, 'pages/domains.html',context)


def about(request):
     employees = Employee.objects.order_by('-add_date').all()

     context = {'employees': employees}
     return render(request, 'pages/about.html', context)


  

def domain(request, domain_id):
  domain = get_object_or_404(Domain, pk=domain_id)

  context = {
    'domain': domain
  }

  return render(request, 'pages/domain.html', context)

  

def search(request):
  queryset_list = Domain.objects.all()

  # Keywords
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(title__icontains=keywords)

    context = {'domains': queryset_list}


  return render(request, 'pages/search.html', context)

def contact(request):
   if request.method == 'POST':
      domain = request.POST['domain']
      domain_id = request.POST['domain_id']
      name = request.POST['name']
      phone = request.POST['phone']
      offer = request.POST['offer']
      email = request.POST['email']
      message = request.POST['message']

      contact =Contact(
         domain=domain, domain_id=domain_id,
         name =name, email=email, phone=phone, message=message, offer = offer )
      
      contact.save()
      messages.success(request, 'Your request has been submitted successfully, we will get back to you soon')
      return redirect('/domains/'+ domain_id)

def contact_us(request):
      if request.method == 'POST':
      
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        
        message = request.POST['message']

        contact =Contact(
          name =name, email=email, phone=phone, message=message)
      
        contact.save()
        messages.success(request, 'Your request has been submitted successfully, we will get back to you soon')
        return redirect('contacts')
      return render(request, 'pages/contact.html')


