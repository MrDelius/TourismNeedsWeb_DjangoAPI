from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from .models import Need, UserProfile, UserCommentedNeed
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.EmailField(source='user.email', read_only=True)
    date_joined = serializers.DateTimeField(source='user.date_joined', read_only=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'name', 'profile_image', 'search_history', 'date_joined']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class CommentPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 200


class CommentSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()

    class Meta:
        model = UserCommentedNeed
        fields = ['user', 'comment']


class NeedSerializer(serializers.ModelSerializer):
    num_likes = serializers.SerializerMethodField()
    num_views = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Need
        fields = ['id', 'title', 'images', 'republic', 'city', 'type', 'search_history',
                  'created_by', 'created_at', 'saved_count', 'num_likes', 'num_views', 'comments']

    def get_num_likes(self, obj):
        return obj.num_likes()

    def get_views(self, obj):
        return obj.num_views()

    def get_comments(self, obj):
        # Check if the context contains a request
        if 'request' in self.context:
            # If it does, check if the request is for a single object
            if 'pk' in self.context['request'].parser_context['kwargs']:
                # If the request is for a single object, fetch and serialize the comments
                comments = UserCommentedNeed.objects.filter(need=obj)
                paginator = CommentPagination()
                page = paginator.paginate_queryset(comments, self.context['request'])
                if page is not None:
                    serializer = CommentSerializer(page, many=True)
                    return paginator.get_paginated_response(serializer.data).data
        # If the context doesn't contain a request or the request is not for a single object, return None
        return None