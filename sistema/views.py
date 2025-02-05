from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'Login/login.html'

