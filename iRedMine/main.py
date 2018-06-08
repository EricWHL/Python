from redmine import Redmine

redmine = Redmine('http://iredmine/my/page', key = '6f7adbbb0a5b1d86e03599054b12cc82ecae6956')

issue = redmine.issue.new()
print ('project:%s' % issue.project.name)
