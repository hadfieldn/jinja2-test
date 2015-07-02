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

### Output
```
------------------------------------------
<!-- jshint ignore: start -->
<html>
<body style="color: black;">
  <style> img.emoji { width: 1em; height: 1em;} </style>
  <div style="max-width: 600px">
    <a href="http://worldtable.co"><img src="http://worldtable.co/images/twt-logo-email.png" width="72" height="29"/></a>
    <p>
    
      %fromname% <a href="[pagePermalink]#twtcommentid=[newCommentId]">%action% [pageTitle]</a>:
    
  </p>
  <div style="background-color: #eeeeee; padding: 6px 12px">
    
      <p>[newCommentContent]</p>
    
    
  </div>
  
  
    <p>&nbsp;</p>
    <p>&nbsp;</p>
    <p style="font-size: xx-small">
      To discontinue notifications from The World Table,
      send an e-mail to <a href="mailto:unsubscribe@worldtable.co?subject=Unsubscribe%20me%20please&body=Please%20discontinue%20notification%20e-mail%20to%20[origCommentUser.mail].%20Thanks.">unsubscribe@worldtable.co</a>.
    </p>
  </div>
</body>
</html>
------------------------------------------
%fromname% %action% [pageTitle]:

[newCommentContent]



View comment: [pagePermalink]#twtcommentid=[newCommentId]




To discontinue notifications from The World Table, send an e-mail to unsubscribe@worldtable.co

Process finished with exit code 0
```
