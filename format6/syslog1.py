import syslog

syslog.syslog('test')
syslog.syslog("This is a test message")
syslog.syslog(syslog.LOG_INFO, "Test message at INFO priority")