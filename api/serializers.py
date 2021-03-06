from django.contrib.auth.models import Permission
from guardian.models import UserObjectPermission
from rest_framework import serializers

from api.models import CustomUser, Pattern, Plotter, PlotterUserObjectPermission, PatternUserObjectPermission, \
    PlotterPattern


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class UserSerializerAdmin(serializers.ModelSerializer):
    children = RecursiveField(many=True, read_only=True)

    # parent = serializers.IntegerField(source='CustomUser.id')

    class Meta:
        model = CustomUser
        fields = '__all__'
        # fields = ['id', 'username', 'password', 'parent', 'children', 'administrator', 'dealer']


class UserSerializerDealer(serializers.ModelSerializer):
    children = RecursiveField(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'parent', 'children']


class PlotterSerializerAdmin(serializers.ModelSerializer):
    # creator = serializers.IntegerField(source='creator.id')

    class Meta:
        model = Plotter
        fields = '__all__'


class PlotterSerializer(serializers.ModelSerializer):
    # creator = serializers.IntegerField(source='creator.id')
    whole_amount = serializers.IntegerField(read_only=True)

    class Meta:
        model = Plotter
        fields = '__all__'


class PatternSerializer(serializers.ModelSerializer):
    printed_num = serializers.IntegerField(read_only=True)

    class Meta:
        model = Pattern
        fields = "__all__"


class PlotterPatternStatSerializerAdmin(serializers.ModelSerializer):
    class Meta:
        model = PlotterPattern
        fields = '__all__'


class PlotterPatternStatSerializer(serializers.ModelSerializer):
    plotter = serializers.PrimaryKeyRelatedField(read_only=True)
    pattern = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = PlotterPattern
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class PlotterUserObjectPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlotterUserObjectPermission
        fields = '__all__'


class PatternUserObjectPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatternUserObjectPermission
        fields = '__all__'
