from django.db import models


class Users(models.Model):
    email = models.EmailField(max_length=128)
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    patronymic = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)

    def _str_(self):
        return self.autUser.username


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.IntegerField()


class Pereval(models.Model):
    # NEW = 'NW'
    # PENDING = 'PN'
    # ACCEPTED = 'AC'
    # REJECTED = 'RJ'
    STATUS_CHOICES = [
        ('NEW', 'new'),
        ('PENDING', 'pending'),
        ('ACCEPTED', 'accepted'),
        ('REJECTED', 'rejected'),
    ]

    beauty_title = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    other_titles = models.CharField(max_length=128)
    connect = models.CharField(max_length=128, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    coord_id = models.OneToOneField('Coords', on_delete=models.CASCADE)
    tourist_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='NEW')
    level = models.ForeignKey('Level', on_delete=models.CASCADE)


class Level(models.Model):

    DIFFICULTY_LEVEL = (
        ('1A', '1A'),
        ('1Б', '1Б'),
        ('2A', '2A'),
        ('2Б', '2Б'),
        ('3A', '3A'),
        ('3Б', '3Б')
    )

    winter_lev = models.CharField(max_length=2, choices=DIFFICULTY_LEVEL)
    spring_lev = models.CharField(max_length=2, choices=DIFFICULTY_LEVEL)
    summer_lev = models.CharField(max_length=2, choices=DIFFICULTY_LEVEL)
    autumn_lev = models.CharField(max_length=2, choices=DIFFICULTY_LEVEL)


class Images(models.Model):
    image = models.ImageField(upload_to='static/images')
    title = models.CharField(max_length=100)
    pereval_id = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return self.title
