# -*- coding: utf-8 -*-
# __author__=luhu
from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet


def restore_object(attrs, instance=None):
    """
    Create or update a new snippet instance.
    """
    if instance:
        # Update existing instance
        instance.title = attrs['title']
        instance.code = attrs['code']
        instance.linenos = attrs['linenos']
        instance.language = attrs['language']
        instance.style = attrs['style']
        return instance

    # Create new instance
    return Snippet(**attrs)


class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

