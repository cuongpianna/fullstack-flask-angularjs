app.service('UserCRUDService', ['$http', function ($http) {
    this.addUser = function (username, email, password, avartar) {
        var fd = new FormData();
        fd.append('username', username);
        fd.append('email', email);
        fd.append('password', password);
        fd.append('avartar', avartar);

        $http.post('http://127.0.0.1:5000/users', fd, {
                transformRequest: angular.identity,
                headers: {
                    'Content-Type': undefined
                }
            }).success(function (respones) {
                console.log(respones);
                this.log = respones;
            })
            .error(function (data) {
                console.log(data);
            });
    }

    this.deleteUser = function(id){
        $http({
            method: 'DELETE',
            url: 'http://127.0.0.1:5000/users/'+id,
            data: {
                id: $http
            },
            headers: {
                'Content-type': 'application/json'
            }
        }).success(function(response){
            console.log(response);
        })
    }


}]);