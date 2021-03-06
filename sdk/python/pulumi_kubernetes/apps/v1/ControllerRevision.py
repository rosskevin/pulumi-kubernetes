import pulumi
import pulumi.runtime

from ... import tables

class ControllerRevision(pulumi.CustomResource):
    """
    ControllerRevision implements an immutable snapshot of state data. Clients are responsible for
    serializing and deserializing the objects that contain their internal state. Once a
    ControllerRevision has been successfully created, it can not be updated. The API Server will
    fail validation of all requests that attempt to mutate the Data field. ControllerRevisions may,
    however, be deleted. Note that, due to its use by both the DaemonSet and StatefulSet controllers
    for update and rollback, this object is beta. However, it may be subject to name and
    representation changes in future releases, and clients should not depend on its stability. It is
    primarily for internal use by controllers.
    """
    def __init__(self, __name__, __opts__=None, data=None, metadata=None, revision=None):
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = 'apps/v1'
        __props__['kind'] = 'ControllerRevision'
        if revision is None:
            raise TypeError('Missing required property revision')
        __props__['revision'] = revision
        __props__['data'] = data
        __props__['metadata'] = metadata

        super(ControllerRevision, self).__init__(
            "kubernetes:apps/v1:ControllerRevision",
            __name__,
            __props__,
            __opts__)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop
