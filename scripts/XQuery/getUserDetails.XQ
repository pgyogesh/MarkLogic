(:
  1. This script is used to get user details
  2. This script has to run against Security Database
:)

<table border="1" align="left">
  <tr>
        <th bgcolor="#ffe2ba"> Sr. </th>
        <th bgcolor="#ffe2ba"> Username </th>
        <th bgcolor="#ffe2ba"> Description </th>
  </tr>
  {
  for $user at $num in /sec:user
    let $username := $user/sec:user-name/text()
    let $description := $user/sec:description/text()
    return
    <tr>
      <td>{$num}</td>
      <td>{$username}</td>
      <td>{$description}</td>
    </tr>
   }
</table>
