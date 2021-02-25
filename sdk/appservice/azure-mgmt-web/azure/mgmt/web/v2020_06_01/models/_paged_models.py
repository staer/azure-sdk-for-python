# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.paging import Paged


class AppServiceCertificateOrderPaged(Paged):
    """
    A paging container for iterating over a list of :class:`AppServiceCertificateOrder <azure.mgmt.web.v2020_06_01.models.AppServiceCertificateOrder>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AppServiceCertificateOrder]'}
    }

    def __init__(self, *args, **kwargs):

        super(AppServiceCertificateOrderPaged, self).__init__(*args, **kwargs)
class AppServiceCertificateResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`AppServiceCertificateResource <azure.mgmt.web.v2020_06_01.models.AppServiceCertificateResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AppServiceCertificateResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(AppServiceCertificateResourcePaged, self).__init__(*args, **kwargs)
class CsmOperationDescriptionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`CsmOperationDescription <azure.mgmt.web.v2020_06_01.models.CsmOperationDescription>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[CsmOperationDescription]'}
    }

    def __init__(self, *args, **kwargs):

        super(CsmOperationDescriptionPaged, self).__init__(*args, **kwargs)
class DomainPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Domain <azure.mgmt.web.v2020_06_01.models.Domain>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Domain]'}
    }

    def __init__(self, *args, **kwargs):

        super(DomainPaged, self).__init__(*args, **kwargs)
class NameIdentifierPaged(Paged):
    """
    A paging container for iterating over a list of :class:`NameIdentifier <azure.mgmt.web.v2020_06_01.models.NameIdentifier>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[NameIdentifier]'}
    }

    def __init__(self, *args, **kwargs):

        super(NameIdentifierPaged, self).__init__(*args, **kwargs)
class DomainOwnershipIdentifierPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DomainOwnershipIdentifier <azure.mgmt.web.v2020_06_01.models.DomainOwnershipIdentifier>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DomainOwnershipIdentifier]'}
    }

    def __init__(self, *args, **kwargs):

        super(DomainOwnershipIdentifierPaged, self).__init__(*args, **kwargs)
class TopLevelDomainPaged(Paged):
    """
    A paging container for iterating over a list of :class:`TopLevelDomain <azure.mgmt.web.v2020_06_01.models.TopLevelDomain>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[TopLevelDomain]'}
    }

    def __init__(self, *args, **kwargs):

        super(TopLevelDomainPaged, self).__init__(*args, **kwargs)
class TldLegalAgreementPaged(Paged):
    """
    A paging container for iterating over a list of :class:`TldLegalAgreement <azure.mgmt.web.v2020_06_01.models.TldLegalAgreement>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[TldLegalAgreement]'}
    }

    def __init__(self, *args, **kwargs):

        super(TldLegalAgreementPaged, self).__init__(*args, **kwargs)
class CertificatePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Certificate <azure.mgmt.web.v2020_06_01.models.Certificate>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Certificate]'}
    }

    def __init__(self, *args, **kwargs):

        super(CertificatePaged, self).__init__(*args, **kwargs)
class DeletedSitePaged(Paged):
    """
    A paging container for iterating over a list of :class:`DeletedSite <azure.mgmt.web.v2020_06_01.models.DeletedSite>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DeletedSite]'}
    }

    def __init__(self, *args, **kwargs):

        super(DeletedSitePaged, self).__init__(*args, **kwargs)
class DetectorResponsePaged(Paged):
    """
    A paging container for iterating over a list of :class:`DetectorResponse <azure.mgmt.web.v2020_06_01.models.DetectorResponse>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DetectorResponse]'}
    }

    def __init__(self, *args, **kwargs):

        super(DetectorResponsePaged, self).__init__(*args, **kwargs)
class DiagnosticCategoryPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DiagnosticCategory <azure.mgmt.web.v2020_06_01.models.DiagnosticCategory>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DiagnosticCategory]'}
    }

    def __init__(self, *args, **kwargs):

        super(DiagnosticCategoryPaged, self).__init__(*args, **kwargs)
class AnalysisDefinitionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`AnalysisDefinition <azure.mgmt.web.v2020_06_01.models.AnalysisDefinition>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AnalysisDefinition]'}
    }

    def __init__(self, *args, **kwargs):

        super(AnalysisDefinitionPaged, self).__init__(*args, **kwargs)
class DetectorDefinitionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`DetectorDefinition <azure.mgmt.web.v2020_06_01.models.DetectorDefinition>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[DetectorDefinition]'}
    }

    def __init__(self, *args, **kwargs):

        super(DetectorDefinitionPaged, self).__init__(*args, **kwargs)
class ApplicationStackResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`ApplicationStackResource <azure.mgmt.web.v2020_06_01.models.ApplicationStackResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ApplicationStackResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(ApplicationStackResourcePaged, self).__init__(*args, **kwargs)
class RecommendationPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Recommendation <azure.mgmt.web.v2020_06_01.models.Recommendation>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Recommendation]'}
    }

    def __init__(self, *args, **kwargs):

        super(RecommendationPaged, self).__init__(*args, **kwargs)
class SourceControlPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SourceControl <azure.mgmt.web.v2020_06_01.models.SourceControl>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SourceControl]'}
    }

    def __init__(self, *args, **kwargs):

        super(SourceControlPaged, self).__init__(*args, **kwargs)
class BillingMeterPaged(Paged):
    """
    A paging container for iterating over a list of :class:`BillingMeter <azure.mgmt.web.v2020_06_01.models.BillingMeter>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[BillingMeter]'}
    }

    def __init__(self, *args, **kwargs):

        super(BillingMeterPaged, self).__init__(*args, **kwargs)
class GeoRegionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`GeoRegion <azure.mgmt.web.v2020_06_01.models.GeoRegion>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[GeoRegion]'}
    }

    def __init__(self, *args, **kwargs):

        super(GeoRegionPaged, self).__init__(*args, **kwargs)
class IdentifierPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Identifier <azure.mgmt.web.v2020_06_01.models.Identifier>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Identifier]'}
    }

    def __init__(self, *args, **kwargs):

        super(IdentifierPaged, self).__init__(*args, **kwargs)
class PremierAddOnOfferPaged(Paged):
    """
    A paging container for iterating over a list of :class:`PremierAddOnOffer <azure.mgmt.web.v2020_06_01.models.PremierAddOnOffer>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PremierAddOnOffer]'}
    }

    def __init__(self, *args, **kwargs):

        super(PremierAddOnOfferPaged, self).__init__(*args, **kwargs)
class SitePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Site <azure.mgmt.web.v2020_06_01.models.Site>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Site]'}
    }

    def __init__(self, *args, **kwargs):

        super(SitePaged, self).__init__(*args, **kwargs)
class BackupItemPaged(Paged):
    """
    A paging container for iterating over a list of :class:`BackupItem <azure.mgmt.web.v2020_06_01.models.BackupItem>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[BackupItem]'}
    }

    def __init__(self, *args, **kwargs):

        super(BackupItemPaged, self).__init__(*args, **kwargs)
class SiteConfigResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`SiteConfigResource <azure.mgmt.web.v2020_06_01.models.SiteConfigResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SiteConfigResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(SiteConfigResourcePaged, self).__init__(*args, **kwargs)
class SiteConfigurationSnapshotInfoPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SiteConfigurationSnapshotInfo <azure.mgmt.web.v2020_06_01.models.SiteConfigurationSnapshotInfo>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SiteConfigurationSnapshotInfo]'}
    }

    def __init__(self, *args, **kwargs):

        super(SiteConfigurationSnapshotInfoPaged, self).__init__(*args, **kwargs)
class ContinuousWebJobPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ContinuousWebJob <azure.mgmt.web.v2020_06_01.models.ContinuousWebJob>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ContinuousWebJob]'}
    }

    def __init__(self, *args, **kwargs):

        super(ContinuousWebJobPaged, self).__init__(*args, **kwargs)
class DeploymentPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Deployment <azure.mgmt.web.v2020_06_01.models.Deployment>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Deployment]'}
    }

    def __init__(self, *args, **kwargs):

        super(DeploymentPaged, self).__init__(*args, **kwargs)
class FunctionEnvelopePaged(Paged):
    """
    A paging container for iterating over a list of :class:`FunctionEnvelope <azure.mgmt.web.v2020_06_01.models.FunctionEnvelope>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[FunctionEnvelope]'}
    }

    def __init__(self, *args, **kwargs):

        super(FunctionEnvelopePaged, self).__init__(*args, **kwargs)
class HostNameBindingPaged(Paged):
    """
    A paging container for iterating over a list of :class:`HostNameBinding <azure.mgmt.web.v2020_06_01.models.HostNameBinding>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[HostNameBinding]'}
    }

    def __init__(self, *args, **kwargs):

        super(HostNameBindingPaged, self).__init__(*args, **kwargs)
class WebSiteInstanceStatusPaged(Paged):
    """
    A paging container for iterating over a list of :class:`WebSiteInstanceStatus <azure.mgmt.web.v2020_06_01.models.WebSiteInstanceStatus>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[WebSiteInstanceStatus]'}
    }

    def __init__(self, *args, **kwargs):

        super(WebSiteInstanceStatusPaged, self).__init__(*args, **kwargs)
class ProcessInfoPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ProcessInfo <azure.mgmt.web.v2020_06_01.models.ProcessInfo>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ProcessInfo]'}
    }

    def __init__(self, *args, **kwargs):

        super(ProcessInfoPaged, self).__init__(*args, **kwargs)
class ProcessModuleInfoPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ProcessModuleInfo <azure.mgmt.web.v2020_06_01.models.ProcessModuleInfo>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ProcessModuleInfo]'}
    }

    def __init__(self, *args, **kwargs):

        super(ProcessModuleInfoPaged, self).__init__(*args, **kwargs)
class ProcessThreadInfoPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ProcessThreadInfo <azure.mgmt.web.v2020_06_01.models.ProcessThreadInfo>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ProcessThreadInfo]'}
    }

    def __init__(self, *args, **kwargs):

        super(ProcessThreadInfoPaged, self).__init__(*args, **kwargs)
class PerfMonResponsePaged(Paged):
    """
    A paging container for iterating over a list of :class:`PerfMonResponse <azure.mgmt.web.v2020_06_01.models.PerfMonResponse>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PerfMonResponse]'}
    }

    def __init__(self, *args, **kwargs):

        super(PerfMonResponsePaged, self).__init__(*args, **kwargs)
class PublicCertificatePaged(Paged):
    """
    A paging container for iterating over a list of :class:`PublicCertificate <azure.mgmt.web.v2020_06_01.models.PublicCertificate>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[PublicCertificate]'}
    }

    def __init__(self, *args, **kwargs):

        super(PublicCertificatePaged, self).__init__(*args, **kwargs)
class SiteExtensionInfoPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SiteExtensionInfo <azure.mgmt.web.v2020_06_01.models.SiteExtensionInfo>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SiteExtensionInfo]'}
    }

    def __init__(self, *args, **kwargs):

        super(SiteExtensionInfoPaged, self).__init__(*args, **kwargs)
class SlotDifferencePaged(Paged):
    """
    A paging container for iterating over a list of :class:`SlotDifference <azure.mgmt.web.v2020_06_01.models.SlotDifference>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SlotDifference]'}
    }

    def __init__(self, *args, **kwargs):

        super(SlotDifferencePaged, self).__init__(*args, **kwargs)
class SnapshotPaged(Paged):
    """
    A paging container for iterating over a list of :class:`Snapshot <azure.mgmt.web.v2020_06_01.models.Snapshot>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Snapshot]'}
    }

    def __init__(self, *args, **kwargs):

        super(SnapshotPaged, self).__init__(*args, **kwargs)
class TriggeredWebJobPaged(Paged):
    """
    A paging container for iterating over a list of :class:`TriggeredWebJob <azure.mgmt.web.v2020_06_01.models.TriggeredWebJob>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[TriggeredWebJob]'}
    }

    def __init__(self, *args, **kwargs):

        super(TriggeredWebJobPaged, self).__init__(*args, **kwargs)
class TriggeredJobHistoryPaged(Paged):
    """
    A paging container for iterating over a list of :class:`TriggeredJobHistory <azure.mgmt.web.v2020_06_01.models.TriggeredJobHistory>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[TriggeredJobHistory]'}
    }

    def __init__(self, *args, **kwargs):

        super(TriggeredJobHistoryPaged, self).__init__(*args, **kwargs)
class CsmUsageQuotaPaged(Paged):
    """
    A paging container for iterating over a list of :class:`CsmUsageQuota <azure.mgmt.web.v2020_06_01.models.CsmUsageQuota>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[CsmUsageQuota]'}
    }

    def __init__(self, *args, **kwargs):

        super(CsmUsageQuotaPaged, self).__init__(*args, **kwargs)
class WebJobPaged(Paged):
    """
    A paging container for iterating over a list of :class:`WebJob <azure.mgmt.web.v2020_06_01.models.WebJob>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[WebJob]'}
    }

    def __init__(self, *args, **kwargs):

        super(WebJobPaged, self).__init__(*args, **kwargs)
class StaticSiteARMResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`StaticSiteARMResource <azure.mgmt.web.v2020_06_01.models.StaticSiteARMResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[StaticSiteARMResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(StaticSiteARMResourcePaged, self).__init__(*args, **kwargs)
class StaticSiteUserARMResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`StaticSiteUserARMResource <azure.mgmt.web.v2020_06_01.models.StaticSiteUserARMResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[StaticSiteUserARMResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(StaticSiteUserARMResourcePaged, self).__init__(*args, **kwargs)
class StaticSiteBuildARMResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`StaticSiteBuildARMResource <azure.mgmt.web.v2020_06_01.models.StaticSiteBuildARMResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[StaticSiteBuildARMResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(StaticSiteBuildARMResourcePaged, self).__init__(*args, **kwargs)
class StaticSiteFunctionOverviewARMResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`StaticSiteFunctionOverviewARMResource <azure.mgmt.web.v2020_06_01.models.StaticSiteFunctionOverviewARMResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[StaticSiteFunctionOverviewARMResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(StaticSiteFunctionOverviewARMResourcePaged, self).__init__(*args, **kwargs)
class StaticSiteCustomDomainOverviewARMResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`StaticSiteCustomDomainOverviewARMResource <azure.mgmt.web.v2020_06_01.models.StaticSiteCustomDomainOverviewARMResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[StaticSiteCustomDomainOverviewARMResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(StaticSiteCustomDomainOverviewARMResourcePaged, self).__init__(*args, **kwargs)
class AppServiceEnvironmentResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`AppServiceEnvironmentResource <azure.mgmt.web.v2020_06_01.models.AppServiceEnvironmentResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AppServiceEnvironmentResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(AppServiceEnvironmentResourcePaged, self).__init__(*args, **kwargs)
class StampCapacityPaged(Paged):
    """
    A paging container for iterating over a list of :class:`StampCapacity <azure.mgmt.web.v2020_06_01.models.StampCapacity>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[StampCapacity]'}
    }

    def __init__(self, *args, **kwargs):

        super(StampCapacityPaged, self).__init__(*args, **kwargs)
class InboundEnvironmentEndpointPaged(Paged):
    """
    A paging container for iterating over a list of :class:`InboundEnvironmentEndpoint <azure.mgmt.web.v2020_06_01.models.InboundEnvironmentEndpoint>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[InboundEnvironmentEndpoint]'}
    }

    def __init__(self, *args, **kwargs):

        super(InboundEnvironmentEndpointPaged, self).__init__(*args, **kwargs)
class WorkerPoolResourcePaged(Paged):
    """
    A paging container for iterating over a list of :class:`WorkerPoolResource <azure.mgmt.web.v2020_06_01.models.WorkerPoolResource>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[WorkerPoolResource]'}
    }

    def __init__(self, *args, **kwargs):

        super(WorkerPoolResourcePaged, self).__init__(*args, **kwargs)
class ResourceMetricDefinitionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ResourceMetricDefinition <azure.mgmt.web.v2020_06_01.models.ResourceMetricDefinition>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ResourceMetricDefinition]'}
    }

    def __init__(self, *args, **kwargs):

        super(ResourceMetricDefinitionPaged, self).__init__(*args, **kwargs)
class SkuInfoPaged(Paged):
    """
    A paging container for iterating over a list of :class:`SkuInfo <azure.mgmt.web.v2020_06_01.models.SkuInfo>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[SkuInfo]'}
    }

    def __init__(self, *args, **kwargs):

        super(SkuInfoPaged, self).__init__(*args, **kwargs)
class UsagePaged(Paged):
    """
    A paging container for iterating over a list of :class:`Usage <azure.mgmt.web.v2020_06_01.models.Usage>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[Usage]'}
    }

    def __init__(self, *args, **kwargs):

        super(UsagePaged, self).__init__(*args, **kwargs)
class OutboundEnvironmentEndpointPaged(Paged):
    """
    A paging container for iterating over a list of :class:`OutboundEnvironmentEndpoint <azure.mgmt.web.v2020_06_01.models.OutboundEnvironmentEndpoint>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[OutboundEnvironmentEndpoint]'}
    }

    def __init__(self, *args, **kwargs):

        super(OutboundEnvironmentEndpointPaged, self).__init__(*args, **kwargs)
class AppServicePlanPaged(Paged):
    """
    A paging container for iterating over a list of :class:`AppServicePlan <azure.mgmt.web.v2020_06_01.models.AppServicePlan>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[AppServicePlan]'}
    }

    def __init__(self, *args, **kwargs):

        super(AppServicePlanPaged, self).__init__(*args, **kwargs)
class StrPaged(Paged):
    """
    A paging container for iterating over a list of str object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[str]'}
    }

    def __init__(self, *args, **kwargs):

        super(StrPaged, self).__init__(*args, **kwargs)
class HybridConnectionPaged(Paged):
    """
    A paging container for iterating over a list of :class:`HybridConnection <azure.mgmt.web.v2020_06_01.models.HybridConnection>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[HybridConnection]'}
    }

    def __init__(self, *args, **kwargs):

        super(HybridConnectionPaged, self).__init__(*args, **kwargs)
class ResourceHealthMetadataPaged(Paged):
    """
    A paging container for iterating over a list of :class:`ResourceHealthMetadata <azure.mgmt.web.v2020_06_01.models.ResourceHealthMetadata>` object
    """

    _attribute_map = {
        'next_link': {'key': 'nextLink', 'type': 'str'},
        'current_page': {'key': 'value', 'type': '[ResourceHealthMetadata]'}
    }

    def __init__(self, *args, **kwargs):

        super(ResourceHealthMetadataPaged, self).__init__(*args, **kwargs)
