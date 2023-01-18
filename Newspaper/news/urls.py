from django.urls import path
from .views import (
   PostList, PostDetail, PostSearch, PostCreate, PostEdit, PostDelete,
ArtCreate, ArtEdit, ArtDelete,

)


urlpatterns = [
   path('', PostList.as_view(), name='news'),
   # pk — это первичный ключ новости, которая будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', PostDetail.as_view(), name='news_detail'),
   path('search/', PostSearch.as_view(), name='search'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('articles/create/', ArtCreate.as_view(), name='art_create'),
   path('articles/<int:pk>/edit/', ArtEdit.as_view(), name='art_edit'),
   path('articles/<int:pk>/delete/', ArtDelete.as_view(), name='art_delete'),
]