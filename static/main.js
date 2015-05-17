var protojson = angular.module('protojson', []);

protojson.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
}]);


var ProtoBuf = dcodeIO.ProtoBuf;
var AddressBook, Contact;

ProtoBuf.loadProtoFile("/static/addressbook.proto", function(err, builder) {
  AddressBook = builder.build("AddressBook");
  Contact = builder.build("Contact");
});

protojson.controller('AddressBookCtrl', function($scope, $http) {
  $scope.contacts = [];
  $scope.newContact = {
    firstName: "",
    lastName: ""
  };
  $scope.useProtobuf = false;
  $scope.getContacts = function() {
    $scope.contacts = [];
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
    $scope.contacts = [];
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

  var saveJSON = function(_contact) {
    var req = {
      method: 'POST',
      url: '/api/contacts',
      data: {
        first_name: contact.firstName,
        last_name: contact.lastName
      },
       headers: {
         'Accept': 'application/json'
       }
    };
    $http(req).success(function(data) {
      $scope.contacts = data;
    });
  };

  var saveProtobuf = function(_contact) {
    var contact = new Contact({
      first_name: _contact['firstName'],
      last_name: _contact['lastName'],
    });
    var req = {
      method: 'POST',
      url: '/api/contacts',
      responseType: 'arraybuffer',
      transformRequest: function(r) { return r;},
      data: contact.toArrayBuffer(),
      headers: {
        'Content-Type': 'binary/octet-stream'
      }
    };

    $http(req).success(function(data) {
      var msg = AddressBook.decode(data);
      $scope.contacts = msg.contacts;
    });
  };

  $scope.saveContact = function() {
    if ($scope.useProtobuf) {
      saveProtobuf($scope.newContact);
    } else {
      saveJSON($scope.newContact);
    }
  };

  // Init page with json data
  $scope.getContacts();
});
