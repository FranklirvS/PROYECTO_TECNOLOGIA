from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import formularioiniciosesión,MyPasswordResetForm,MyPasswordChangeForm,MySetPasswordForm

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contactos/',views.contacto,name="contacto"),
    path("categoria/<slug:val>",views.CategoriaView.as_view(),name="categoria"),
    path("categoria-titulo/<val>",views.CategoriaTitle.as_view(),name="categoria-titulo"),
    path("producto-detalle/<int:pk>",views.ProductoDetalle.as_view(),name="producto-detalle"),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('adress/',views.direccion, name= 'adress'),
    path("updateDireccion/<int:pk>",views.updateDireccion.as_view(),name="updateDireccion"),

    path('agregar-a-carrito/',views.agregar_a_carrito, name='agregar-a-carrito'),
    path('carrito/',views.mostrar_carro, name='mostrarcarro'),


    #login autentificacion
    path('Registro/',views.formularioregistroclientesViews.as_view(),name="Registroclientes"),
    path('cuentas/inicio_de_sesión/',auth_view.LoginView.as_view(template_name="app/login.html",authentication_form =formularioiniciosesión),name="login"),
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='app/cambio_contrasena.html', form_class=MyPasswordChangeForm,success_url='/passwordchangedone'),name='cambiocontrasena'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
    path('logout',auth_view.LogoutView.as_view(next_page='login'),name='logout'),


    path('password-reset/', auth_view.PasswordResetView.as_view(template_name="app/password_reset.html", form_class=MyPasswordResetForm),name='password_reset'),

    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view( template_name='app/password_reset_done.html'),name='password_reset_done'),

    path('password-reset/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),

    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name="password_reset_complete"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
