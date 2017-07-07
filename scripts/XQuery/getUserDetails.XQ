(:
  1. This script is used to get user details
  2. This script has to run against Security Database
  3. Just choose HTML format to get result in table format
:)

<table border="1">
  <tr>
        <th> Username </th>
        <th> Description </th>
  </tr>
  {
  for $user in /sec:user
    let $username := $user/sec:user-name/text()
    let $description := $user/sec:description/text()
    return
    <tr>
      <td>{$username}</td>
      <td>{$description}</td>
    </tr>  
   }
</table>
