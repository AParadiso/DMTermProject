# -*- coding: utf-8 -*-
"""
Anthony Paradiso
ID: 001187812
Course: CSI 526-01 - Data Mining
TA Lin Zhang
"""

from LocationResolver import LocationResolver
import json
import sys
reload(sys)
sys.setdefaultencoding("utf8")

def main():

	tweets = []
	zero_count = 0
	one_count = 0
	
	for line in open('class_data.txt').readlines():
		tweet = json.loads(line)
		tweets.append(tweet)
		
	for tweet in tweets:
		
		if 'class' in tweet:
			if tweet['class'] == 0:
				zero_count += 1
			else:
				one_count += 1
			continue
			
		try:
			num = int(raw_input(tweet['text'] + '\n\r'))
		except ValueError:
			print "Not a number"
		
		if num == 0:
			zero_count += 1
		elif num == -999:
			break
		else:
			one_count += 1
	
		tweet['class'] = num
	
	print 'neg: ',zero_count
	print 'pos: ',one_count
	
	f = open('class_data.txt', 'w')  

	for tweet in tweets:
		f.write(json.dumps(tweet) + '\n')
		
	f.close()

if __name__ == '__main__':
	main()