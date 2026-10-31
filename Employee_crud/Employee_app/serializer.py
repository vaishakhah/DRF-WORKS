from rest_framework import serializers
from django.contrib.auth.models import User
from models import Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']

    def create(self, validated_data):
        u = User.objects.create_user(**validated_data)
        return u

class EmployeeSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    Name = serializers.CharField(max_length=30)
    Emp_id = serializers.IntegerField()
    Age = serializers.IntegerField()
    Place = serializers.CharField(max_length=30)
    mode_choices =(('male','male'),('female','female'))
    Gender = serializers.ChoiceField(choices=mode_choices)
    Joining_date = serializers.DateField(read_only=True)
    Salary = serializers.FloatField()
    Designation = serializers.CharField(max_length=50)
    image =serializers.ImageField()

    def validate(self,data):
        if data['Age']<=0:
            raise serializers.ValidationError("Age should be positive")


#create() is called after validation and before saving
    def create(self,validated_data):
        print(validated_data)
        emp = Employee.objects.create(**validated_data)
        return emp
    def update(self,instance,validated_data):
        instance.Emp_id = validated_data.get('Emp_id',instance.Emp_id)
        instance.Name = validated_data.get('Name',instance.Name)
        instance.Age = validated_data.get('Age', instance.Age)
        instance.Place = validated_data.get('Place', instance.Place)
        instance.Gender = validated_data.get('Gender',instance.Gender)
        instance.Salary = validated_data.get('Salary',instance.Salary )
        instance.Designation = validated_data.get('Designation', instance.Designation)
        instance.save()
        return instance










