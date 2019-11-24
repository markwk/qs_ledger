# go to https://cloud.ouraring.com/oauth/applications and create an application
# you will be provided with client_id and client_secret put them to config.py
# put ""http://localhost:65010/oura_auth" to redirect uri field

REDIRECT_URI = "http://localhost:65010/oura_auth"

import os
os.environ["FLASK_ENV"] = "development"

# configuration
import json
with open("credentials.json", "r") as file:
    credentials = json.load(file)
    oura_cr = credentials['oura']
    CLIENT_SECRET = oura_cr['CLIENT_SECRET']
    CLIENT_ID = oura_cr['CLIENT_ID']


from flask import Flask, abort, request
app = Flask(__name__)
@app.route('/')
def homepage():
	text = '<a href="%s">Get access token!</a>'
	return text % make_authorization_url()

def make_authorization_url():
	# Generate a random string for the state parameter
	from uuid import uuid4
	state = str(uuid4())
	params = {"client_id": CLIENT_ID,
			  "response_type": "code",
			  "state": state,
			  "redirect_uri": REDIRECT_URI,
			  "duration": "temporary",
			  "scope": "email personal daily"} # all possible scopes
	import urllib
	url = "https://cloud.ouraring.com/oauth/authorize?" + urllib.parse.urlencode(params)
	return url

import requests
import requests.auth
def get_token(code):
	client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
	post_data = {"grant_type": "authorization_code",
				 "code": code,
				 "redirect_uri": REDIRECT_URI}
	response = requests.post("https://cloud.ouraring.com/oauth/token",
							 auth=client_auth,
							 data=post_data)
	token_json = response.json()
	return token_json["access_token"]

@app.route('/oura_auth')
def oura_redir():
	error = request.args.get('error', '')
	error = request.args.get('error_description', '')
	if error:
		return "Error: " + error
	state = request.args.get('state', '')
	code = request.args.get('code')

	return "got an access token! %s" % get_token(code)

if __name__ == '__main__':
	app.run(debug=True, port=65010)
