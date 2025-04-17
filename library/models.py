from django.db import models

class Author(models.Model):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)


    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


    def __str__(self):
        return self.full_name


class Book(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    isdn = models.CharField(max_length=255)
    author = models.ForeignKey(Author , related_name='authors', on_delete=models.CASCADE)
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    public_date = models.DateField(null=True)


    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='books', null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = 'Картина'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return self.title


