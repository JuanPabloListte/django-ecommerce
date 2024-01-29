from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import Token
from .models import Product, Reviews

class ProductSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField(source='user.avatar.url')
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = Product
        fields = '__all__'
        
    def get_avatar(self, obj):
        return obj.user.avatar.url
        
class ReviewSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Reviews
        fields = '__all__'
        
    def get_reviews(self, obj):
        rev = obj.reviews_set.all()
        serializers = ReviewSerializer(rev, many=True)
        return serializers.data