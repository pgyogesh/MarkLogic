/*
  Create the project-default-user for the app
*/

var config = 
    {
      "user-name":"project-default-user",
      "password":"pass",
      "role": [ "project-default" ] // Role to be assigned to user, Can be more than one
    };

var options = {
  authentication: {
    'method': 'digest',
    'username': 'admin',
    'password': 'admin'
  },
  data: xdmp.quote(config), //xdmp.quote() formats the config object as a string so the REST endpoint understands it
  headers : {
    'content-type' : 'application/json'
  }
};

xdmp.httpPost('http://localhost:8002/manage/v2/users', options);
