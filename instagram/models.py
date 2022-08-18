from django.db import models


class Post(models.Model):
    message = models.TextField()
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def message_length(self):
    #     return len(self.message)

    # message_length.short_description = "메세지 글자수"

    # java의 toString과 동일
    def __str__(self) -> str:
        return self.message
