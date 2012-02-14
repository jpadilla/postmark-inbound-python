import re
import json
from base64 import b64decode


class PostmarkInbound(object):

    def __init__(self, **kwargs):
        if 'json' not in kwargs:
            raise Exception('Postmark Inbound Error: you must provide json data')
        self.json = kwargs['json']
        self.source = json.loads(self.json)

    def subject(self):
        return self.source['Subject']

    def from_name(self):
        re1 = '(".*?")'
        rg = re.compile(re1, re.IGNORECASE | re.DOTALL)
        m = rg.search(self.source['From'])
        if m:
            return m.group(1).replace('"', '')
        return ''

    def from_email(self):
        re1 = '([\\w+]+(?:\\.[\\w+]+)*@(?:[\\w]+\\.)+[a-zA-Z]{2,7})'
        rg = re.compile(re1, re.IGNORECASE | re.DOTALL)
        m = rg.search(self.source['From'])
        if m:
            return m.group(1)
        return ''

    def to(self):
        return self.source['To']

    def bcc(self):
        return self.source['Bcc']

    def cc(self):
        return self.source['Cc']

    def reply_to(self):
        return self.source['ReplyTo']

    def mailbox_hash(self):
        return self.source['MailboxHash']

    def tag(self):
        return self.source['Tag']

    def message_id(self):
        return self.source['MessageID']

    def text_body(self):
        return self.source['TextBody']

    def html_body(self):
        return self.source['HtmlBody']

    def spam(self, name='X-Spam-Status'):
        for header in self.source['Headers']:
            for key, value in header.iteritems():
                if key == name:
                    return value
        return False

    def headers(self, name='Date'):
        for header in self.source['Headers']:
            if header['Name'] == name:
                return header['Value']
        return None

    def attachments(self):
        attachments = []
        for attachment in self.source['Attachments']:
            attachments.append(Attachment(attachment))
        return attachments

    def has_attachments(self):
        if not self.attachments():
            return False
        return True


class Attachment(object):

    def __init__(self, attachment, **kwargs):
        self.attachment = attachment

    def name(self):
        return self.attachment['Name']

    def content_type(self):
        return self.attachment['ContentType']

    def content_length(self):
        return self.attachment['ContentLength']

    def read(self):
        return b64decode(self.attachment['Content'])

    def download(self, directory='', allowed_content_types=[], max_content_length=''):
        if len(directory) == 0:
            raise Exception('Postmark Inbound Error: you must provide the upload path')

        if len(max_content_length) > 0 and self.content_length() > max_content_length:
            raise Exception('Postmark Inbound Error: the file size is over %s' % max_content_length)

        if allowed_content_types and self.content_type() not in allowed_content_types:
            raise Exception('Postmark Inbound Ereror: the file type %s is not allowed' % self.content_type())

        try:
            attachment = open('%s%s' % (directory, self.name()), 'w')
            attachment.write(self.read())
        except IOError:
            raise Exception('Postmark Inbound Error: cannot save the file, check path and rights.')
        else:
            attachment.close()
