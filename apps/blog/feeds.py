from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse_lazy
from apps.blog.models import Post


class LatestPostsFeed(Feed):
    title = 'dj-hyperbeam'
    link = reverse_lazy('blog:post-list')
    description = 'Recent post'

    def items(self):
        return Post.published.all()[:6]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)
