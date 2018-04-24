from django.db import models
from django.conf import settings
from django.utils import timezone

from simplemooc.core.mail import send_mail_template


class AnimalManager(models.Manager):

    def search(self, query):
        return self.get_queryset().filter(
            models.Q(name__icontains=query) | \
            models.Q(description__icontains=query) | \
            models.Q(tipo_icontains=query)
        )


class Animal(models.Model):

    name = models.CharField('Nome', max_length=30)
    slug = models.SlugField('Apelido')
    TIPO_CHOICES = (
        (1, 'Cachorro'),
        (2, 'Gato')
    )

    tipo = models.IntegerField('Tipo', max_length=1, choices=TIPO_CHOICES)
    IDADE_CHOICES = (
                 (1, 'Menos de 6 meses'),
                 (2, 'De 6 meses a 1 ano'),
                 (3, 'De 1 a 3 anos'),
                 (4, 'De 3 a 5 anos'),
                 (5, 'Mais de 5 anos')
    )
    idade = models.IntegerField('Idade', max_length=20, choices=IDADE_CHOICES)

    PORTE_CHOICES = (
        (1, 'Pequeno'),
        (2, 'Médio'),
        (3, 'Grande')
    )
    porte = models.IntegerField('Porte', max_length=10, choices=PORTE_CHOICES)

    CASTRADO_CHOICES = (
        (1, 'Sim'),
        (2, 'Não')
    )
    castrado = models.IntegerField('Castrado ?', max_length=10, choices=CASTRADO_CHOICES)

    VERMIFUGADO_CHOICES = (
        (1, 'Sim'),
        (2, 'Não')
    )
    vermifugado = models.IntegerField('Vermifugado ?', max_length=10, choices=VERMIFUGADO_CHOICES)

    VACINADO_CHOICES = (
        (1, 'Sim'),
        (2, 'Não')
    )
    vacinado = models.IntegerField('Vacinado ?', max_length=10, choices=VACINADO_CHOICES)

    COMPORTAMENTO_CHOICES = (
        (1, 'Dócil'),
        (2, 'Agitado'),
        (3, 'Agressivo')
    )
    comportamento = models.IntegerField('Dicas do comportamento', max_length=10, choices=COMPORTAMENTO_CHOICES)


    raça = models.CharField('Raça', max_length=20)
    description = models.TextField('Descrição do Animal', blank=True)
    image = models.ImageField(
        upload_to='Adota/images', verbose_name='Foto perfil',
        null=False, blank=False
    )
    imagebook1 = models.ImageField(
        upload_to='Adota/images', verbose_name='Foto album',
        null=True, blank=True
    )
    imagebook2 = models.ImageField(
        upload_to='Adota/images', verbose_name='Foto album',
        null=True, blank=True
    )
    imagebook3 = models.ImageField(
        upload_to='Adota/images', verbose_name='Foto album',
        null=True, blank=True
    )
    disponivel = models.DateField('Disponivel desde: ')
    ATIVO_CHOICES = (
        (1, 'Ativo'),
        (2, 'Adotado')
    )
    status = models.IntegerField('Situação', choices=ATIVO_CHOICES, default=1, blank=True)
##    ativo = models.BooleanField('Situação',choices = ATIVO_CHOICES)
    contato = models.CharField('Contato para adoção: ', max_length=15)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    objects = AnimalManager()

    def active(self):
         self.status = 1
         self.save()

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('Adota:details', (), {'slug': self.slug})

#     def release_lessons(self):
#         today = timezone.now().date()
#         return self.lessons.filter(release_date__gte=today)
#
    class Meta:
        verbose_name = 'Adoção'
        verbose_name_plural = 'Adoções'
        ordering = ['name']
#
#
# class Lesson(models.Model):
#
#     name = models.CharField('Nome', max_length=100)
#     description = models.TextField('Descrição', blank=True)
#     number = models.IntegerField('Número (ordem)', blank=True, default=0)
#     release_date = models.DateField('Data de Liberação', blank=True, null=True)
#
#     course = models.ForeignKey(Course, verbose_name='Curso', related_name='lessons')
#
#     created_at = models.DateTimeField('Criado em', auto_now_add=True)
#     updated_at = models.DateTimeField('Atualizado em', auto_now=True)
#
#     def __str__(self):
#         return self.name
#
#     def is_available(self):
#         if self.release_date:
#             today = timezone.now().date()
#             return self.release_date >= today
#         return False
#
#     class Meta:
#         verbose_name = 'Aula'
#         verbose_name_plural = 'Aulas'
#         ordering = ['number']
#
#
# class Material(models.Model):
#
#     name = models.CharField('Nome', max_length=100)
#     embedded = models.TextField('Vídeo embedded', blank=True)
#     file = models.FileField(upload_to='lessons/materials', blank=True, null=True)
#
#     lesson = models.ForeignKey(Lesson, verbose_name='Aula', related_name='materials')
#
#     def is_embedded(self):
#         return bool(self.embedded)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Matérial'
#         verbose_name_plural = 'Materiais'
#
#
# class Enrollment(models.Model):
#
#     STATUS_CHOICES = (
#         (0, 'Pendente'),
#         (1, 'Aprovado'),
#         (2, 'Cancelado'),
#     )
#
#     user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, verbose_name='Usuário',
#         related_name='enrollments'
#     )
#     course = models.ForeignKey(
#         Course, verbose_name='Curso', related_name='enrollments'
#     )
#     status = models.IntegerField(
#         'Situação', choices=STATUS_CHOICES, default=1, blank=True
#     )
#
#     created_at = models.DateTimeField('Criado em', auto_now_add=True)
#     updated_at = models.DateTimeField('Atualizado em', auto_now=True)
#
#     def active(self):
#         self.status = 1
#         self.save()
#
#     def is_approved(self):
#         return self.status == 1
#
#     class Meta:
#         verbose_name = 'Inscrição'
#         verbose_name_plural = 'Inscrições'
#         unique_together = (('user', 'course'),)
#
#
# class Announcement(models.Model):
#
#     course = models.ForeignKey(
#         Course, verbose_name='Curso', related_name='announcements'
#     )
#     title = models.CharField('Título', max_length=100)
#     content = models.TextField('Conteúdo')
#
#     created_at = models.DateTimeField('Criado em', auto_now_add=True)
#     updated_at = models.DateTimeField('Atualizado em', auto_now=True)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Anúncio'
#         verbose_name_plural = 'Anúncios'
#         ordering = ['-created_at']
#
#
# class Comment(models.Model):
#
#     announcement = models.ForeignKey(
#         Announcement, verbose_name='Anúncio', related_name='comments'
#     )
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='usuário')
#     comment = models.TextField('Comentário')
#
#     created_at = models.DateTimeField('Criado em', auto_now_add=True)
#     updated_at = models.DateTimeField('Atualizado em', auto_now=True)
#
#     class Meta:
#         verbose_name = 'Comentário'
#         verbose_name_plural = 'Comentários'
#         ordering = ['created_at']
#
#
# def post_save_announcement(instance, created, **kwargs):
#     if created:
#         subject = instance.title
#         context = {
#             'announcement': instance
#         }
#         template_name = 'courses/announcement_mail.html'
#         enrollments = Enrollment.objects.filter(
#             course=instance.course, status=1
#         )
#         for enrollment in enrollments:
#             recipient_list = [enrollment.user.email]
#             send_mail_template(subject, template_name, context, recipient_list)
#
# models.signals.post_save.connect(
#     post_save_announcement, sender=Announcement,
#     dispatch_uid='post_save_announcement'
# )
