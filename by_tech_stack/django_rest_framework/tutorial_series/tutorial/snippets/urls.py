from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views_function_csrf_exempt,\
      views_function_api_view,\
      views_class_api_view,\
      views_class_mixins,\
      views_class_generics

'''
Possible Values for views_type:
    views_function_csrf_exempt
    views_function_api_view
    views_class_api_view
    views_class_mixins
    views_class_generics
'''

views_type = "views_class_generics"

if views_type == "views_function_csrf_exempt":
    urlpatterns = [
        path('snippets/', views_function_csrf_exempt.snippet_list),
        path('snippets/<int:pk>/', views_function_csrf_exempt.snippet_detail),
    ]

elif views_type == "views_function_api_view":
    urlpatterns = [
        path('snippets/', views_function_api_view.snippet_list),
        path('snippets/<int:pk>/', views_function_api_view.snippet_detail),
    ]

elif views_type == "views_class_api_view":
    urlpatterns = [
        path('snippets/', views_class_api_view.SnippetList.as_view()),
        path('snippets/<int:pk>/', views_class_api_view.SnippetDetail.as_view()),
    ]

elif views_type == "views_class_mixins":
    urlpatterns = [
        path('snippets/', views_class_mixins.SnippetList.as_view()),
        path('snippets/<int:pk>/', views_class_mixins.SnippetDetail.as_view()),
    ]

elif views_type == "views_class_generics":
    urlpatterns = [
        path('snippets/', views_class_generics.SnippetList.as_view()),
        path('snippets/<int:pk>/', views_class_generics.SnippetDetail.as_view()),

        path('users/', views_class_generics.UserList.as_view()),
        path('users/<int:pk>/', views_class_generics.UserDetail.as_view()),

        path('', views_class_generics.api_root),
        path('snippets/<int:pk>/highlight/', views_class_generics.SnippetHighlight.as_view()),
    ]

    urlpatterns = format_suffix_patterns([
    path('', views_class_generics.api_root),
    path('snippets/',
        views_class_generics.SnippetList.as_view(),
        name='snippet-list'),
    path('snippets/<int:pk>/',
        views_class_generics.SnippetDetail.as_view(),
        name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',
        views_class_generics.SnippetHighlight.as_view(),
        name='snippet-highlight'),
    path('users/',
        views_class_generics.UserList.as_view(),
        name='user-list'),
    path('users/<int:pk>/',
        views_class_generics.UserDetail.as_view(),
        name='user-detail')
])
