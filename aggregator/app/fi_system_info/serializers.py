from rest_framework import routers, serializers, viewsets
from .models import Agent, FuzzingTarget


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id',
                  'created',
                  'host',
                  'port',
                  'title',
                  "description"
        ]
    
    # already create() and update() default methods


class FuzzingTargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuzzingTarget
        fields = ['id',
                  'agent',
                  'target_name',
                  'priority',
                  'last_status'
        ]

    # already create() and update() default methods
