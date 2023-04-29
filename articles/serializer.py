from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.Serializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email

    class Meta:
        model = Article
        fields = "__all__"
