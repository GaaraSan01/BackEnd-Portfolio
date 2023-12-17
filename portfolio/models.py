from django.db import models

class Projeto(models.Model):
    CATEGORIA = (
        ('B', 'Back-end'),
        ('F', 'Front-end'),
        ('D', 'DevOps'),
        ('S', 'Full-Stack')
    )

    imagem = models.ImageField(blank=True)
    titulo = models.CharField(max_length=30, blank=False)
    categoria = models.CharField(max_length=1, choices=CATEGORIA, null=False, default='F')
    descricao = models.TextField(max_length=255, blank=False)
    link = models.CharField(max_length=100, blank=False, default='')

    def __str__(self) -> str:
        return self.titulo
