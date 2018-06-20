var usersController = app.controller('usersController', ['$scope', '$http','$stateParams', 'UserCRUDService', function ($scope, $http,$stateParams, UserCRUDService) {
    $scope.msg = 'leu leu';
    $scope.users = [];
    $scope.offset = 1;
    $scope.range = [];
    $scope.lastpage = 1;
    $scope.limit = 5;

    $scope.userIDs = new Array();

    var url = 'http://127.0.0.1:5000/users';

    //get all users
    $http.get(url).success(function (results) {
        console.log(results);
        $scope.users = results;

    }).error(function (data) {
        console.log(data);
    });

    //function to get all users
    $scope.getAllUsers = function (offset, limit) {
        if (offset === undefined) {
            offset = $stateParams.offset || '1';
            //$scope.offset = offset;
        }
        if (limit === undefined) {
            limit = $stateParams.limit || '5';
            $scope.limit = limit;
        }

        $http.get('http://127.0.0.1:5000/users' + '?offset=' + offset + '&limit=' + limit)
            .success(function (results) {
                console.log(results.data[0]);
                $scope.users = results.data[0];
                $scope.offset = results.offset;
                $scope.lastpage = results.last_page;
                console.log(results.offset);

                var pages = [];
                for (var i = 1; i <= results.last_page; i++) {
                    pages.push(i);
                }
                $scope.range = pages;
            })
            .error(function (data) {
                console.log(data);
            });
    }

    //add users
    $scope.addUser = function () {
        var f = document.getElementById('avartar').files[0],
            r = new FileReader();
        r.onloadend = function (e) {
            var data = e.target.result;
        }
        var ss = r.readAsBinaryString(f);
        console.log(f);
        UserCRUDService.addUser($scope.user.username, $scope.user.email, $scope.user.password, f);
        $scope.info = "New user added successfully!";
        $scope.getAllUsers();
    }

    //delete user
    $scope.deleteUser = function (user) {
        if (confirm("Are you sure?")) {
            var index = $scope.users.indexOf(user);
            UserCRUDService.deleteUser(user.id);
            $scope.users.splice(index, 1);
            $scope.info = "Deleted an user!"
        }
    }

    $scope.deleteMultilUser = function (list) {
        if (confirm("Are you sure to delete these items?")) {
            var allItem = $('.userselect');
            var itemList = [];
            var totalItem = 0;
            angular.forEach(allItem, function (item) {
                if (item.checked) {
                    itemList.push(parseInt(item.attributes['data-id'].value));
                    UserCRUDService.deleteUser(item.attributes['data-id'].value);
                    totalItem++;
                }
            })
            $scope.info('Deleted ' + totalItem + ' item');
            console.log(itemList);
        }

    }

    $scope.selectedUser = function (user) {
        $scope.thisUser = user;
        console.log('user' +user);
    }

}]);


//just fo pagination
app.directive('userPagi', function () {
    return {
        restrict: 'E',
        templateUrl: '/static/angular/components/users/pagi.html',
        replace: true
    };
});