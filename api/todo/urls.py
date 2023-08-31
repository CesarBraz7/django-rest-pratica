from rest_framework import routers #routers dá rotas pré-prontas
from todo.views import TodoListViewset, PessoaViewSet

#função para acessar uma url
router = routers.DefaultRouter() #instanciando o DefaltRouter()
router.register(r'todo', TodoListViewset) #registra as rotas em TodoListViewset
router.register(r'pessoa', PessoaViewSet) #registra as rotas em PessoaViewSet
urlpatterns = router.urls #todas as urls do router vão para o urlpatterns