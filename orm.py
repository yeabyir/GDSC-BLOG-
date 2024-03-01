import os
import django
from django.conf import settings
from django.utils import timezone
from BlogApp.models import Post
from CommentApp.models import Comment


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GDSCBlog.settings')
django.setup()


def post_operations():
    # Create posts
    post1 = Post.objects.create(title="Post 1", content="Content 1", category="Category 1", image="image1.jpg", tags=["tag1", "tag2"])
    post2 = Post.objects.create(title="Post 2", content="Content 2", category="Category 2", image="image2.png", tags=["tag3", "tag4"])
    post3 = Post.objects.create(title="Post 3", content="Content 3", category="Category 1", image="image3.png", tags=["tag5", "tag6"])

    # Query and display all posts in a specific category
    category_posts = Post.objects.filter(category="Category 1")
    print("Posts in Category 1:")
    for post in category_posts:
        print(post.title)

    return post1, post2, post3

def comment_operations(post1, post2, post3):
    # Create comments
    comment1 = Comment.objects.create(content="Comment 1", author="Author 1", published_date=timezone.now(), post=post1)
    comment2 = Comment.objects.create(content="Comment 2", author="Author 2", published_date=timezone.now(), post=post2)
    comment3 = Comment.objects.create(content="Comment 3", author="Author 3", published_date=timezone.now(), post=post3)

    # Query and display all comments related to a specific post
    post_comments = Comment.objects.filter(post=post1)
    print(f"Comments related to {post1.title}:")
    for comment in post_comments:
        print(comment.content)

if __name__ == "__main__":
    post1, post2, post3 = post_operations()
    comment_operations(post1, post2, post3)