from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class LoginView(View):

    templates_name = 'accounts/login.html'

    def get(self,request):
        context = {}
        try:
            if request.user.is_authenticated:
                return redirect('/')

            success_msg = self.request.GET.get('success_msg')
            msg = self.request.GET.get('msg')

            return render(request,self.templates_name,context)
        except Exception as e:
            print(e)
            context['msg'] = 'Something Went Wrong, Please Try Again or Contact Us'
            return render(request,self.templates_name,context)


    def post(self,request):
        context = {}
        try:
            if request.user.is_authenticated:
                return redirect('/')

            username = request.POST.get("username")
            if not username:
                context['msg'] = 'Error ! Please Enter Your Username'
                return render(request,self.templates_name,context)

            password = request.POST.get('password')
            if not password:
                context['msg'] = "Error ! Please, Enter Your password"
                return render(request,self.templates_name,context)

            check_user = User.objects.filter(username = username)
            if check_user:
                if check_user[0].is_active == True and check_user[0].is_staff == True:
                    username_auth = authenticate(username = username, password = password)
                    return redirect('/')
     
                else:
                    print('56')
                    context['msg'] = 'Error ! Sorry, You have not confirmed your account yet'
                    return render(request,self.templates_name,context)


            else:
                print('62')
                context['msg'] = 'Error ! Incorrect Username and Password, Please try again'
                return render(request,self.templates_name,context)
            return render(request,self.templates_name,context)

        except Exception as e:
            print("\n" * 3)
            print(e)
            print("\n" * 3)
            context['msg'] = 'Something Went Wrong, Please Try Again or Contact Us'
            return render(request,self.templates_name,context)



