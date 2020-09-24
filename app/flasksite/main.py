import flasksite.pypd
import os
from flasksite.create_profile import create_profile
from os import listdir
from os.path import isfile, join
from io import StringIO
import pandas as pd
from collections import Counter

mypath = '/home/madscientist/Desktop/Resume_ranker/resumes'
onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

def execute(csv_filename):
	 
	csv_path = '/home/madscientist/Desktop/Resume_ranker/csvs/' + csv_filename + '.csv'
	keyword_dict = pd.read_csv(csv_path)
	keyword_dict = keyword_dict.loc[:, ~keyword_dict.columns.str.contains('^Unnamed')]
	col_name = keyword_dict.columns.to_list()
	col_name = ['Candidate Names'] + col_name + ['Experience'] + ['Total Score']
	#print(col_name)
	main_frame = pd.DataFrame(columns=col_name)
	#main_frame.set_index('Candidate Names')
	i = 0
	while i < len(onlyfiles):
		file = onlyfiles[i]
		text = flasksite.pypd.get_text(file)
		main_frame = create_profile(text,main_frame,file,csv_path)
		i += 1

	#print(main_frame)
	main_frame.set_index('Candidate Names')
	main_frame['Total Score'] = main_frame['Total Score'].astype(int)
	main_frame.sort_values(by=['Total Score'], ascending=False, inplace=True)
	main_frame.to_csv('/home/madscientist/Desktop/Resume_ranker/profile/profile.csv', sep='\t', encoding='utf-8', index=False)
	return main_frame








