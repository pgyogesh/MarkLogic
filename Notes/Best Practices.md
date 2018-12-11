## Re-indexing
  - Stop the journal archiving
  - Start reindexing
  - Take increamental backup with journal archiving
  
## Updating permissions.
  - Stop the journal archiving
  - Update the permissions
  - Take increamental backup with journal archiving

## Checking the archiving status of forest

```
declare namespace fs="https://www.marklogic.com/xdmp/status/forest" ;
xdmp:forest-status(xdmp:forest('Documents'))/fs:point-in-time-recovery/fs:journal-archive
```
