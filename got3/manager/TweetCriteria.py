class TweetCriteria:

	def __init__(self):
		self.maxTweets = 0

	def setUsername(self, username):
		self.username = username
		return self

    
	def setSince(self, since):
		self.since = since
		return self
	def setCite(self, cite):
		self.cite = cite
		return self
	def setUntil(self, until):
		self.until = until
		return self
	def getUntil(self):
		return self.until
	def setQuerySearch(self, querySearch):
		self.querySearch = querySearch
		return self

	def setMaxTweets(self, maxTweets):
		self.maxTweets = maxTweets
		return self

	def setLang(self, Lang):
		self.lang = Lang
		return self

	def setTopTweets(self, topTweets):
 		self.topTweets = topTweets
 		return self