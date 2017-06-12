/*
  Update the documents in the database with appropriate permissions.
*/

declareUpdate();

if (xdmp.databaseName(xdmp.database()) == "Documents") // To check if DB is correct
{
  xdmp.documentAddPermissions("/uri/of/document.json",
 [
    xdmp.permission("rolename1", "read"), 
    xdmp.permission("rolename2", "update"),
    \\ Add more permissions here if required
 ]);
}
else 
{
  "Please select the Documents database from the Content Source menu and run this script again." 
} 

/*
Permisions can be "read","insert","update","execute"
*/
