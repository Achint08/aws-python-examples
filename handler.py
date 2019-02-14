import json
# import jwt


def hello(event, context):
    print "Hello"
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    # return {
    #     "message": "Go Serverless v1.0! Your function executed successfully!",
    #     "event": event
    # }

def generate_policy(principalId, effect, resource):
    """
    Functionality to generate policy to invoke API on based on response of Token authentication

    :param principalId: THe principal identifier of the policy

    :param effect: Whether to allow or deny the API Gateway execution service to invoke the specified API Method

    :param resource: The resource is the ARN of the incoming method request

    """
    policy = {
        'principalId': 'user',
        'policyDocument': {
            'Version': '2012-10-17',
            'Statement': [
                {
                    'Action': 'execute-api:Invoke',
                    'Effect': effect,
                    'Resource': resource

                }
            ]
        },
        'context': {
            'stringKey': '1'
        }
    }

    return policy


def auth(event, context):
    """
    Authorizer Function to authorize the endpoints with tokens from UMS
    Checkout https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html for more

    :param event: The event for API Gateway

    
    """
    authorization_token = event.get('authorizationToken')
    print authorization_token
    success = False
    
    # if not success:
    #     return generate_policy('user', 'Allow', event.get('methodArn'))
    
    return generate_policy('user', 'Allow', event.get('methodArn'))
