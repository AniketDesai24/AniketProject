import pandas as pd
import numpy as np
import os

writer1 = pd.ExcelWriter('D:/Python/2017-09_Warner_Bros Monthly Royalty Report - Europe.xls', engine='xlwt')
writer = pd.ExcelWriter('D:/Python/2017-09_Warner_Bros Monthly Royalty Report - Mexixo.xls', engine='xlwt')
#path = glob.glob(r'D:\python\example/*.xlsx')
sheets = ['Germany','France','Spain','Italy']
folderPath = 'D:/Python/Files'
os.chdir(folderPath)

try:
	for f in os.listdir(os.getcwd()):
		if "- DE" in f:
			print("hello" + f)
			df = pd.read_excel(f, 'Warner Bros Monthly POS Report')
			df.to_excel(writer1, 'Germany')
			os.remove(f)
		elif "- FR" in f:
			print("hello" + f)
			df = pd.read_excel(f, 'Warner Bros Monthly POS Report')
			df.to_excel(writer1, 'France')
			os.remove(f)
		elif "- ES" in f:
			print("hello" + f)
			df = pd.read_excel(f, 'Warner Bros Monthly POS Report')
			df.to_excel(writer1, 'Spain')
			os.remove(f)
		elif "- IT" in f:
			print("hello" + f)
			df = pd.read_excel(f, 'Warner Bros Monthly POS Report')
			df.to_excel(writer1, 'Italy')
			os.remove(f)
		elif "MX" in f:
			print("hello" + f)
			df = pd.read_excel(f, 'Warner Bros Monthly POS Report')
			df.to_excel(writer, 'Mexico')
			os.remove(f)
		else :
			print('not found')
	writer.save()
	writer1.save()
except:
	print "Oops!  That was no valid number.  Try again..."
