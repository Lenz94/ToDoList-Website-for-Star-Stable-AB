<html ng-app="todoApp">
    <head>
        <script src="static/js/jquery-2.1.3.min.js"></script>
        <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.4.5/angular.min.js"></script>
        <script src="static/js/todoapp.js"></script>
        <script src="static/js/bootstrap.min.js"></script>

        <link rel="stylesheet" href="static/styles/bootstrap.min.css">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
        <link rel="stylesheet" href="static/styles/main.css">
    </head>

    <body ng-controller="TodoListController">
        <div class="row">
            <div class="col-md-4 col-xs-4 col-md-offset-1 col-xs-offset-1">
                <img src="/static/images/starstable_logo.png">
            </div>
        </div>

        <div class="row">
            <div class="col-lg-5 col-md-6 col-sm-8 col-xs-11 col-md-offset-1 col-sm-offset-1 col-xs-offset-1">
                <div class="panel panel-danger note">
                      <div class="panel-heading notehead">
                          <h2>ToDo Notes <img class="horse" src="/static/images/horse.png"></h2>
                      </div>

                      <div class="panel-body notebody">
                          <h3>Star Stable List ({{remaining()}} of {{notes.length}} done)</h3>
                          <ul class="unstyled">
                            <li ng-repeat="todo in notes">
                              <input class="checkingbox" type="checkbox" ng-model="todo.done">
                              <input class="noteInput" ng-model="todo.todo.what">
                              <span> Date: {{todo.todo.due}}</span>
                              <a ng-click="updateTodo(todo.todo.id, todo)"><i class="fa fa-floppy-o icon"></i></a>
                              <a ng-click="removeTodo(todo.todo.id, todo)"><i class="fa fa-trash-o fa-lg icon"></i></a>
                            </li>
                          </ul>

                          <form ng-submit="addTodo(what)">
                            <input type="text" class="noteInput2" ng-model="what"  size="30"
                                   placeholder="Add a new todo here">
                            <input type="submit" class="btn-primary" value="Add">
                          </form>

                      </div>

                      <div class="panel-footer">by Enzo Marcani</div>
                </div>
           </div>

        </div>
    </body>
</html>