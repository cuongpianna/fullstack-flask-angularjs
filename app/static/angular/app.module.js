var app = angular.module("app", ['ui.router','ngResource']);
app.controller("HelloController", function($scope) {
  $scope.message = "Hello, AngularJS";
});