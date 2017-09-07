xquery version "1.0-ml";
import module namespace sec="http://marklogic.com/xdmp/security" at "/MarkLogic/security.xqy";
for $u in /sec:user
let $n := string($u/sec:user-name)
order by $n
return
  <user>
    <name>{$n}</name>
    {
      for $role-id in $u/sec:role-ids/sec:role-id 
      let $role-name := sec:get-role-names($role-id)/fn:string()
      order by $role-name
      return element role {$role-name}
    }
  </user>
