from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from iSkyLIMS_drylab.models import PipelineExternalDataJobs
from iSkyLIMS_drylab.models import ParameterPipeline
from iSkyLIMS_wetlab.models import SamplesInProject
from iSkyLIMS_wetlab.models import Projects
from iSkyLIMS_drylab.models import Service
from .serializers import PipelineExternalDataJobsSerializer
from .serializers import PipelineExternalDataJobsBSerializer
from .serializers import ParameterPipelineSerializer
from .serializers import SamplesInProjectSerializer
from .serializers import ServiceSerializer
# Create your views here.
#class PipelinesViewSet(viewsets.ModelViewSet):
#    serializer_class = PipelinesSerializer
#    queryset = Pipelines.objects.all()

# view to load all the records from the model  PipelineExternalDataJobs 
@api_view(['GET',])
def service_list(request):
    service = Service.objects.all()
    serializer = ServiceSerializer(service, many=True)
    return Response(serializer.data)

@api_view(['GET',])
def jobs_list(request):

   jobs = PipelineExternalDataJobs.objects.all()
   serializer = PipelineExternalDataJobsSerializer(jobs,many=True)
   return Response(serializer.data)

# view to load all the records from the model whose jobState is state
@api_view(['GET',])
def jobs_list_state(request,state):
   try:
       jobs = PipelineExternalDataJobs.objects.filter(jobState=state)
   except PipelineExternalDataJobs.DoesNotExist:
       return Response(status=status.HTTP_404__FOUND)
   #jobsstate = get_object_or_404(jobs, jobState=state).last()
   serializer = PipelineExternalDataJobsSerializer(jobs,many=True)
   return Response(serializer.data)

@api_view(['GET'],)
def get_pipeline(request,pipeline):
   try:
      pipeline =  ParameterPipeline.objects.filter(id =pipeline)
   except ParameterPipeline.DoesNotExist:
      return Response(status=status.HTTP_404_FOUND)
   serializer = ParameterPipelineSerializer(pipeline,many=True)
   return Response(serializer.data)

@api_view(['GET'],)
def get_samplesinproject(request,service):
   try:
      project_name = Service.objects.filter(serviceRequestNumber = service).serviceProjectNames
      project_id = Projects.objects.get(projectName__exact = project_name).id
      samples = SamplesInProject.objects.filter(project_id = project_id)
   except SamplesInProject.DoesNotExist:
      return Response(status=status.HTTP_404_FOUND)
   serializer = SamplesInProjectSerializer(samples, many=True)
   return Response(serializer.data)


#view to update the entire record
@api_view(['PUT',])
def api_update_job(request, service):
   try:
      pipejob = PipelineExternalDataJobs.objects.get(serviceRequestNumber=service)
   except PipelineExternalDataJobs.DoesNotExist:
      return Response({'message': 'Pipe does not exist'},status = status.HTTP_404_NOT_FOUND)
   
   #pipejob_data = JSONParser().parse(request)
   pipejob_serializer = PipelineExternalDataJobsSerializer(pipejob,data=request.data)
   if pipejob_serializer.is_valid():
       pipejob_serializer.save()
       return Response(pipejob_serializer.data)
   return Response(pipejob_serializer.errors, status = status.HTTP_400_BAD_REQUEST) 
   
# view to update the field passed in request, from the service passed by argument
@api_view(['PATCH',])
def api_update_state(request, service):
   try:
      pipejob = PipelineExternalDataJobs.objects.get(serviceRequestNumber=service)
   except PipelineExternalDataJobs.DoesNotExist:
      return Response({'message': 'Pipe does not exist'},status = status.HTTP_404_NOT_FOUND)
 
   #pipejob_data = JSONParser().parse(request)
   pipejob_serializer = PipelineExternalDataJobsBSerializer(pipejob,data=request.data)
   if pipejob_serializer.is_valid():
       pipejob_serializer.save()
       return Response(pipejob_serializer.data)
   return Response(pipejob_serializer.errors, status = status.HTTP_400_BAD_REQUEST)  
