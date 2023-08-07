from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# Create your views here.


def Home(request):
    title = 'Alphacs | Transforming Technology Vision Into Reality'
    keywords = "Alpha Cyber Solution, Webdesign at Cheap Cost, WEbdesign, Android Development, ERP development, Seo services in delhi ncr, Seo services in faridabad, smo services, ppc services, adword services, adsense services, "
    description = "Alphacs | Transforming Technology Vision Into Reality. Deal With all type of Web Development and app Development"
    return render(request, 'home.html', {
        'title': title,
        'keywords': keywords,
        'description': description,
    })


def ContactUs(request):
    title = 'Alphacs | contactus'
    keywords = "Contact alpha cyber soloution, Contact Today to Know more about Deals, Contact Alphacs "
    description = "Contact Alpha cyber solution and Feal Free to Ask any Question about Our Services Deals With all Type Of Searvices"
    return render(request, 'contactus.html', {
        'title': title,
        'keywords': keywords,
        'description': description,
    })


def Erp(request):
    title = 'ERP Development | Advanced ERP Softwares | ERP With Test Series'
    keywords = "ERP for colleges, Advanced ERP, Cheap ERP Development, Material ERP System, ERP Development"
    description = "Enterprise resource planning (ERP) is the integrated management of main business, ERP Helps to manage All Data At One Place."
    return render(request, 'erp.html', {
        'title': title,
        'keywords': keywords,
        'description': description,
    })


def Cloud(request):
    title = 'Cloud Services | Cloud Services at Cheap Cost'
    keywords = "Cloud Searvices at Cheap Cost, Setup Cloud For You, Data Portability, Flexibility, Cloud server Optimization, Virtual Machines"
    description = "Cloud computing refers to a computing hardware machine or group of computing, Alphacs is the Best Place to setup your cloud service today."
    return render(request, 'cloud.html', {
        'title': title,
        'keywords': keywords,
        'description': description,
    })


def Crm(request):
    title = 'CRM Development | Alphacs'
    keywords = "custom crm development services, crm development companies in india, crm development process, crm software development services, crm software development company, custom crm development company, crm development companies in india, development of customization in crm, in-house crm software, on-demand software development, how to build a crm system from scratch"
    description = "As a CRM software development company, Alpha Cyber solution (alphacs) aims to deliver user-friendly yet feature-rich solutions. We offer custom CRM solutions that help businesses to leverage business growth."
    return render(request, 'crm.html', {
        'title': title,
        'keywords': keywords,
        'description': description,
    })


def Web(request):
    title = 'Website Designing | web development | All type of website designing'
    keywords = "top web development companies in india, web development company usa, top custom software development company, best website design companies, a web development company, web development at cheap cost, Cost Effective service"
    description = "Alpha cyber solution a Web designing and development company in faridabad and offers best website design and website development services in faridabad."
    return render(request, 'web.html', {
        'title': title,
        'keywords': keywords,
        'description': description,
    })


def Mobile(request):
    title = 'Mobile Development |  Android, IOS Application Development'
    keywords = "mobile app development, what is needed for app development, mobile application development companies, mobile application development course, mobile application development tools, mobile application development languages, mobile app development india, mobile app development services, mobile app developer, mobile app developer salary, mobile app developer jobs, mobile app development lifecycle, major milestones in app development, android app development process step-by step, android app development software, "
    description = "Mobile application development is the set of processes and procedures involved in writing software for small, wireless computing devices. alpha cyber solution provide automated mobile applications like Paytm, e-commerce application"
    return render(request, 'mobile.html', {
        'title': title,
        'keywords': keywords,
        'description': description,
    })


def Seo(request):
    title = 'SEO - Digital marketing | ALphacs Marketing Seriveces '
    keywords = "seo services, Smo services, ppc Services, adword services, adsense services, seo marketing, website seo, seo optimization, seo services company, seo services agency, best seo services, online seo service, professional seo service seo services for small business, seo services delhi, best seo services in delhi ncr,seo agency in delhi, top seo company in delhi, seo services at low price, Seo expert in delhi, Social Media Marketing,"
    description = "Alpha Cyber Solution, the best Digital marketing services in Faridabad, India offers services like SEO, SMO, PPC, ORM and website design for company/agency."
    return render(request, 'seo.html', {
        'title': title,
        'keywords': keywords,
        'description': description,
    })


def ContactForm(request):
    subject = request.POST['subject']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    messages = request.POST['message']
    message = ' Name:- ' + name + ' \n ' + ' Phone: ' + \
        phone + ' \n ' + ' Message: ' + messages

    if subject and message and email:
        try:
            print(subject, name, email)
            send_mail(subject, message, email, ['alphacs.in@gmail.com'])
            messages.success(request, 'success')
            return redirect('contact-us')

        except BadHeaderError:
            messages.warning(request, 'Invalid header found.')

        return redirect('contact-us')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        messages.error(request, 'Make sure all fields are entered and valid.')
