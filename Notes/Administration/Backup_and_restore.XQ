(:BACKUP:)

xdmp:database-backup((Forest ID),"/PATH/TO/BACKUP")

(:Example:)
xdmp:database-backup((10),
    "/Users/yogeshjadhav96/marklogic/backup")
    
(:How to get Forest ID:)

xquery version "1.0-ml";
import module namespace admin = "http://marklogic.com/xdmp/admin"
		  at "/MarkLogic/admin.xqy";

admin:forest-get-id(admin:get-configuration(), "Forest_Name")
