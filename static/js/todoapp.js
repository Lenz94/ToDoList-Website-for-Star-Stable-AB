angular.module('todoApp', [])
  .controller('TodoListController',['$scope', '$http', function($scope, $http) {

    $scope.showAll = function() {
        $http.get('todo/get')
          .success(function (data) {
            $scope.notes = data.todos;
            $scope.remaining();
          })
    };

    $scope.showAll();

    $scope.addTodo = function(what, done) {
        var newTodo = { todos:[]};
        var note = {
                todo: {
                    what : what,
                    done : 0,
                    due : null
                }
        }
        newTodo.todos.push(note);
        $http.post('todo/add', newTodo)
          .success(function () {
            $scope.showAll();
            $scope.what = "";
        });
    };

    $scope.removeTodo = function(id){
        $http.delete('todo/delete/' + id)
        .success(function(){
            $scope.showAll();
            $scope.what = "";
        });
    };

    $scope.updateTodo = function(id, todo){
        $http.put('todo/update/' + id, todo)
        .success(function(){
            $scope.showAll();
            $scope.what = "";
        });
    };

    $scope.remaining = function() {
      var count = 0;
      angular.forEach($scope.notes, function(todo) {
        count += todo.done ? 1 : 0;
      });
      return count;
    };

  }]);