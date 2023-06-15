import os
import json

from terraform_cloud_client import AuthenticatedClient
from terraform_cloud_client.api.organizations import list_workspaces

token = os.environ['TFC_TOKEN']
organization = "****"

# create an authenticated client -------------------------------------------------
client = AuthenticatedClient( 
            base_url = "https://app.terraform.io/api/v2",
            token = token,
            verify_ssl = True )


# recieve a response back using authenticated client ----------------------------- 
response = list_workspaces.sync_detailed(
    client = client,
    organization_name = organization )

data = json.loads(response.content)
total_count = data['meta']['pagination']['total-count']


# iterate thtough each page --------------------------------------------------
for page in range(1, total_count):   
    response = list_workspaces.sync_detailed(
        client = client,
        organization_name = organization,
        pagenumber = page )

    data = json.loads(response.content)
    current_page = data['meta']['pagination']['current-page']

    print(f"Current Page is:  {current_page}")