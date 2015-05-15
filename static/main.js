var protojson = angular.module('protojson', []);

protojson.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
}]);

protojson.controller('AddressBookCtrl', function($scope, $http) {
  $scope.contacts = [];

  $scope.getContacts = function() {
    var req = {
      method: 'GET',
      url: '/api/contacts',
       headers: {
         'Content-Type': 'application/json'
       }
    };

    $http(req).success(function(data) {
      $scope.contacts = data;
    });
  };

  // Init page with json data
  $scope.getContacts();
});
