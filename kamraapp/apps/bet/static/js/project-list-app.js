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

        $scope.selectProject = function (project) {
            ProjectListService.selected_project(project);
        };

        var init = function () {
            ProjectListService.recommended().then(function success (data) {
                // console.log(data)
                $scope.projects = data;
            });
        };

        init(); // initialize
    }
])// end controller

app.controller("SelectedProjectController", [
    '$scope',
    '$q',
    '$filter',
    '$location',
    'ProjectListService',
    function ($scope, $q, $filter, $location, ProjectListService) {
        $scope.project = ProjectListService.selected_project();
        $scope.$on('project:updated', function( event, project) {
            $scope.project = project;
        });
    }
])// end controller


app.factory('ProjectListService', [
    '$q',
    '$log',
    '$resource',
    '$rootScope',
    function($q, $log, $resource, $rootScope) {

        var selected_project = null;

        function projectListAPI() {
            return $resource('/donation-recipients/:slug', {}, {
                'query': {
                    'cache': false,
                    'isArray': false
                }
            });
        };

        return {
            selected_project: function (project) {
                if (project === undefined) {
                    return selected_project;
                } else {
                    selected_project = project;
                    $rootScope.$broadcast('project:updated', project);
                }
            },
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
