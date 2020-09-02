from rest_framework import serializers
from .models import CourseModel, CourseTopicModel, SkillModel


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseModel
        exclude = ('course_topics', 'novice_skills', 'intermediate_skills', 'expert_skills')


class CourseTopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseTopicModel
        fields = ['id', 'name']


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = SkillModel
        fields = ['id', 'slug']


class CourseTopicsAndSkillsSerializer(serializers.ModelSerializer):
    
    course_topics = CourseTopicSerializer(many=True)
    novice_skills = SkillSerializer(many=True)
    intermediate_skills = SkillSerializer(many=True)
    expert_skills = SkillSerializer(many=True)

    class Meta:
        model = CourseModel
        fields = ['id', 'title', 'course_topics', 'novice_skills', 'intermediate_skills', 'expert_skills']