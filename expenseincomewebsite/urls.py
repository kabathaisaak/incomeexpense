from django.urls import path, include

urlpatterns = [
   path('expanseincome/', include('expenseincomeapp.urls')),
   path('expenses', include('expense.urls')),
   path('userincome/', include('userincome.urls')),
   path('userpreferences/', include('userpreferences.urls')),
   path('', include('authentication.urls'))
]
