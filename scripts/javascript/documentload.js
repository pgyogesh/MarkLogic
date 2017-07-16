/*
  Load the Test JSON Documents from the filesystem into the Document database.
*/

declareUpdate();

var file1 = "/Users/yogeshjadhav96/LoadTest1.json";
var file2 = "/Users/yogeshjadhav96/LoadTest2.json";

if (xdmp.databaseName(xdmp.database()) == "Documents")
{  
  xdmp.documentLoad(file1,{"uri" : "/LoadTest1.json"})
  xdmp.documentLoad(file2,{"uri" : "/LoadTest2.json"})
}
else {
  "Please select the Modules database from the Content Source menu and run this script again."
}
