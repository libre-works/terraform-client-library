import os

from terraform_cloud_client import AuthenticatedClient
from terraform_cloud_client.api.organizations import list_workspaces, show_organization
from terraform_cloud_client.types import Response

token = os.environ['TFC_TOKEN']


# create an authenticated client -------------------------------------------------
client = AuthenticatedClient( 
            base_url = "https://app.terraform.io/api/v2",
            token = token,
            verify_ssl = True )


# recieve a response back using authenticated client ----------------------------- 
response: Response[list_workspaces] = list_workspaces.sync_detailed(
    client = client,
    organization_name = "ecp-shell-prod")

print(f"Result:  {str(response.content)}")
