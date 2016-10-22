### README

By: Will Long   
MRU: Oct 22 2016  

#### Usage

This email crawler takes a single argument in the form of a web address  

ex. ` python find_email_addresses.py web.mit.edu`

and then crawls all connected webpages whose URLs begin with `http://web.mit.edu`  

At each page, the crawler stores any email addresses that it finds, and when done, prints them to stdout.   

Note: Where applicable, addresses should begin with the “www” subdomain.  
ex. Use `www.google.com` instead of `google.com` 

#### Implementation

- `find_email_addresses.py` makes use of a Queue to track and store webpages that it finds 
-  It implements several naive address formatting checks to correctly provide valid web addresses to `request.get` including:
	- Checking if the webpage contains "pdf"
	- Appends "http://" if none is found at the beginning
	- Appends the argument URL if the link has a relative address (begins with "/")

#### Dependencies
`find_email_addresses.py` makes use of the following dependencies, all of which should come included with Python:
- BeautifulSoup (bs4)
- Collections (deque)
- Requests (requests)
- Regular Expressions (re)
- System (sys)

#### Contact

email: wlong@college.harvard.edu