from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# Create your models here.

class ModificarUsuario(BaseUserManager):
    use_in_migrations = True
    def _crear_usuario(self, correo, nombre, telefono, contrasena, **informacion_adicional):
        valores = [nombre, nombre, correo]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, valores))
        for informacion_requerida, valor in field_value_map.items():
            if not valor:
                raise ValueError("El valor de {} debe estar definido".format(informacion_requerida))
        correo = self.normalize_email(correo)
        usuario = self.model(
            nombre = nombre,
            correo = correo,
            telefono = telefono,
            **informacion_adicional
        )
        usuario.set_password(contrasena)
        usuario.save(using=self._db)
        return usuario

    def create_user(self, nombre, correo, contrasena, telefono, **informacion_adicional):
        informacion_adicional.setdefault('is_staff', False)
        informacion_adicional.setdefault('is_superuser',False)
        return self._crear_usuario(nombre, correo, telefono, **informacion_adicional)
    
    def create_superuser(self, nombre, correo, contrasena, telefono, **informacion_adicional):
        informacion_adicional.setdefault('is_staff',True)
        informacion_adicional.setdefault('is_superuser',True)
        if informacion_adicional.get('is_staff') is not True:
            raise ValueError('El super usuario debe de ser staff')
        if informacion_adicional.get('is_superuser') is not True:
            raise ValueError('El super usuario debe de ser superusuario')
        return self._crear_usuario(nombre, correo, contrasena, telefono, **informacion_adicional)

class UsuarioModel(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(db_column="id", primary_key=True, null=False, unique=True)
    nombre = models.CharField(db_column="nombre", max_length=225, null=False, unique=True)
    apellido = models.CharField(db_column="apellido", max_length=225, null=False)
    correo = models.CharField(db_column="correo", max_length=255, null=False, unique=True)
    contrasena = models.CharField(db_column="contrasena", max_length=225, null=False)
    telefono = models.IntegerField(db_column="telefono", null=False, unique=True)
    descripcion = models.TextField(db_column="descripcion", null=False)
    sexo = models.CharField(db_column="sexo", max_length=50, null=False)
    imagen = models.CharField(db_column="imagen", max_length=225, null=False)
    direccion = models.CharField(db_column="direccion", max_length=225, null=False)
    creado_el = models.DateField(db_column="creado_el", auto_now_add=True)
    actualizado_el = models.DateField(db_column="actualizado_el", auto_now=True)
    estado = models.BooleanField(db_column="estado", default=True, null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default = timezone.now)
    last_login = models.DateTimeField(null=True)

    objects = ModificarUsuario()

    USERNAME_FIELD = "nombre"
    REQUIRED_FIELDS = ["correo", "contrasena", "telefono"]

    class Meta:
        db_table = "usuarios"

