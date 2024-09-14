from django.urls import path
from .views import index, CategoriaAventura, Aventura1, Aventura2,  CategoriaConduccion, categoriaDeportes, CategoriaEstrategia, \
    CategoriaInfantiles, Conduccion1, Conduccion2, Deporte1, Deporte2, Estrategia1, Estrategia2, Infantil1, Infantil2, \
    login, Principal, recuperar_contrasena, register
from .views import home, form_vehiculo, form_mod_vehiculo, form_del_vehiculo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
if settings.DEBUG:
    urlpatterns+= static(settings.Media_URL, document_root=settings.MEDIA_ROOT)
    
urlpatterns = [
    path('', index, name="index"),
    path('CategoriaAventura/', CategoriaAventura, name="CategoriaAventura"),
    path('Aventura1/', Aventura1, name="Aventura1"),
    path('Aventura2/', Aventura2, name="Aventura2"),
    path('CategoriaConduccion/', CategoriaConduccion, name="CategoriaConduccion"),
    path('categoriaDeportes/', categoriaDeportes, name="categoriaDeportes"),
    path('CategoriaEstrategia/', CategoriaEstrategia, name="CategoriaEstrategia"),
    path('CategoriaInfantiles/', CategoriaInfantiles, name="CategoriaInfantiles"),
    path('Conduccion1/', Conduccion1, name="Conduccion1"),
    path('Conduccion2/', Conduccion2, name="Conduccion2"),
    path('Deporte1/', Deporte1, name="Deporte1"),
    path('Deporte2/', Deporte2, name="Deporte2"),
    path('Estrategia1/', Estrategia1, name="Estrategia1"),
    path('Estrategia2/', Estrategia2, name="Estrategia2"),
    path('Infantil1/', Infantil1, name="Infantil1"),
    path('Infantil2/', Infantil2, name="Infantil2"),
    path('login/', login, name="login"),
    path('Principal/', Principal, name="Principal"),
    path('recuperar_contrasena/', recuperar_contrasena, name="recuperar_contraseña"),
    path('register/', register, name="register"),
    path('form-vehiculo', form_vehiculo, name="form_vehiculo"),
    path ('form_mod_vehiculo/<id>', form_mod_vehiculo, name="form_mod_vehiculo"),
    path ('form_del_vehiculo/<id>', form_del_vehiculo, name="form_del_vehiculo"),
]
