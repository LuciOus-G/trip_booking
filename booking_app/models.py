from django.db import models
from django.utils.text import slugify
from datetime import date as dt
from PIL import Image as Images
import string,random
from django_resized import ResizedImageField
# Create your models here.

class category(models.Model):
    category_name = models.CharField(max_length=255, default='')

    def __str__(self):
        return f"{self.category_name}"


class Post(models.Model):
    name = models.CharField(max_length=100, default=None)
    slug = models.SlugField(blank=True, editable=False, max_length=255)
    desc = models.TextField(default=None)
    date = models.DateField(auto_now_add=True)
    max_people = models.IntegerField(default=None)
    photo1 = ResizedImageField(size=[1980, 1080], default=None, upload_to='media_thumbnail')
    # day1 = models.DateField(blank=True, default=dt(2020, 10, 18), null=True, help_text="Today Date.")
    departure_day = models.DateField(default=dt(2020, 10, 18))
    Price = models.IntegerField(default=None)
    seat = models.CharField(max_length=20, default=None)
    meeting = models.CharField(max_length=256, default=None)
    special = models.BooleanField(default=False)
    special_desc = models.TextField(default=None, blank=True, null=True)
    special_desc = models.TextField(default=None, blank=True, null=True, max_length=620)
    Token = models.CharField(max_length=255, unique=True, blank=True, editable=False, default='')
    categories = models.ForeignKey(category, on_delete=models.CASCADE, default='')
    viewer = models.IntegerField(blank=True, null=True)


    class Meta:
        verbose_name = u'Trip'
        verbose_name_plural = u'Trip'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.Token == '':
            self.Token = self.randomGenerate()
        if not self.seat:
            self.seat = self.max_people
        self.name = str(self.name).upper()

        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return "{}, {}, person {}".format(self.id, self.name, self.seat)

    snp = 85
    def snippet(self):
        return self.desc[:self.snp]

    def randomGenerate(self, size=25, chars=string.ascii_letters + string.digits):
        slug = list(Post.objects.all())
        generate = ''.join(random.choice(chars) for _ in range(size))
        qs = Post.objects.filter(Token=generate).exists()
        if qs:
            randomGenerate(size=size + 1)
        return generate

class PostImage(models.Model):
    images = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.id)

class carousel(models.Model):
    image = ResizedImageField(size=[1980, 1080], default=None, upload_to='media_thumbnail')

    def __str__(self):
        return "{}".format(self.id)


class booking(models.Model):
    name_trip = models.CharField(default=None, max_length=100)
    seat_available = models.CharField(default=None, max_length=50)
    price = models.CharField(default=None, max_length=20)
    place_born = models.CharField(default=None, max_length=20)
    day_born = models.CharField(default=None, max_length=15)
    gender = models.CharField(default=None, max_length=10)
    address = models.CharField(default=None, max_length=255)
    phone1 = models.CharField(default=None,max_length=255)
    people = models.CharField(default=None, max_length=5)
    # automatic
    user_name = models.CharField(default=None, max_length=100)
    customer_id  = models.CharField(default=None,max_length=255)
    booking_id = models.CharField(default=None, max_length=50)
    trip_id = models.CharField(default=None, max_length=50)
    departure_day = models.CharField(default=None, max_length=20)
    meeting_point = models.CharField(max_length=256, default=None)
    total_price = models.CharField(default=None, max_length=20)
    email = models.CharField(default=None,max_length=255)
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    # day = models.DateField(default=dt(2020, 10, 18))

    # class Meta:
    #     verbose_name = u'Booking'
    #     verbose_name_plural = u'Booking'

    def __str__(self):
        return '{} {}'.format(self.id, self.user_name)

class test(models.Model):
    name = models.CharField(default=None, max_length=100)
