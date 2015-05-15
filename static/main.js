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
         'Accept': 'application/json'
       }
    };

    $http(req).success(function(data) {
      $scope.contacts = data;
    });
  };

  $scope.getContactsProtobuf = function() {
    var req = {
      method: 'GET',
      url: '/api/contacts',
       headers: {
         'Accept': 'application/x-protobuf'
       }
    };

    $http(req).success(function(data) {
      $scope.contacts = data;
    });
  };

  // Init page with json data
  $scope.getContactsProtobuf();
  $scope.getContacts();
});
