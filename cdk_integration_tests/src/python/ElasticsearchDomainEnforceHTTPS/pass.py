from aws_cdk import core
from aws_cdk import aws_elasticsearch as elasticsearch

class ElasticsearchStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an Amazon Elasticsearch domain
        elasticsearch_domain = elasticsearch.CfnDomain(
            self, "MyElasticsearchDomain",
            domain_name="my-elasticsearch-domain",
            elasticsearch_version="7.10",
            node_to_node_encryption_options={
                "enabled": True
            },
            domain_endpoint_options=elasticsearch.CfnDomain.DomainEndpointOptionsProperty(
                custom_endpoint="customEndpoint",
                custom_endpoint_certificate_arn="customEndpointCertificateArn",
                custom_endpoint_enabled=False,
                enforce_https=True,
                tls_security_policy="tlsSecurityPolicy"
            ),
            ebs_options={
                "ebsEnabled": True,
                "volumeSize": 10
            },
        )

# Create the CDK app and stack
app = core.App()
ElasticsearchStack(app, "ElasticsearchStack")
app.synth()
