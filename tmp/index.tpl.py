# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1442561838.472164
_enable_loop = True
_template_filename = 'templates/index.tpl'
_template_uri = 'index.tpl'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer(u'<html ng-app="todoApp">\n    <head>\n        <script src="static/js/jquery-2.1.3.min.js"></script>\n        <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.5/angular.min.js"></script>\n        <script src="static/js/todoapp.js"></script>\n        <script src="static/js/bootstrap.min.js"></script>\n\n        <link rel="stylesheet" href="static/styles/bootstrap.min.css">\n        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">\n        <link rel="stylesheet" href="static/styles/main.css">\n    </head>\n\n    <body ng-controller="TodoListController">\n        <div class="row">\n            <div class="col-md-4 col-xs-4 col-md-offset-1 col-xs-offset-1">\n                <img src="/static/images/starstable_logo.png">\n            </div>\n        </div>\n\n        <div class="row">\n            <div class="col-lg-5 col-md-6 col-sm-8 col-xs-11 col-md-offset-1 col-sm-offset-1 col-xs-offset-1">\n                <div class="panel panel-danger note">\n                      <div class="panel-heading notehead">\n                          <h2>ToDo Notes <img class="horse" src="/static/images/horse.png"></h2>\n                      </div>\n\n                      <div class="panel-body notebody">\n                          <h3>Star Stable List ({{remaining()}} of {{notes.length}} done)</h3>\n                          <ul class="unstyled">\n                            <li ng-repeat="todo in notes">\n                              <input class="checkingbox" type="checkbox" ng-model="todo.done">\n                              <input class="noteInput" ng-model="todo.todo.what">\n                              <span> Date: {{todo.todo.due}}</span>\n                              <a ng-click="updateTodo(todo.todo.id, todo)"><i class="fa fa-floppy-o icon"></i></a>\n                              <a ng-click="removeTodo(todo.todo.id, todo)"><i class="fa fa-trash-o fa-lg icon"></i></a>\n                            </li>\n                          </ul>\n\n                          <form ng-submit="addTodo(what)">\n                            <input type="text" class="noteInput2" ng-model="what"  size="30"\n                                   placeholder="Add a new todo here">\n                            <input type="submit" class="btn-primary" value="Add">\n                          </form>\n\n                      </div>\n\n                      <div class="panel-footer">by Enzo Marcani</div>\n                </div>\n           </div>\n\n        </div>\n    </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"26": 20, "20": 1, "15": 0}, "uri": "index.tpl", "filename": "templates/index.tpl"}
__M_END_METADATA
"""
