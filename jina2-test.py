from jinja2 import Environment, FileSystemLoader

class NotificationTemplates:

    def __init__(self):
        env = Environment(loader=FileSystemLoader("templates"))
        self.html_template = env.get_template("notification-email.html")
        self.text_template = env.get_template("notification-email.txt")

    def _params_from_args(self, args):
        page_permalink = '[pagePermalink]'
        is_page_comment = True
        params = {
            'page': args['page'],
            'pagePermalink': page_permalink,
            'isPageComment': is_page_comment,
            'newCommentUser': args['newCommentUser'],
            'newComment': args['newComment'],
            'newCommentPermalink': page_permalink + '#twtcommentid=' + args['newComment']['commentId'],
            'ratings': [{'label': 'honest', 'value': 65},  {'label': 'helpful', 'value': 85}],
            'origCommentUser': args['origCommentUser'],
            'origComment': args['origComment'],
            'origCommentPermalink': page_permalink + '#twtcommentid=' + args['origComment']['commentId'],
            'to': args['origCommentUser']['email'],
        }
        return params

    def get_html(self, args):
        return self.html_template.render(self._params_from_args(args))

    def get_text(self, args):
        return self.text_template.render(self._params_from_args(args))

templates = NotificationTemplates()
args = {
    'page': {'title': '[pageTitle]'},
    'newCommentUser': {},
    'newComment': {'content': '[newCommentContent]', 'commentId': '[newCommentId]', 'rating': {}},
    'origComment': {'commentId': '[origCommentId]'},
    'origCommentUser': {'email': '[origCommentUser.mail]', 'score': {'overall': 600}},
}

print("------------------------------------------")
print(templates.get_html(args))
print("------------------------------------------")
print(templates.get_text(args))

