POSTMARK INBOUND HOOK
=====================

This is a simple API wrapper for Postmark Inbound Hook (http://developer.postmarkapp.com/developer-inbound.html) in Python inspired by [jjaffeux](https://github.com/jjaffeux/) [PHP API wrapper](https://github.com/jjaffeux/postmark-inbound-php).


Usage
-----

``` python
from postmark import PostmarkInbound


# load json
json_data = open('./tests/fixtures/valid_http_post.json').read()
inbound = PostmarkInbound(json=json_data)

# content
inbound.from_name();
inbound.from_email();
inbound.to();
inbound.bcc();
inbound.tag();
inbound.message_id();
inbound.mailbox_hash();
inbound.reply_to();
inbound.html_body();
inbound.text_body();

# headers
inbound.headers();  //default to get Date
inbound.headers('MIME-Version');
inbound.headers('Received-SPF');

# attachments
inbound.has_attachments(); //boolean
attachments = inbound.attachments();

first_attachment = attachments[0];
first_attachment.name();

second_attachment = attachments[1];
second_attachment.content_length();

for a in attachments:
	a.name();
	a.content_type();
	a.content_length();
	a.download('./tests/', array('allowed_content_types' => 'image/png'), '10000');
}

# raw data
inbound.json
inbound.source
``` 

Bug tracker
-----------

Have a bug? Please create an issue here on GitHub!


Contributions
-------------

* Fork
* Write tests
* Write Code
* Pull request

Thanks for your help.


TODO
----

* Write more tests


Authors
-------

**José Padilla**

+ http://twitter.com/jpadilla_
+ http://github.com/jpadilla

License
---------------------

DON'T BE A DICK PUBLIC LICENSE