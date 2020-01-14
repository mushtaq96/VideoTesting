from crontab import CronTab

cron = CronTab(user='mushtaq')
job = cron.new(command='python examplecron.py')
job.minute.every(1)

cron.write()