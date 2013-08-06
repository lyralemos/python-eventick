import requests

class Eventick(object):

	token = None
	isLogged = False
	apiUrl = 'www.eventick.com.br/api/v1/'
	apiUResponseFormat = '.json'
	https = True

	_user = None
	_pass = None

	def __init__(self,username,password):
		self._user = username
		self._pass = password

		try:
			self.token = self.request('tokens')['token']
			self.isLogged = True
		except IndexError:
			raise Exception('Authentication Falied')

	def events(self):
		return self.request('events')

	def event(self,id):
		events = self.request('events/%s' % id)
		try:
			return events['events'][0]
		except IndexError:
			raise Exception('Event not found')

	def attendees(self,event_id,after=False):
		params = {}
		if after:
			params['checked_after'] = after.strftime('%Y-%m-%dT%H:%M:%S-03:00')
		return self.request('events/%s/attendees' % event_id,params=params)

	def attendee(self,event_id,id):
		try:
			return self.request('events/%s/attendees/%s' % (event_id,id))['attendees'][0]
		except IndexError:
			raise Exception('Attendee not found')

	def checkin(self,event_id,code,time=None):
		params = {}
		if time is not None:
			params['checked_at'] = time.strftime('%Y-%m-%dT%H:%M:%S-03:00')

		return self.request('events/%s/attendees/%s' % (event_id,code),method='put',params=params)

	def request(self,type,**kwargs):
		url = self.getAPIUrl()
		format = self.apiUResponseFormat
		credentials = self.getCredentials()
		method = kwargs.get('method','get')
		params = kwargs.get('params',None)

		data = getattr(requests, method)('%s%s%s' % (url,type,format),auth=credentials,params=params)

		#data = requests.get('%s%s%s' % (url,type,format),auth=credentials,params=kwargs)
		if data.status_code == 200:
			return data.json()
		elif data.status_code == 204:
			return True
		return None

	def getAPIUrl(self):
		return 'https://' + self.apiUrl

	def getCredentials(self):
		if self.token:
			return (self.token,'')
		else:
			return (self.username,self.password)

	@property
	def username(self):
		return self._user

	@property
	def password(self):
		return self._pass
