var app = angular.module('ProjectDetailApp', [
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


app.controller("BetForController", [
    '$scope',
    '$q',
    '$filter',
    '$location',
    'ProjectDetailService',
    function ($scope, $q, $filter, $location, ProjectDetailService) {
        var init = function () {
        };

        init(); // initialize
    }
])// end controller

app.controller("BetAgainstController", [
    '$scope',
    '$q',
    '$filter',
    '$location',
    'ProjectDetailService',
    function ($scope, $q, $filter, $location, ProjectDetailService) {
        var init = function () {
        };

        init(); // initialize
    }
])// end controller


app.factory('ProjectDetailService', [
    '$q',
    '$log',
    '$resource',
    '$http',
    '$rootScope',
    function($q, $log, $resource, $http, $rootScope) {

        var selected_project = null;

        function projectDetailAPI() {
            return $resource('/bet/:slug/:action', {}, {
                'query': {
                    'cache': false,
                    'isArray': false
                }
            });
        };

        var query_api = function (method, url_params, data) {
            var deferred = $q.defer();
            var api = projectDetailAPI();
            var data = {};
            url_params = url_params || {};
            data = data || {};

            api[method](url_params, data,
                function success (response) {
                    data = response.toJSON();
                    deferred.resolve(data);
                },
                function error (err) {
                    data.results = [];
                    deferred.reject(err);
                }
            );
            return deferred.promise;
        };

        return {
            go: function (url) {
                var deferred = $q.defer();

                $http.get(url).then(
                    function success (response) {
                        deferred.resolve(response.data);
                    },
                    function error (err) {
                        deferred.reject(err);
                });
                return deferred.promise;
            },
            bet_for: function (slug, user) {
                return query_api('post',
                                 {'action': 'for'},
                                 {'user': user.id});
            },
            bet_against: function (slug, user) {
                return query_api('post',
                                 {'action': 'against'},
                                 {'user': user.id});
            },
            query: function (q) {
                return query_api('query', {'q': q});
            }
        };// end signleton return
    }
]); // end service
