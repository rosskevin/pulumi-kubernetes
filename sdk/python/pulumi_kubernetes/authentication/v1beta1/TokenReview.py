import pulumi
import pulumi.runtime

from ... import tables

class TokenReview(pulumi.CustomResource):
    """
    TokenReview attempts to authenticate a token to a known user. Note: TokenReview requests may be
    cached by the webhook token authenticator plugin in the kube-apiserver.
    """
    def __init__(self, __name__, __opts__=None, metadata=None, spec=None, status=None):
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['apiVersion'] = 'authentication.k8s.io/v1beta1'
        __props__['kind'] = 'TokenReview'
        if spec is None:
            raise TypeError('Missing required property spec')
        __props__['spec'] = spec
        __props__['metadata'] = metadata
        __props__['status'] = status

        super(TokenReview, self).__init__(
            "kubernetes:authentication.k8s.io/v1beta1:TokenReview",
            __name__,
            __props__,
            __opts__)

    def translate_output_property(self, prop: str) -> str:
        return tables._CASING_FORWARD_TABLE.get(prop) or prop

    def translate_input_property(self, prop: str) -> str:
        return tables._CASING_BACKWARD_TABLE.get(prop) or prop
