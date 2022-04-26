from django.conf import settings
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView, FormView, LoginView
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, FormView

from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from authapp.models import User
from basket.models import Basket
from mainapp.mixin import BaseClassContextMixin, UserDispatchMixin


# def login(request):
#
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = auth.authenticate(username=username, password=password)
#             if user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#             else:
#                 print('Пользователь не активный')
#         else:
#             print(form.errors)
#     else:
#         form = UserLoginForm()
#     context = {
#         'title': 'Geekshop | Авторизация',
#         'form': form
#     }
#     return render(request, 'authapp/login.html', context)

class LoginGBView(LoginView, BaseClassContextMixin):
    template_name = 'authapp/login.html'
    form_class = UserLoginForm
    title = 'Geekshop | Авторизация'

# def register(request):
#
#     if request.method == 'POST':
#         form = UserRegisterForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Вы успешно зарегистрировались')
#             return HttpResponseRedirect(reverse('authapp:login'))
#
#         else:
#             print(form.errors)
#     else:
#         form = UserRegisterForm()
#
#
#     context = {
#         'title': 'Geekshop | Регистрация',
#         'form': form
#     }
#     return render(request, 'authapp/register.html', context)


class RegisterView(FormView, BaseClassContextMixin):
    model = User
    title = 'Geekshop | Регистрация'
    form_class = UserRegisterForm
    template_name = 'authapp/register.html'
    success_url = reverse_lazy('authapp:login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save()
            if self.send_verify_link(user):
                messages.set_level(request, messages.SUCCESS)
                messages.success(request, 'Вы успешно зарегистрировались')
                return HttpResponseRedirect(reverse('authapp:login'))
            else:
                messages.set_level(request, messages.ERROR)
                messages.error(request, form.errors)
        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, form.errors)
        context = {'form': form}
        return render(request, self.template_name, context)

    def send_verify_link(self, user):
        verify_link = reverse('authapp:verify', args=[user.email, user.activation_key])
        subject = f'Для активации учетной записи {user.username} пройдите по ссылки'
        message = f'Для подтверждения учетной записи {user.username} на портале \n {settings.DOMAIN_NAME}{verify_link}'
        return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

    def verify(self, email, activate_key):
        try:
            user = User.objects.get(email=email)
            if user and user.activation_key == activate_key and not user.is_activation_key_expires():
                user.activation_key = ''
                user.activation_key_expires = None
                user.is_active = True
                user.save()
                auth.login(self, user)
            return render(self, 'authapp/verification.html')
        except Exception as e:
            return HttpResponseRedirect(reverse('index'))


# def logout(request):
#     auth.logout(request)
#     return render(request, 'mainapp/index.html')

class Logout(LogoutView):
    template_name = 'mainapp/index.html'

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             messages.set_level(request, messages.SUCCESS)
#             messages.error(request, 'Данные изменены')
#             form.save()
#         else:
#             messages.set_level(request, messages.ERROR)
#             messages.error(request, form.errors)
#
#     user_select = request.user
#     baskets = Basket.objects.filter(user=user_select)
#     total_quantity = sum(basket.quantity for basket in baskets)
#     total_sum = sum(basket.sum() for basket in baskets)
#
#     context = {
#         'title': 'Geekshop | Профиль',
#         'form': UserProfileForm(instance=user_select),
#         'baskets': baskets,
#         'total_sum': total_sum,
#         'total_quantity': total_quantity
#     }
#     return render(request, 'authapp/profile.html', context)

class ProfileFormView(UpdateView, BaseClassContextMixin, UserDispatchMixin):
    model = User
    template_name = 'authapp/profile.html'
    form_class = UserProfileForm
    title = 'Geekshop | Профиль'
    success_url = reverse_lazy('authapp:profile')

    def get_context_data(self, **kwargs):
        context = super(ProfileFormView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context

    def form_valid(self, form):
        messages.set_level(self.request, messages.SUCCESS)
        messages.error(self.request, 'Данные изменены')
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())



    def get_object(self, queryset=None):
        return User.objects.get(id=self.request.user.pk)