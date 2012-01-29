import os.path
import unittest
from postmark import PostmarkInbound


class PostmarkInboundTest(unittest.TestCase):

    def setUp(self):
        json_data = open('fixtures/valid_http_post.json').read()
        self.inbound = PostmarkInbound(json=json_data)

    def test_should_have_a_subject(self):
        assert 'Hi There' == self.inbound.subject()

    def test_should_have_a_bcc(self):
        assert 'FBI <hi@fbi.com>' == self.inbound.bcc()

    def test_should_have_a_cc(self):
        assert 'Your Mom <hithere@hotmail.com>' == self.inbound.cc()

    def test_should_have_a_reply_to(self):
        assert 'new-comment+sometoken@yeah.com' == self.inbound.reply_to()

    def test_should_have_a_mailbox_hash(self):
        assert 'moitoken' == self.inbound.mailbox_hash()

    def test_should_have_a_tag(self):
        assert 'yourit' == self.inbound.tag()

    def test_should_have_a_message_id(self):
        assert 'a8c1040e-db1c-4e18-ac79-bc5f64c7ce2c' == self.inbound.message_id()

    def test_should_be_from_someone(self):
        pass

    def test_should_pull_out_the_from_email(self):
        assert 'bob@bob.com' == self.inbound.from_email()

    def test_should_pull_out_the_from_name(self):
        assert 'Bob Bobson' == self.inbound.from_name()

    def test_should_have_a_html_body(self):
        assert '<p>We no speak americano</p>' == self.inbound.html_body()

    def test_should_have_a_text_body(self):
        assert '\nThis is awesome!\n\n' == self.inbound.text_body()

    def test_should_be_to_someone(self):
        assert 'api-hash@inbound.postmarkapp.com' == self.inbound.to()

    def test_default_header_should_have_date(self):
        assert 'Thu, 31 Mar 2011 12:01:17 -0400' == self.inbound.headers()

    def test_should_have_header_date(self):
        assert 'Thu, 31 Mar 2011 12:01:17 -0400' == self.inbound.headers('Date')

    def test_should_have_header_mime_version(self):
        assert '1.0' == self.inbound.headers('MIME-Version')

    def test_should_have_header_received_spf(self):
        assert 'None (no SPF record) identity=mailfrom; client-ip=209.85.212.52; helo=mail-vw0-f52.google.com; envelope-from=bob@bob.com; receiver=4e8d6dec234dd90018e7bfd2b5d79107@inbound.postmarkapp.com' == self.inbound.headers('Received-SPF')

    def test_should_have_two_attachments(self):
        assert 2 == len(self.inbound.attachments())

    def test_should_have_attachment(self):
        assert True == self.inbound.has_attachments()

    def test_attachment_should_have_content_length(self):
        for a in self.inbound.attachments():
            assert a.content_length() is not None

    def test_attachment_should_have_conent_type(self):
        for a in self.inbound.attachments():
            assert a.content_type() is not None

    def test_attachment_should_have_name(self):
        for a in self.inbound.attachments():
            assert a.name() is not None

    def test_attachment_should_download(self):
        for a in self.inbound.attachments():
            a.download('./')

        assert True == os.path.exists('./chart.png')
        assert True == os.path.exists('./chart2.png')

if __name__ == "__main__":
    unittest.main()
