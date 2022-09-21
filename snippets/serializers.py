from rest_framework import serializers

from snippets.models import Snippets, STYLE_CHOICES, LANGUAGE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippets
        fields = ["id", "title", "code", "linenos", "language", "style"]

    def create(self, validated_data):
        """
        Create and return a new `Snippets` instance, given validated data.
        """
        return Snippets.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippets` instance, given validated data.
        """
        instance.title = validated_data.get("title", instance.title)
        instance.code = validated_data.get("code", instance.code)
        instance.linenos = validated_data.get("linenos", instance.linenos)
        instance.language = validated_data.get("language", instance.language)
        instance.style = validated_data.get("style", instance.styel)
        instance.save()

        return instance