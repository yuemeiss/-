from django.db import models

# Create your models here.
class Author(models.Model):
    id = models.CharField(primary_key=True, max_length=80)
    name = models.CharField(max_length=80, blank=True, null=True)
    gender = models.CharField(max_length=3, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    add_desc = models.TextField(blank=True, null=True)
    headline = models.CharField(max_length=255, blank=True, null=True)
    intro = models.CharField(max_length=255, blank=True, null=True)
    school = models.CharField(max_length=100, blank=True, null=True)
    jobname = models.CharField(max_length=100, blank=True, null=True)
    answer_count = models.CharField(max_length=50, blank=True, null=True)
    question_count = models.CharField(max_length=50, blank=True, null=True)
    follower_count = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.name
    class Meta:
        # managed = False
        db_table = 'author'

class Answer(models.Model):
    id = models.CharField(primary_key=True, max_length=80)
    content = models.TextField(blank=True, null=True)
    pub_time = models.CharField(max_length=80, blank=True, null=True)
    update_time = models.CharField(max_length=80, blank=True, null=True)
    endorse = models.CharField(max_length=50, blank=True, null=True)
    comment_num = models.CharField(max_length=50, blank=True, null=True)
    qid = models.ForeignKey('Question')
    ahthor_id = models.ForeignKey(Author)


    class Meta:
        # managed = False
        db_table = 'answer'





class Comment(models.Model):
    id = models.CharField(primary_key=True, max_length=80)
    author_name = models.CharField(max_length=100, blank=True, null=True)
    pub_time = models.CharField(max_length=50, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    like_num = models.CharField(max_length=50, blank=True, null=True)
    child_comment_count = models.CharField(max_length=50, blank=True, null=True)
    child_comments = models.TextField(blank=True, null=True)
    aid = models.ForeignKey('Answer')
    author_id = models.ForeignKey('Author')

    class Meta:
        # managed = False
        db_table = 'comment'


class Question(models.Model):
    id = models.CharField(primary_key=True, max_length=80)
    title = models.CharField(max_length=80, blank=True, null=True)
    pub_time = models.CharField(max_length=80, blank=True, null=True)
    answer_count = models.CharField(max_length=50, blank=True, null=True)
    follower_count = models.CharField(max_length=50, blank=True, null=True)
    intro = models.CharField(max_length=255, blank=True, null=True)
    author_id = models.ForeignKey('Author',related_name='questions')
    def __str__(self):
        return self.title

    class Meta:
        # managed = False
        db_table = 'question'


class Tags(models.Model):
    id = models.CharField(primary_key=True, max_length=80)
    name = models.CharField(max_length=80, blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    tag_url = models.CharField(max_length=255, blank=True, null=True)
    qtype = models.ManyToManyField('Question')
    def __str__(self):
        return self.name

    class Meta:
        # managed = False
        db_table = 'tags'
