
from rest_framework import status as sc  # Status codes
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response

from .models import Agent, FuzzingTarget
from .serializers import AgentSerializer, FuzzingTargetSerializer


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def agent_list(request):
    """
    List all agents
    """
    if request.method == 'GET':
        agents = Agent.objects.all()
        serializer = AgentSerializer(agents, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AgentSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=sc.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=sc.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def agent_detail(request, pk):
    try:
        # id ~ pk
        agent = Agent.objects.get(pk=pk)
    except:
        return Response(status=sc.HTTP_404_NOT_FOUND)  

    if request.method == 'GET':
        serializer = AgentSerializer(agent)
        return Response(serializer.data)
    
    elif request.method == 'PUT' :
        serializer = AgentSerializer(agent, data=request.data)

        if(serializer.is_valid()):  
            serializer.save() 
            return Response(serializer.data, status=sc.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=sc.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        agent.delete() 
        return Response(status=sc.HTTP_204_NO_CONTENT)
    
    else:
        return Response(status=sc.HTTP_405_METHOD_NOT_ALLOWED)
