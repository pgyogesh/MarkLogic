### Success: (3 parallel restores)

```
Yogeshs-MacBook-Air:~ yogeshjadhav$ python ml_restore_new.py --config-file config.file --user admin --password changeme --max-threads 3
2019-03-25 02:08:52,372:INFO:Reading configuration file
2019-03-25 02:08:52,394:INFO:testdb1 restore started from /mlbackup/20190325-0040001458910/Forests/testdb1
2019-03-25 02:08:52,394:INFO:testdb2 restore started from /mlbackup/20190325-0040001458910/Forests/testdb2
2019-03-25 02:08:52,396:INFO:testdb3 restore started from /mlbackup/20190325-0040001458910/Forests/testdb3
2019-03-25 02:09:19,011:INFO:testdb1 forest restore COMPLETED
2019-03-25 02:09:19,011:INFO:testdb2 forest restore COMPLETED
2019-03-25 02:09:21,529:INFO:testdb3 forest restore COMPLETED
2019-03-25 02:09:21,574:INFO:DONE
```

### Success: (2 parallel restore)

```
Yogeshs-MacBook-Air:~ yogeshjadhav$ python ml_restore_new.py --config-file config.file --user admin --password changeme --max-threads 2
2019-03-25 02:21:37,650:INFO:Reading configuration file
2019-03-25 02:21:37,673:INFO:testdb1 restore started from /mlbackup/20190325-0040001458910/Forests/testdb1
2019-03-25 02:21:37,673:INFO:testdb2 restore started from /mlbackup/20190325-0040001458910/Forests/testdb2
2019-03-25 02:22:02,597:INFO:testdb1 forest restore COMPLETED
2019-03-25 02:22:02,598:INFO:testdb3 restore started from /mlbackup/20190325-0040001458910/Forests/testdb3
2019-03-25 02:22:02,876:INFO:testdb2 forest restore COMPLETED
2019-03-25 02:22:30,254:INFO:testdb3 forest restore COMPLETED
2019-03-25 02:22:30,355:INFO:DONE
```

### Failed: (I used backup directory which doesn't exists)

```
Yogeshs-MacBook-Air:~ yogeshjadhav$ python ml_restore_new.py -c config.file -p 2 -u admin -w changeme
2019-03-27 00:45:16,324:INFO:Reading configuration file
2019-03-27 00:45:16,349:INFO:testdb1 restore started from /mlbackup/20190325-0040001458910/Forests/testdb1
2019-03-27 00:45:16,350:INFO:testdb2 restore started from /mlbackup/20190325-0040001458910/Forests/testdb2
2019-03-27 00:45:40,904:INFO:testdb1 forest restore COMPLETED
2019-03-27 00:45:40,904:INFO:testdb3 restore started from /mlbackup/20190325-0040001458910/Forests/testdb4
2019-03-27 00:45:41,118:INFO:testdb2 forest restore COMPLETED
2019-03-27 00:45:41,314:ERROR:testdb3 forest restore FAILED
2019-03-27 00:45:41,314:ERROR:<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>500 Internal Server Error</title>
    <meta name="robots" content="noindex,nofollow"/>
    <link rel="stylesheet" href="/error.css"/>
  </head>
  <body>
    <span class="error">
      <h1>500 Internal Server Error</h1>
      <dl>
        <dt>XDMP-LABELDNE: xdmp:forest-restore(xs:unsignedLong("9378778004316883276"), "/mlbackup/20190325-0040001458910/Forests/testdb4") -- Forest label does not exist: /mlbackup/20190325-0040001458910/Forests/testdb4/Label</dt>
        <dd></dd>
        <dt>in /eval, at 5:4 [1.0-ml]</dt>
        <dd></dd>
      </dl>
    </span>
  </body>
</html>
2019-03-27 00:45:41,314:INFO:Restore will continue for other forests
2019-03-27 00:45:41,362:INFO:DONE
```
