var app = angular.module('ProjectListApp', [
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

        $scope.go = function (url) {
            ProjectListService.go(url).then(function success (data) {
                $scope.projects = data.results;
                $scope.next_page = data.next;
                $scope.previous_page = data.previous;
            });
        };

        var init = function () {
            ProjectListService.query().then(function success (data) {
                // console.log(data)
                $scope.projects = data.results;
                $scope.next_page = data.next;
                $scope.previous_page = data.previous;
                var selected_project_id = $('#id_0-donation_recipient').val();
                if (selected_project_id) {
                    ProjectListService.detail(selected_project_id).then(function success (data) {
                        $scope.selectProject(data);
                    });
                }
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
  function($scope, $q, $filter, $location, ProjectListService) {
    $scope.project = ProjectListService.selected_project();
    $scope.$on('project:updated', function(event, project) {
      $scope.project = project;
      $('#id_0-donation_recipient').val([project.id]);
    });

    $scope.clearSelectedProject = function() {
      ProjectListService.selected_project(null);
    };
  }
]) // end controller


app.factory('ProjectListService', [
    '$q',
    '$log',
    '$resource',
    '$http',
    '$rootScope',
    function($q, $log, $resource, $http, $rootScope) {

        var selected_project = null;

        function projectListAPI() {
            return $resource('/donation-recipients/:pk', {}, {
                'query': {
                    'cache': false,
                    'isArray': false
                }
            });
        };

        var query_api = function (method, url_params, data) {
            var deferred = $q.defer();
            var api = projectListAPI();
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
            selected_project: function (project) {
                if (project === undefined) {
                    return selected_project;
                } else {
                    selected_project = project;
                    $rootScope.$broadcast('project:updated', project);
                }
            },
            go: function (url) {
                var deferred = $q.defer();
                var api = projectListAPI();
                var data = {};

                $http.get(url).then(
                    function success (response) {
                        deferred.resolve(response.data);
                    },
                    function error (err) {
                        data.results = [];
                        deferred.reject(err);
                });
                return deferred.promise;
            },
            detail: function (pk) {
                return query_api('get', {'pk': pk});
            },
            query: function (q) {
                return query_api('query', {'q': q});
            }
        };// end signleton return
    }
]); // end service
