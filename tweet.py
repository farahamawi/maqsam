# tweet using python 
# you need to install tweepy https://www.tweepy.org/
import tweepy
# environment veriables
consumer_key = 'NWo8dlQbH3IEm6Q4y8drBf5iO'
consumer_secret = 'zjXITSU5mJPjAAYWyR1ggXfay42jGcMVXw0W2YRlc2Q4f87aP5'
access_token = '1198702473805996033-1CXGBHeQ0c8bIvWgblcmHQGr1W8j85'
access_token_secret = 'jTxb5MtB7sKAw8caqPt5eCf86N1urTHf824wVGFYRU3gv'

def OAuth(**kwargs):
	consumer_key = kwargs.get('consumer_key')
	consumer_secret = kwargs.get('consumer_secret')
	access_token = kwargs.get('access_token')
	access_token_secret = kwargs.get('access_token_secret')

	try:
		# Create an OAuthHandler instance. Into this we pass our consumer key and secret
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		return auth

	except Exception as e:
		return None

def tweet(oauth, body):
	api = tweepy.API(oauth)
	api.update_status(body)
	print('tweet is posted')


if __name__ == '__main__':

	oauth = OAuth(
		consumer_key=consumer_key, 
		consumer_secret=consumer_secret,
		access_token=access_token,
		access_token_secret=access_token_secret
	)

	tweet(oauth, 'Iam posting tweet using python')
