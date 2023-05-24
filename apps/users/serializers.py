#This line imports the User model from the current package. 
from .models import User 

#This line imports the serializers module from the Django REST Framework.
from rest_framework import serializers 

#This line imports the make_password and check_password functions from Django's authentication framework.
from django.contrib.auth.hashers import make_password,check_password

#This Line imports the datetime module, which is used to handle date and time values
import datetime

#This line imports the token_hex function from the secrets module. This function is used to generate a random token.
from secrets import token_hex



#Requested fields received from frontend 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email','profile','token', 'token_expires')
        
class UserSignUpSerializer(serializers.ModelSerializer):
    email =serializers.CharField(required=True)
    password = serializers.CharField(write_only=True,required=True)
    token = serializers.CharField(read_only=True)
    token_expires = serializers.DateTimeField(read_only=True)
    profile = serializers.ImageField(required=False)
    class Meta:
        model  = User
        fields = ('id','name','email','password','profile','token','token_expires')
    
    def create(self, validate_data):
        
        if User.objects.filter(email=validate_data['email']):
            raise serializers.ValidationError({'email':['This Email is already registered.']})
        
        #Encrypting the password
        validate_data['password'] = make_password(validate_data['password'])
        
        #Generating a token
        validate_data['token'] = token_hex(30)
        validate_data['token_expires'] = datetime.datetime.now() + datetime.timedelta(days=7)
        
        return super().create(validate_data)
    
    
class UserSignInSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    name = serializers.CharField(read_only=True)
    token = serializers.CharField(read_only=True)
    token_expires = serializers.DateTimeField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'token', 'token_expires')

# The create method is overridden to handle the sign-in logic.
# The email and password fields are retrieved from the validated data.
    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        if ( not email or not password):
            raise serializers.ValidationError({"message":["please add email and password"]})
        # The user is saved, and the user object is returned as the response.
        user = User.objects.filter(email = email)
        if(not user):
            raise serializers.ValidationError({"message":["Email does not exists, please register to continue"]})
        validate = check_password(password, user[0].password)
        if( not validate):
             raise serializers.ValidationError("The password is incorrect.")
        user[0].token = token_hex(30)
        user[0].token_expires=datetime.datetime.now() + datetime.timedelta(days=7)
        user[0].save()
        return user[0]
        # If the email or password is incorrect, a ValidationError is raised with the appropriate error message.
       
    
    
