from bs4 import BeautifulSoup
from collections import deque
import requests
import re
import sys

# Starting URL should be first argument from sys
start_url = sys.argv[1]
if not start_url.startswith("http://"):
	start_url = "http://" + start_url 

q = deque([start_url])

urls_seen = set([])
emails = set([])

while q:
	url = q.popleft()
	urls_seen.add(url)

	# Allow redirecting only on start_url
	r = requests.get(url, allow_redirects = (url == start_url))

	soup = BeautifulSoup(r.text, 'html.parser')

	# Extract all email addresses and add them into the resulting set
	new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", r.text, re.I))
	emails.update(new_emails)

	# Iterate over all links found on the page
	for link in soup.find_all('a'):

		# It's possible to see 'a' elements without 'href'
		try:		
			new_url = link.attrs["href"]
		except:
			break

		# Truncate extraneous slashes
		if new_url.startswith("//"):
			new_url = new_url[2:]

		# Check if relative address is being used
		elif new_url.startswith("/"):
			new_url = start_url + new_url

		if not new_url.startswith("http://"):
			new_url = "http://" + new_url 

		# Ensure that we stay in one domain and don't search pdf files
		if new_url.startswith(start_url) and not "pdf" in new_url:
			if not new_url in urls_seen and not new_url in q:
				# print "Queuing", new_url 
				q.append(new_url)

print "Found these email addresses"

for email in emails:
	print email