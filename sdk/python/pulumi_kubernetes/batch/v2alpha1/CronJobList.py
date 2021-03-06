import pulumi
import pulumi.runtime

from ... import tables

class CronJobList(pulumi.CustomResource):
    """
    CronJobList is a collection of cron jobs.
    """
    def __init__(self, __name__, __opts__=None, items=None, metadata=None):
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = 'batch/v2alpha1'
        __props__['kind'] = 'CronJobList'
        if items is None:
            raise TypeError('Missing required property items')
        __props__['items'] = items
        __props__['metadata'] = metadata

        super(CronJobList, self).__init__(
            "kubernetes:batch/v2alpha1:CronJobList",
            __name__,
            __props__,
            __opts__)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop
