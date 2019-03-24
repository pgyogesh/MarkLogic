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
Yogeshs-MacBook-Air:~ yogeshjadhav$ python ml_restore_new.py --config-file config.file --user admin --password changeme --max-threads 3
2019-03-25 02:19:15,374:INFO:Reading configuration file
2019-03-25 02:19:15,397:INFO:testdb1 restore started from /mlbackup/20190325-0040001458910/Forests/testdb1
2019-03-25 02:19:15,398:INFO:testdb2 restore started from /mlbackup/20190325-0040001458910/Forests/testdb4
2019-03-25 02:19:15,399:INFO:testdb3 restore started from /mlbackup/20190325-0040001458910/Forests/testdb3
2019-03-25 02:19:15,785:ERROR:testdb2 forest restore FAILED
2019-03-25 02:19:40,773:INFO:testdb1 forest restore COMPLETED
2019-03-25 02:19:43,668:INFO:testdb3 forest restore COMPLETED
2019-03-25 02:19:43,706:INFO:DONE
```
