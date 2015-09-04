var app = angular.module('ProjectListApp', [
    'ui.router',
    'ngResource',
    'ngSanitize',
    'angularMoment',
    'angular-loading-bar',
    'smart-table',
])


app.config(function ($stateProvider, $urlRouterProvider) {
    // For any unmatched url, send to /route1
    $urlRouterProvider.otherwise("/");
    $stateProvider
        .state('index', {
            url: "/",
            templateUrl: "",
            controller: "ProjectListController"
        })
})


app.controller("ProjectListController", [
    '$scope',
    '$q',
    '$filter',
    '$location',
    'ProjectListService',
    function ($scope, $q, $filter, $location, ProjectListService) {
        $scope.projects = [];

        var init = function () {
            ProjectListService.recommended().then(function success (data) {
                // console.log(data)
                $scope.projects = data;
            });
        };

        init(); // initialize
    }
])// end controller


app.factory('ProjectListService', [
    '$q',
    '$log',
    '$resource',
    function($q, $log, $resource) {

        function projectListAPI() {
            return $resource('/donation-recipients/:slug', {}, {
                'query': {
                    'cache': false,
                    'isArray': false
                }
            });
        };

        return {
            query: function (q) {
                var deferred = $q.defer();
                var api = projectListAPI();
                var data = {};

                api.query({'q': q},
                    function success (response) {
                        data = response.toJSON();
                        deferred.resolve(data.results);
                    },
                    function error (err) {
                        data.results = [];
                        deferred.reject(err);
                    }
                );
                return deferred.promise;
            },
            recommended: function () {
                var deferred = $q.defer();
                var api = projectListAPI();
                var data = {};

                api.query({'q': null},
                    function success (response) {
                        data = response.toJSON();
                        deferred.resolve(data.results);
                    },
                    function error (err) {
                        data.results = [];
                        deferred.reject(err);
                    }
                );
                return deferred.promise;
            }
        };// end signleton return
    }
]); // end service
