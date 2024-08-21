from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Domain, Employee, Contact
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


# Create your views here.

def index(request):
    domains = Domain.objects.order_by('-add_date').filter(is_sold=False)[:9]
    context = {'domains': domains}
    return render(request, 'pages/index.html', context)


def domains(request):
    domains = Domain.objects.order_by('-add_date').filter(is_sold=False)
    paginator = Paginator(domains, 12)
    page = request.GET.get('page')
    paged_domains = paginator.get_page(page)

    context = {
        'domains': paged_domains
    }
    return render(request, 'pages/domains.html', context)


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

        contact = Contact(
            domain=domain, domain_id=domain_id,
            name=name, email=email, phone=phone, message=message, offer=offer)

        contact.save()
        messages.success(
            request, 'Your request has been submitted successfully, we will get back to you soon')

        # Email to user who filled out the contact form
        subject = 'Thank you for your offer for {}'.format(domain)
        from_email = 'Sterlingdomainsinc@gmail.com'
        to_email = email
        context = {
            'name': name,
            'phone': phone,
            'email': email,
            'message': message,
            'domain': domain,
            'offer': offer
        }
        html_content = render_to_string('emails/user_offer.html', context)
        msg = EmailMessage(subject, html_content, from_email, [to_email])
        msg.content_subtype = 'html'
        msg.send()

        # Email to admin
        subject = 'New Offer for {}'.format(domain)
        from_email = 'Sterlingdomainsinc@gmail.com'
        to_email = 'sterlingdomainsinc@gmail.com'
        context = {
            'domain': domain,
            'name': name,
            'phone': phone,
            'email': email,
            'offer': offer,
            'message': message
        }
        html_content = render_to_string('emails/admin_offer.html', context)
        msg = EmailMessage(subject, html_content, from_email, [to_email])
        msg.content_subtype = 'html'
        msg.send()

    return redirect('/domains/' + domain_id)


def contact_us(request):
    if request.method == 'POST':

        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']

        message = request.POST['message']

        contact = Contact(
            name=name, email=email, phone=phone, message=message)

        contact.save()
        messages.success(
            request, 'Your request has been submitted successfully, we will get back to you soon')

       # Send email notification to admin
        subject_admin = 'New Enquiry'
        from_email = 'sterlingdomainsinc@gmail.com'
        to_email_admin = 'sterlingdomainsinc@gmail.com'
        context_admin = {
            'name': name,
            'phone': phone,
            'email': email,
            'message': message
        }
        html_content_admin = render_to_string(
            'emails/admin_enquiry.html', context_admin)
        msg_admin = EmailMessage(
            subject_admin, html_content_admin, from_email, [to_email_admin])
        msg_admin.content_subtype = 'html'
        msg_admin.send()

        # Send email notification to user
        subject_user = 'Thank you for your enquiry'
        from_email = 'sterlingdomainsinc@gmail.com'
        to_email_user = email
        context_user = {
            'name': name,
            'phone': phone,
            'email': email,
            'message': message
        }
        html_content_user = render_to_string(
            'emails/user_enquiry.html', context_user)
        msg_user = EmailMessage(
            subject_user, html_content_user, from_email, [to_email_user])
        msg_user.content_subtype = 'html'
        msg_user.send()

        return redirect('contacts')
    return render(request, 'pages/contact.html')
