
from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    category = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class NoteLink(models.Model):
    source = models.ForeignKey(
        Note,
        on_delete=models.CASCADE,
        related_name="outgoing_links"
    )

    target = models.ForeignKey(
        Note,
        on_delete=models.CASCADE,
        related_name="incoming_links"
    )

    relationship = models.CharField(
        max_length=100,
        default="related"
    )

    def __str__(self):
        return f"{self.source} → {self.target}"
