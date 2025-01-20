from django.db import models


# Create your models here.
class Author(models.Model):
	last_name = models.CharField(max_length=100, null=True)
	name = models.CharField(max_length=100)
	second_name = models.CharField(max_length=100, null=True)
	url = models.SlugField(unique=True)
	description = models.TextField(blank=True)

	def __str__(self):
		if self.second_name:
			return f"{self.last_name} {self.name} {self.second_name} "
		return f"{self.last_name} {self.name}"

	class Meta:
		ordering = ['last_name', 'name']
		indexes = [
			models.Index(fields=['last_name', 'name']),
		]


class Book(models.Model):
	title = models.CharField(max_length=100)
	url = models.SlugField(unique=True)
	# author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', null=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title


class Authorship(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	seq_num = models.IntegerField()

	def __str__(self):
		return f"{self.book} {self.author} {self.seq_num}"

class Operations(models.Model):
	book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
	qty_change = models.IntegerField()
	date_created = models.DateTimeField(auto_now_add=True)
