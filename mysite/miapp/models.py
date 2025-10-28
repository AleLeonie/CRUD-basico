from django.db import models

# Create your models here.

class UsuarioTipo(models.Model):
    id_usuario_tipo = models.CharField(primary_key=True, max_length=10,  db_column='ID_USUARIO_TIPO')
    usuario_tipo = models.CharField(max_length=30, blank=True, db_column='USUARIO_TIPO')

    def __str__(self):
        if self.usuario_tipo:
            return f"{self.usuario_tipo} (ID: {self.id_usuario_tipo})"
        return f"Tipo sin nombre (ID: {self.id_usuario_tipo})"
    
    class Meta:
        verbose_name = 'Tipo de Usuario'
        verbose_name_plural = 'Tipos de Usuario'


class Pais(models.Model):
    id_pais = models.CharField(primary_key=True, max_length=10, db_column='ID_PAIS')
    pais = models.CharField(max_length=50, blank=True, db_column='PAIS')

    def __str__(self):
        if self.pais:
            return f"{self.pais} (ID: {self.id_pais})"
        return f"País sin nombre (ID: {self.id_pais})"
    
    class Meta:
        verbose_name = 'País'
        verbose_name_plural = 'Países'


class Region(models.Model):
    id_region = models.CharField(primary_key=True, max_length=10, db_column='ID_REGION')
    region = models.CharField(max_length=50, blank=True, db_column='REGION')

    def __str__(self):
        if self.region:
            return f"{self.region} (ID: {self.id_region})"
        return f"Región sin nombre (ID: {self.id_region})"
    
    class Meta:
        verbose_name = 'Región'
        verbose_name_plural = 'Regiones'


class Usuario(models.Model):
    id_usuario = models.CharField(primary_key=True, max_length=10, db_column='ID_USUARIO')
    
    id_usuario_tipo = models.ForeignKey(UsuarioTipo, on_delete=models.CASCADE, db_column='ID_USUARIO_TIPO')
    id_pais = models.ForeignKey(Pais, on_delete=models.CASCADE, db_column='ID_PAIS')
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE, db_column='ID_REGION')

    usuario_nombre = models.CharField(max_length=50, blank=True, db_column='USUARIO_NOMBRE')
    usuario_apellido = models.CharField(max_length=50, blank=True, db_column='USUARIO_APELLIDO')
    telefono = models.CharField(max_length=20, blank=True, db_column='TELEFONO')
    email = models.EmailField(blank=True, db_column='EMAIL')
    direccion = models.CharField(max_length=100, blank=True, db_column='DIRECCION')

    def __str__(self):
        nombre_completo = f"{self.usuario_nombre} {self.usuario_apellido}".strip()
        if nombre_completo:
            return f"{nombre_completo} (ID: {self.id_usuario})"
        return f"Usuario sin nombre (ID: {self.id_usuario})"
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['usuario_nombre', 'usuario_apellido']


class DocumentoTipo(models.Model):
    id_documento_tipo = models.CharField(primary_key=True, max_length=10, db_column='ID_DOCUMENTO_TIPO')
    documento_tipo = models.CharField(max_length=30, blank=True, db_column='DOCUMENTO_TIPO')

    def __str__(self):
        if self.documento_tipo:
            return f"{self.documento_tipo} (ID: {self.id_documento_tipo})"
        return f"Tipo de documento sin nombre (ID: {self.id_documento_tipo})"

    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documentos'


class Documento(models.Model):
    id_documento = models.CharField(primary_key=True, max_length=10, db_column='ID_DOCUMENTO')
    documento_nombre = models.CharField(max_length=50, blank=True, db_column='DOCUMENTO_NOMBRE')

    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, db_column='ID_USUARIO')
    id_documento_tipo = models.ForeignKey(DocumentoTipo, on_delete=models.CASCADE, null=True, blank=True, db_column='ID_DOCUMENTO_TIPO')

    def __str__(self):
        if self.documento_nombre:
            return f"{self.documento_nombre} (ID: {self.id_documento})"
        return f"Documento sin nombre (ID: {self.id_documento})"

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'
