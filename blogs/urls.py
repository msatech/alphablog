
from django.urls import path, include
from blogs import views
urlpatterns = [
    
    path('blog/', views.Blog, name="blog"),
    path('newhome/', views.NewHome, name="newhome"),

    path('blog/', views.Blog, name="search"),
    path('autocomplete/', views.Autocomplete, name="autocomplete"),

    path('single-post/<slug:slug>/', views.Single_Post, name="single-post"),
    path('post-comment/<slug:slug>/', views.CommentSave, name="comment-save"),
    path('comment-delete/<slug:slug>/<int:id>/', views.CommentDelete, name="comment-delete"),
    path('reply-comment-delete/<slug:slug>/<int:id>/', views.ReplyCommentDelete, name="reply-comment-delete"),

    path('comment-reply/<slug:slug>/<str:user>/<int:id>/', views.ReplyComment, name="comment-reply"),
    path('blog/<str:blogcategory>/', views.CategoryWiseBlog, name="category-wise-blog"),



]
