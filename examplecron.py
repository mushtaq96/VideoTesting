from datetime import datetime
myfile = open('append.txt','a')
myfile.write('\nAccessed on '+str(datetime.now()))