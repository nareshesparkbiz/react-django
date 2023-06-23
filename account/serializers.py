
from rest_framework import serializers

from .models import MyUser

class UserRegisterSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type': 'password'},write_only=True)
    class Meta:
        model=MyUser
        fields=['email','firstname','lastname','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def validate(self, attrs):
        password=attrs.get('password')
        respass=attrs.get('password2')

        if password!=respass:
            raise serializers.ValidationError("Password and Confirm doesn't match ")
        return attrs
    
    def create(self,validate_data):
        return MyUser.objects.create_user(**validate_data)




class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(style={'input_type': 'email'})
    class Meta:
        model=MyUser
        fields=['email', 'password']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=MyUser
        fields=['id','email', 'firstname', 'lastname']


class UserChangePasswordSerializer(serializers.Serializer):
    password=serializers.CharField(max_length=255,style={'input_type': 'password'},write_only=True)
    password2=serializers.CharField(max_length=255,style={'input_type': 'password'},write_only=True)

    class Meta:
        fields=['password', 'password2']
    
    def validate(self,attrs):
        pass1=attrs.get('password')
        pass2=attrs.get('password2')

        if pass1!=pass2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        else:
            user=self.context.get('user')

            user.set_password(pass1)
            user.save()
            return attrs
