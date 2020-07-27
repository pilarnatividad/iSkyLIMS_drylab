from rest_framework import serializers
from iSkyLIMS_drylab.models import PipelineExternalDataJobs
from iSkyLIMS_drylab.models import ParameterPipeline
from iSkyLIMS_drylab.models import Service
from iSkyLIMS_wetlab.models import SamplesInProject

class ParameterPipelineSerializer (serializers.ModelSerializer):
    class Meta:
         model = ParameterPipeline
         fields = '__all__'

class PipelineExternalDataJobsSerializer (serializers.ModelSerializer):
    class Meta:
         model = PipelineExternalDataJobs
         fields = '__all__'

class PipelineExternalDataJobsBSerializer (serializers.ModelSerializer):
    class Meta:
         model = PipelineExternalDataJobs
         fields =  ['serviceRequestNumber','jobState']

class SamplesInProjectSerializer (serializers.ModelSerializer):
    class Meta:
         model = SamplesInProject
         fields = ['sampleName']


class ServiceSerializer (serializers.ModelSerializer):
    serviceProjectNames = serializers.StringRelatedField(many=True)
    class Meta: 
        model = Service
        fields =['serviceRequestNumber','serviceFileExt', 'serviceProjectNames', 'serviceFileExt']

