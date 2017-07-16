xquery=
xquery version "1.0-ml";
(:
  1. This script is used to get user details
  2. This script has to run against Security Database
:)

<table border="1" align="left">
  <tr>
        <th bgcolor="#ffe2ba"> Username </th>
        <th bgcolor="#ffe2ba"> Description </th>
  </tr>
  {
  for $user in /sec:user
    let $username := $user/sec:user-name/text()
    let $description := $user/sec:description/text()
    (:where $username = 'username':)
    order by $username
    return
    <tr>
      <td>{$username}</td>
      <td>{$description}</td>
    </tr>
   }
</table>
