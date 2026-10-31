from rest_framework import serializers

from Employee_app.models import Employee
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    def validate(self, data):
        if data['Age']<=0:
            raise serializers.ValidationError("Age should not be zero")
        return data


#create() is called after validation and before saving







