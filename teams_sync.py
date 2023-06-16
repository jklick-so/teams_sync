'''
This Python script is offered with no formal support. 
If you run into difficulties, reach out to the person who provided you with this script.

Documentation for using the Teams Sync API can be found here:
https://support.stackenterprise.co/support/solutions/articles/22000232700-team-membership-sync#syncing-team-membership-via-api-push-(2019.2-release-or-later)'''
import requests
import json


def post_teams_data(base_url, key, token, teams_data, dryrun=True):

    endpoint = base_url + '/api/2.3/enterprise/usersync'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-API-Access-Token': token,
        'X-API-Key': key
    }
    form_data = {
        "requestsJson": json.dumps(teams_data),
        'dryRun': dryrun
    }
    response = requests.post(endpoint, data=form_data, headers=headers)

    return json.loads(response.text)


def read_json(file_path):

    with open(file_path, 'r') as f:
        data = json.loads(f.read())

    return data


if __name__ == '__main__':

    # Change these variables to match your environment
    base_url = 'URL_TO_YOUR_STACKOVERFLOW_TEAMS_SITE' # e.g. 'https://subdomain.stackenterprise.co'
    key = 'YOUR_KEY'
    token = 'YOUR_TOKEN'
    json_path = 'PATH_TO_JSON_FILE' # e.g. 'teams_data.json'

    # Alternatively, you can directly assign the teams_data variable to a list of dictionaries
    teams_data = read_json(json_path)

    # Sample JSON structure for teams_data:
    # teams_data = [
    #     {
    #         "Team": "team-name",
    #         "Members": [
    #             {
    #                 "UserIdentifier": "value_for_user_identifier_SAML_assertion",
    #                 "Level": "Admin or Member"
    #             }
    #         ]
    #     }
    # ]

    # JSON structure documentation: 
    # https://support.stackenterprise.co/support/solutions/articles/22000232700-team-membership-sync#json-format

    # To test the API call without making any changes, set dryrun=True
    # Otherwise, set dryrun=False
    resp_data = post_teams_data(base_url, key, token, teams_data, dryrun=True)
    print(resp_data)
