from django.shortcuts import render

# Create your views here.
from django.views import generic
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json, requests

from django.http.response import HttpResponse
# Create your views here.
class ngothabotView(generic.View):
	def get(self, request, *args, **kwargs):
	    if self.request.GET['hub.verify_token'] == '9962478798':
	    	return HttpResponse(self.request.GET['hub.challenge'])
	    else:
	    	return HttpResponse('Error, invalid token')

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
	    return generic.View.dispatch(self, request, *args, **kwargs)

	# Post function to handle Facebook messages
	def post(self, request, *args, **kwargs):
	    # Converts the text payload into a python dictionary
	    incoming_message = json.loads(self.request.body)
	    # Facebook recommends going through every entry since they might send
	    # multiple messages in a single call during high load
	    for entry in incoming_message['entry']:
	        for message in entry['messaging']:
	            # Check to make sure the received call is a message call
	            # This might be delivery, optin, postback for other events 
	            if message.has_key('message'):
	                # Print the message to the terminal
	                print(message)     
	    		post_facebook_message(message['sender']['id'], message['message']['text'])



def post_facebook_message(fbid, recevied_message):           
    post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=EAAZAWpNqQ9p4BAMuiug1gGYGiZA6lMsxurbkwTvpRvQ06ZBUsK2SpJa9x3aGYtHvoKsVGWxLHwX7szhPvGJURBqXtpIt2fkxPbzrZCHEKzFJUKUmaxRWjCdMoL93xHe1DCEZBcwoeqlfjinDx8Ji8Jctn4sbWH22e30PPXsjkyQZDZD'
    response_msg = json.dumps({"recipient":{"id":fbid}, "message":{"text":"adingothaaa"}})
    status = requests.post(post_message_url, headers={"Content-Type": "application/json"},data=response_msg)
    print(status.json())

