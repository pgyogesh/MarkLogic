/*
  Create the role with name project-default
*/

var config = 
    {
      "role-name":"project-default"
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

xdmp.httpPost('http://localhost:8002/manage/v2/roles', options);
