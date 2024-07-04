from django.contrib import messages
from django.shortcuts import redirect, render
# from django.http import HttpResponse
# from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from django.contrib.sites.shortcuts import get_current_site
# from django.core.mail import EmailMessage, send_mail
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_str
# from QuantPair_Server import settings
# from .tokens import generate_token

# custom functions to redirect to appropriate places
def home(request) :
    # render index.html
    return render(request, "registration/index.html")

def signin(request) :
    # if user is filling for and has pressed submit 
    if request.method == "POST" : 
        # get form data
        username =  request.POST.get('username')
        pass1 = request.POST.get('pass1')
        # authenticate using auth module
        user = authenticate(username=username, password=pass1)
        # if user found
        if user is not None :
            # login the user
            login(request, user)
            fname = user.first_name
            # render the index page
            return render(request, 'registration/index.html', {'fname' : fname})
        else :
            # give error message 
            messages.error(request, "Wrong Credentials")
            # looks for the function with name home and calls the render there
            return redirect('home')
    # if not sent POST request, just render the signin page 
    return render(request, "registration/signin.html")

def signup(request) :
    # if user is filling for and has pressed submit 
    if request.method == "POST" :
        # getting relevant data
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        

        # Checks on username, email, passwords etc and doinsg some condition checks
        if User.objects.filter(username = username) :
            messages.error(request, "Username already exists")
            return redirect('home')
        
        elif User.objects.filter(email = email) :
            messages.error(request, "Email already exists")
            return redirect('home')
        
        elif pass1 != pass2 :
            messages.error(request, "Passwords do not match")
            return redirect('home')
        
        else : 
            # creating a user object
            user = User.objects.create_user(username, email, pass1)
            user.first_name = fname
            user.last_name = lname
            # user.is_active = False
            # this user object will be stored in the auth_table of selected database, in this version, QuantPair_DB
            user.save()
            # success message
            messages.success(request, "Account Successfully Created")
            
            #uncomment when relevant data is filled in info.py and less secure apps is enabled

            #automated email system
            # subject = 'Welcome to <...>'
            # message = "Hello" + user.first_name + "\n" + "Welcome to <...>!! " + "\n" + "Please click link below to activate your account!" + "\n"
            # from_email = settings.EMAIL_HOST_USER
            # to_email = [user.email]
            # send_mail(subject, message, from_email, to_email, fail_silently = True) 

            #email confirmation
            # current_site = get_current_site(request)
            # email_subject = "Confirm your email address!!"
            # message2 = render_to_string('registration/email_confirmation.html', {
                # 'name' : user.first_name,
                # 'domain' : current_site.domain,
                # 'uid' : urlsafe_base64_encode(force_bytes(user.pk)),
                # 'token' : generate_token.make_token(user),
            # })
            # email = EmailMessage(
                # email_subject,
                # message2,
                # from_email,
                # to_email,
            # )
            # email.fail_silently = True
            # email.send()
            return redirect('signin')
        

    # if user hasnt sent POST request, just render this signup page
    return render(request, "registration/signup.html")

def signout(request) : 
    # when user presses signout, use inbuilt logout function
    logout(request)
    messages.success(request, "Logged you out of your account")
    return redirect('home')


#uncomment when relevant data is filled in info.py and less secure apps is enabled

# def activate(request, uibd64, token) :
    # try :
        # uid = force_text(urlsafe_base64_decode(uibd64))
        # user = User.objects.get(pk = uid)
    # except(TypeError, ValueError, OverflowError, User.DoesNotExist) :
        # user = None
    
    # if user is not None and generate_token.check_token(user, token) :
        # user.is_active = True
        # user.save()
        # login(request, user)
        # return redirect('index')
    # else :
        # return render(request, 'registration/activation_failed.html')
