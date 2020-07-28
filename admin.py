from django.contrib import admin
from iSkyLIMS_drylab.models import *
from django_mptt_admin.admin import DjangoMpttAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class FileExtAdmin(admin.ModelAdmin):
	list_display = ('fileExt',)

class PlatformAdmin(admin.ModelAdmin):
	list_display=('platformName',)

class MachinesAdmin (admin.ModelAdmin) :
	list_display=('machineName', 'platformID','machineDescription', 'machineLocation','machineProvider','machineSerialNumber', 'machineState','machineOperationStart','machineOperationEnd','machineNumberLanes')
# 'serviceUsername' refactored to 'serviceUserid' which shows better its real nature
class ServiceAdmin(admin.ModelAdmin):
	list_display=('serviceRequestNumber','serviceUserId','serviceSeqCenter','servicePlatform','serviceRunSpecs','serviceFileExt','serviceFile','serviceStatus','serviceNotes','serviceCreatedOnDate','serviceOnApprovedDate','serviceOnRejectedDate','serviceOnDeliveredDate')
#	list_display=('serviceUserId','serviceUserId')

class RequestedProjectInServicesAdmin(admin.ModelAdmin):
	list_display = ['projectService','externalProjectKey', 'externalProjectName']


class AvailableServiceAdmin(DjangoMpttAdmin):
	list_display=('availServiceDescription',)

class ResolutionAdmin(admin.ModelAdmin):
	list_display=('resolutionServiceID','resolutionNumber','resolutionDate','resolutionEstimatedDate','resolutionOnQueuedDate','resolutionOnInProgressDate','resolutionFullNumber','resolutionAsignedUser','resolutionNotes')

class ResolutionParametersAdmin(admin.ModelAdmin):
	list_display = ['resolution','resolutionParameter', 'resolutionParamValue','resolutionParamNotes']

class DeliveryAdmin(admin.ModelAdmin):
	list_display=('deliveryResolutionID','deliveryDate','deliveryNotes')

class PipelinesManager(admin.ModelAdmin):
	list_display = ['availableService', 'userName','pipelineName','pipelineVersion','pipelineInUse', 'externalRequest', 'useRunFolder','default']

class ParameterPipelineManager(admin.ModelAdmin):
	list_display = ['parameterPipeline', 'parameterName', 'parameterValue']

class JobStatesManager(admin.ModelAdmin):
	list_display = ['jobStateName']

class PipelineExternalDataJobsManager(admin.ModelAdmin):
	list_display = ['pipeline', 'availableService', 'serviceRequestNumber', 'folderData', 'jobState', 'lastRequestedTime', 'pipelineName', 'pipelineVersion']

admin.site.register(FileExt,FileExtAdmin)
admin.site.register(Platform,PlatformAdmin)
admin.site.register(Machines,MachinesAdmin)
admin.site.register(Service,ServiceAdmin)
admin.site.register(ResolutionParameters, ResolutionParametersAdmin)
admin.site.register(RequestedProjectInServices, RequestedProjectInServicesAdmin)

admin.site.register(AvailableService,AvailableServiceAdmin)
admin.site.register(Resolution,ResolutionAdmin)
admin.site.register(Delivery,DeliveryAdmin)

admin.site.register(Pipelines,PipelinesManager)
admin.site.register(ParameterPipeline,ParameterPipelineManager)

admin.site.register(JobStates,JobStatesManager)
admin.site.register(PipelineExternalDataJobs, PipelineExternalDataJobsManager)
