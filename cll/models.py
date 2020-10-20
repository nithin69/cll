from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

Free_ind_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No'),
)

Online_ind_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No'),
)

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(max_length=100, blank=True)
    subject_desc = models.CharField(max_length=255, blank=True)
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # phone = models.CharField(max_length=30, blank=True)
    # bio = models.TextField(max_length=500, blank=True)
    # location = models.CharField(max_length=30, blank=True)
    # birth_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.subject_name

class SubjectTopic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    topic_name = models.CharField(max_length=100, blank=True)
    topic_desc = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.topic_name

class TopicSubtopic(models.Model):
    topic = models.ForeignKey(SubjectTopic, on_delete=models.CASCADE)
    subtopic_name = models.CharField(max_length=100, blank=True)
    subtopic_desc = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.subtopic_name

class SubtopicLearningUrl(models.Model):
    subtopic = models.ForeignKey(TopicSubtopic, on_delete=models.CASCADE)
    learning_url = models.CharField(max_length=255, blank=True)
    learning_url_desc = models.CharField(max_length=255, blank=True)
    learning_url_section_name = models.CharField(max_length=255, blank=True)
    learning_url_code_link = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.id

class SubjectCourse(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    course_url = models.CharField(max_length=255, blank=True)
    free_ind = models.CharField(max_length=1, choices=Free_ind_CHOICES)
    online_ind = models.CharField(max_length=1, choices=Online_ind_CHOICES)
    course_desc = models.TextField(max_length=500, blank=True)
    def __str__(self):
        return self.id


class SubjectProject(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    project_url = models.CharField(max_length=255, blank=True)
    project_desc = models.TextField(max_length=500, blank=True)
    def __str__(self):
        return self.id

class LearningUrlVote(models.Model):
    learning_url = models.ForeignKey(SubjectProject, on_delete=models.CASCADE)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)
    comment = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.id

class ProjectVote(models.Model):
    subject_project = models.ForeignKey(SubjectProject, on_delete=models.CASCADE)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)
    comment = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.id

class CourseVote(models.Model):
    subject_course = models.ForeignKey(SubjectProject, on_delete=models.CASCADE)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1)
    comment = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.id
