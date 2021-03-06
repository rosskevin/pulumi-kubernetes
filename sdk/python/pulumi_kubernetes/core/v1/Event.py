import pulumi
import pulumi.runtime

from ... import tables

class Event(pulumi.CustomResource):
    """
    Event is a report of an event somewhere in the cluster.
    """
    def __init__(self, __name__, __opts__=None, action=None, count=None, event_time=None, first_timestamp=None, involved_object=None, last_timestamp=None, message=None, metadata=None, reason=None, related=None, reporting_component=None, reporting_instance=None, series=None, source=None, type=None):
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = 'v1'
        __props__['kind'] = 'Event'
        if involved_object is None:
            raise TypeError('Missing required property involved_object')
        __props__['involvedObject'] = involved_object
        if metadata is None:
            raise TypeError('Missing required property metadata')
        __props__['metadata'] = metadata
        __props__['action'] = action
        __props__['count'] = count
        __props__['eventTime'] = event_time
        __props__['firstTimestamp'] = first_timestamp
        __props__['lastTimestamp'] = last_timestamp
        __props__['message'] = message
        __props__['reason'] = reason
        __props__['related'] = related
        __props__['reportingComponent'] = reporting_component
        __props__['reportingInstance'] = reporting_instance
        __props__['series'] = series
        __props__['source'] = source
        __props__['type'] = type

        super(Event, self).__init__(
            "kubernetes:core/v1:Event",
            __name__,
            __props__,
            __opts__)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop
