var app = angular.module('ProjectListApp', [
    'ui.router',
    'ngResource',
    'angularMoment',
    'angular-loading-bar',
    'daterangepicker',
    'smart-table',
    'chart.js',
])


app.config(function ($stateProvider, $urlRouterProvider) {
    // For any unmatched url, send to /route1
    $urlRouterProvider.otherwise("/");
    $stateProvider
        .state('index', {
            url: "/",
            templateUrl: "/static/html/partials/_job_list.html",
            controller: "DashboardController"
        })
})


app.controller("DashboardController", [
    '$scope',
    '$q',
    '$filter',
    '$location',
    'ProjectListService',
    function ($scope, $q, $filter, $location, ProjectListService) {

        var init = function () {
            ProjectListService.initial().then(function success (data) {
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
                },
            });
        };

        return {
            query: function (q) {
                var deferred = $q.defer();
                var api = projectListAPI();
                var data = {};

                api.query({'q': q},
                    function success (response) {
                        deferred.resolve(response.toJSON());
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
