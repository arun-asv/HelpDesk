from rest_framework import serializers
from django.contrib.auth.models import User
        

class RegisterSerializer(serializers.ModelSerializer):
    
    password2=serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'password2')
                
    def save(self):
        reg=User(
            email=self.validated_data['email'],
            username=self.validated_data['username']
                 
        )
        
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'error': 'Password does not match'})
        
        reg.set_password(password)
        reg.save()
        return reg



class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
