# teams_sync
This is a sample, working script for leveraging the Teams Sync API for private teams in Stack Overflow Enterprise. This is based on the [official documentation](https://support.stackenterprise.co/support/solutions/articles/22000232700-team-membership-sync#syncing-team-membership-via-api-push-(2019.2-release-or-later)) for the Teams Sync API.

This Python script is to help others get started with writing their own API scripts and is offered with no formal support. 
If you run into difficulties, reach out to the person who provided you with this script.

## Requirements
* A Stack Overflow for Teams (Enterprise tier only)
* Python 3.x ([download](https://www.python.org/downloads/))
* Operating system: Linux, MacOS, or Windows

## Setup

[Download](https://github.com/jklick-so/teams_sync/archive/refs/heads/main.zip) and unpack the contents of this repository

**Installing Dependencies**

There's only a single dependency: the [Requests](https://pypi.org/project/requests/) library for Python. If you already have it installed, you can skip to API authentication.
* Open a terminal window (or, for Windows, a command prompt)
* Navigate to the directory where you unpacked the files
* Install the dependencies: `pip3 install -r requirements.txt`

**API Authentication**

You'll need to obtain an API key and an API token, both with write access.
Documentation for creating the key and token can be found within your instance, at this url: `https://[your_site]/api/docs/authentication`

Creating an access token for Enterpise can sometimes be tricky for people who haven't done it before. Here are some (hopefully) straightforward instructions:
* Go to the page where you created your API key. Take note of the "Client ID" associated with your API key.
* Go to the following URL, replacing the base URL, the `client_id`, and base URL of the `redirect_uri` with your own:
`https://YOUR.SO-ENTERPRISE.URL/oauth/dialog?client_id=111&scope=write_access&redirect_uri=https://YOUR.SO-ENTERPRISE.URL/oauth/login_success`
* You may be prompted to login to Stack Overflow Enterprise, if you're not already. Either way, you'll be redirected to a page that simply says "Authorizing Application"
* In the URL of that page, you'll find your access token. Example: `https://YOUR.SO-ENTERPRISE.URL/oauth/login_success#access_token=sRsbqFUEk7FW4c9N3zirWQ))`

## Usage
Before running the script, make sure to open the script and change the following variables to your own:
```
base_url = 'URL_TO_YOUR_STACKOVERFLOW_TEAMS_SITE'
key = 'YOUR_KEY'
token = 'YOUR_TOKEN'
json_path = 'PATH_TO_JSON_FILE'
```

