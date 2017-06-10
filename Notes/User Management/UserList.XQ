xquery version "1.0-ml";
import module namespace sec ="http://marklogic.com/xdmp/security"
  at "/MarkLogic/security.xqy";
  
declare function local:get-usernames()
  {
    for $name in /sec:user/sec:user-name/text()
    order by $name
    return $name
  };

local:get-usernames()
