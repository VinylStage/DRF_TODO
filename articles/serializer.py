from rest_framework import serializers
from articles.models import Article


class ArticleSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.id

    def get_user(self, obj):
        return obj.user.email

    def get_title(self, obj):
        return obj.title


class ArticleDetailSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    is_complete = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.id

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
        fields = "__all__"
