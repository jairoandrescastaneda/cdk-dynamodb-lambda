from aws_cdk import (
    core,
    aws_lambda as _lambda,
    aws_dynamodb as _dynamodb,
    aws_apigateway as _apigateway,
)


class MyProjectStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        my_user_table = _dynamodb.Table(
            self,
            "MyUserTable",
            partition_key=_dynamodb.Attribute(
                name="user_id", type=_dynamodb.AttributeType.STRING
            ),
        )

        user_lambda = _lambda.Function(
            self,
            "UserLambda",
            runtime=_lambda.Runtime.PYTHON_3_7,
            code=_lambda.Code.from_asset("myproject/lambda"),
            handler="user.handler",
        )

        user_lambda.add_environment("TABLE_NAME", my_user_table.table_name)
        user_api = _apigateway.LambdaRestApi(
            self, "UserApi", handler=user_lambda, proxy=False
        )
        user_items = user_api.root.add_resource("user")
        user_items.add_method("POST")

        my_user_table.grant_read_write_data(user_lambda)
