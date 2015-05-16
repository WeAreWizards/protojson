var protojson = angular.module('protojson', []);

protojson.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
}]);


var ProtoBuf = dcodeIO.ProtoBuf;
var AddressBook;

ProtoBuf.loadProtoFile("/static/addressbook.proto", function(err, builder) {
  AddressBook = builder.build("AddressBook");
});

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
    console.log($scope);
    var xhr = ProtoBuf.Util.XHR();
    xhr.open(
        "GET",
        "/api/contacts",
        true
    );
    xhr.responseType = "arraybuffer";
    xhr.onload = function(evt) {
        var msg = AddressBook.decode(xhr.response);
        $scope.contacts = msg.contacts;
        $scope.$apply();
    }
    xhr.send(null);
  };

  // Init page with json data
  $scope.getContactsProtobuf();
  //$scope.getContacts();
});
