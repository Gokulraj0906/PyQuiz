from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home, name= 'home'),
    path('signup',views.signup ,name='signup'),
    path('chemistry/chapters/level/medium/<int:id>', views.chemistry_medium),
    path('chemistry/chapters/level/easy/<int:id>', views.chemistry_easy),
    path('chemistry/chapters/level/hard/<int:id>', views.chemistry_hard),
    path('maths/chapters/level/medium/<int:id>', views.mathematics_medium),
    path('maths/chapters/level/easy/<int:id>', views.mathematics_easy),
    path('maths/chapters/level/hard/<int:id>', views.mathematics_hard),
    path('physics/chapters/level/medium/<int:id>', views.physics_medium),
    path('physics/chapters/level/hard/<int:id>', views.physics_hard),
    path('physics/chapters/level/easy/<int:id>', views.physics_easy),
    path('', views.login_in, name='login'),
    path('logout', views.log_out, name='logout'),
    path('chemistry/chapters', views.chemistry_chapters, name='chemistry_chapters'),
    path('chemistry/chapters/level/<int:id>', views.chemistry_level, name='chemistry_level'),
    path('maths/chapters', views.maths_chapters, name='maths_chapters'),
    path('maths/chapters/level/<int:id>', views.maths_level, name='maths_chapters'),
    path('physics/chapters', views.physics_chapters, name='physics_chapters'),
    path('physics/chapters/level/<int:id>', views.physics_level, name='physics_chapters'),
    path('chemistry_easy_result', views.chemistry_easy_result, name='chemistry_easy_result'),
    path('chemistry_medium_result', views.chemistry_medium_result, name='chemistry_medium_result'),
    path('chemistry_hard_result', views.chemistry_hard_result, name='chemistry_hard_result'),
    path('maths_easy_result', views.maths_easy_result, name='maths_easy_result'),
    path('maths_medium_result', views.maths_medium_result, name='maths_medium_result'),
    path('maths_hard_result', views.maths_hard_result, name='maths_hard_result'),
    path('physics_easy_result', views.physics_easy_result, name='physics_easy_result'),
    path('physics_medium_result', views.physics_medium_result, name='physics_medium_result'),
    path('physics_hard_result', views.physics_hard_result, name='physics_hard_result'),
    path('progress', views.progress, name='progress'),
]