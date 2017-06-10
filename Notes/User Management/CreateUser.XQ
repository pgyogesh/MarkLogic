(:Syntax:)
sec:create-user(
	"username",
	"User Description",
	"Password",
	"Role to assign",
	(
		(permission1),
		(permission2),
		(permission3)
		)
	),
	"Collection Name"
)


(:Example:)

xquery version "1.0-ml";
import module namespace sec="http://marklogic.com/xdmp/security" at 
    "/MarkLogic/security.xqy";

sec:create-user("pgyogesh",
"Yogesh - The Big Data Administrator",
"changeme",
"admin",
(
  xdmp:permission("admin","read"),
  xdmp:permission("admin","insert"),
  xdmp:permission("admin","update"),
  xdmp:permission("admin","execute")
),
("http://marklogic.com/dev_modules"))
