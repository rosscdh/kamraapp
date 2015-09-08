var app = angular.module('ProjectDetailApp', [
    'ui.router',
    'ngResource',
    'ngSanitize',
    'angularMoment',
    'angular-loading-bar',
    'smart-table',
])


app.config(function ($stateProvider, $httpProvider, $urlRouterProvider) {
    // For any unmatched url, send to /route1
    $urlRouterProvider.otherwise("/");
    $stateProvider
        .state('index', {
            url: "/",
            templateUrl: "",
            controller: "ProjectListController"
        })
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
})


app.controller("BetForController", [
    '$scope',
    '$q',
    '$filter',
    '$location',
    'ProjectDetailService',
    function ($scope, $q, $filter, $location, ProjectDetailService) {
        $scope.data = {
            'bets': [],
            'betters': [],
            'total': 0,
        };
        $scope.can_bet = false;
        $scope.bet = window.bet;
        $scope.user = window.user;

        $scope.$watchCollection('data.betters', function(newBetters, oldBetters) {
          can_bet(newBetters);
        });

        var can_bet = function (betters) {
          if (betters.some(function (element, index, array) {
            console.log(element.pk)
            return element.pk === $scope.user.pk;
          }) == true) {
            $scope.can_bet = false;
          } else {
            $scope.can_bet = true;
          }
        };

        $scope.bet_for = function (event, data) {
            ProjectDetailService.bets_for('save', $scope.bet.pk, $scope.user.pk).then(function success (data) {
                $scope.data = data;
            });
        };

        var init = function () {
            ProjectDetailService.bets_for('get', $scope.bet.pk, $scope.user.pk).then(function success (data) {
                $scope.data = data;
                console.log($scope.data)
                can_bet($scope.data.betters);
            });
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
        $scope.data = {
            'bets': [],
            'betters': [],
            'total': 0,
        };
        $scope.can_bet = false;
        $scope.bet = window.bet;
        $scope.user = window.user;

        $scope.$watchCollection('data.betters', function(newBetters, oldBetters) {
          can_bet(newBetters);
        });

        var can_bet = function (betters) {
          if (betters.some(function (element, index, array) { return element.pk === $scope.user.pk; }) == true) {
            $scope.can_bet = false;
          } else {
            $scope.can_bet = true;
          }
        };

        $scope.bet_against = function (event, data) {
            ProjectDetailService.bets_against('save', $scope.bet.pk, $scope.user.pk).then(function success (data) {
                $scope.data = data;
            });
        };

        var init = function () {
            ProjectDetailService.bets_against('get', $scope.bet.pk, $scope.user.pk).then(function success (data) {
                $scope.data = data;
                can_bet($scope.data.betters);
            });
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
            return $resource('/bets/:pk/:action', {}, {
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
            bets_for: function (method, pk, user) {
                return query_api(method,
                                {'action': 'bets_for',
                                 'pk': pk},
                                {'user': user.id});
            },
            bets_against: function (method, pk, user) {
                return query_api(method,
                                {'action': 'bets_against',
                                 'pk': pk},
                                {'user': user.id});
            },
            query: function (q) {
                return query_api('query', {'q': q});
            }
        };// end signleton return
    }
]); // end service
