from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

def send_html_email(subject, template_name, context, recipient_list):
    
    html_message = render_to_string(template_name, context)
    plain_message = strip_tags(html_message)
    
    from_email = 'IFRI TIMETABLE <no-reply@kabirou-alassane.com>'
    
    email = EmailMultiAlternatives(subject, plain_message, from_email, recipient_list)
    email.attach_alternative(html_message, "text/html")
    
    return email.send()
