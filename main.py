#Copyright(c) 2019 mclt0568. MIT LISENCE applied.
#author: Mclt0568 aka Frankie
#Lets check out the file 'wordlist'

#import initialization
import core
import os

os.system("clear")

while True:
	a = input("Enter a verb in Hiragana in -masu form:")
	b = core.sorttoverb(a)
	if b != None:
		core.showresult(b)
	print("")