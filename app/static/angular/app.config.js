app.config(function($stateProvider,$urlRouterProvider){
    $urlRouterProvider.otherwise('')

    $stateProvider
        .state('admin',{
        url: '',
        controller: 'dashboardController',
        templateUrl: '/static/angular/components/dashboard/dashboard.html'
    })
        .state('users',{
        url: '/users?offset&limit',
        templateUrl: '/static/angular/components/users/users.html',
        controller: 'usersController',
    })
});