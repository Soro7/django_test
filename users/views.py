from .models import User
from .serializers import ChangePasswordSerializer


def changePassword(request):
    ser = ChangePasswordSerializer(data= request.data)
    
    if ser.is_valid:
        user= request.user
        data = ser.validated_data
        if user.check_password(data['old_password']) and data['new_password']==data['confirm_password']:
            user.set_password(data['new_password'])
        
        
        