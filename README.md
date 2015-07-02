### Installation
```bash
pip3 install jinja2
```

### Usage
```bash
python3 jinja2-test.py
```

### Notes
The templates in this project include variables to be replaced by [SendGrid](https://github.com/sendgrid/sendgrid-python). E.g.:

```python
message = sendgrid.Mail()
message.addSubstitution('%%toname%%', args['origCommentUser']['fullName'])
message.addSubstitution('%%fromname%%', args['newCommentUser']['fullName'])
message.addSubstitution('%%postingtype%%', 'comment' if args['newComment']['replyToCommentId'] else 'article')
message.addSubstitution('%%action%%', 'replied to' if args['newComment']['content'] else 'rated')
```
