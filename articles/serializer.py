from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.Serializer):
    user = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.id

    def get_title(self, obj):
        return obj.title

    def get_is_complete(self, obj):
        return obj.is_complete

    def get_updated_at(self, obj):
        return obj.updated_at

    def get_created_at(self, obj):
        return obj.created_at

    class Meta:
        model = Article
        fields = "__all__"


class ArticleCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("title", "content", "is_complete")
