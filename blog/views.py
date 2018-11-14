from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.utils import timezone
from .models import Post, PostComment
from .forms import BlogPostForm, PostCommentForm


def donor_check(user):
    """
    User needs to be logged in and a donor to use Blog
    """
    if user.is_authenticated and user.profile.is_donor == 1:
        return 1


@user_passes_test(donor_check, login_url='/accounts/login/')
def get_posts(request):
    """
    Create a view taht will return a list
    of Posts that were published prior to 'now'
    and render them to the blogposts.html template
    """
    posts = Post.objects.filter(published_date__lte=timezone.now
                                ()).order_by('-published_date')
    return render(request, "blogposts.html", {'posts': posts})


@user_passes_test(donor_check, login_url='/accounts/login/')
def post_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and 
    render it to the postdetail.html template
    or return a 404 error if ppost is not found
    """

    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    postcomments = PostComment.objects.filter(
        post_id=pk, created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, "postdetail.html", {'post': post, 'postcomments': postcomments})


@user_passes_test(donor_check, login_url='/accounts/login/')
def create_or_edit_post(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """

    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        if "cancel" in request.POST:
            if not pk:
                return redirect(get_posts)
            else:
                return redirect(post_detail, pk)
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})


@user_passes_test(donor_check, login_url='/accounts/login/')
def create_post_comment(request, pk):
    """
    Comment post comment
    """
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        if "cancel" in request.POST:
            return redirect(post_detail, pk=pk)
        form = PostCommentForm(request.POST)
        if form.is_valid():
            postcomment = form.save(commit=False)
            postcomment.author = request.user
            postcomment.post = post
            postcomment.save()
            return redirect(post_detail, post.pk)
    else:
        form = PostCommentForm()
    return render(request, "postcommentform.html", {'post': post, 'comment_form': form})


@user_passes_test(donor_check, login_url='/accounts/login/')
def blogpost_comment_report(request, pk):
    """
    Create a view taht will return a list
    of Bugs that were published prior to 'now'
    and render them to the bugs.html template
    """
    comment = get_object_or_404(PostComment, pk=pk)
    print(comment.comment)
    print(comment.is_reported)

    comment.is_reported = True
    comment.save()
    return redirect(post_detail, comment.post.id)
