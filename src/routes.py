from src.controlls.controll import *


routes = {

    'index_route': '/', 'indexcontroller': Index.as_view('index'),

    'create_route': '/create', 'createcontroller': Create.as_view('create'),

    'delete_route': '/delete/product/<int:code>', 'deletecontroller': Delete.as_view('delete'),

    'update_route': '/update/product/<int:code>', 'updatecontroller': Update.as_view('update'),

}