import pandas as pd
import en_core_web_sm
nlp = en_core_web_sm.load()
from spacy.matcher import PhraseMatcher
from pyresparser import ResumeParser

def create_profile(text,main_frame,file,csv_filename):
	data = ResumeParser(file).get_extracted_data()
	temp_frame = main_frame
	keyword_dict = pd.read_csv(csv_filename)
	keyword_dict = keyword_dict.loc[:, ~keyword_dict.columns.str.contains('^Unnamed')]
	col_name = keyword_dict.columns.to_list()
	words = []
	for ele in col_name:
		temp = [nlp(text) for text in keyword_dict[ele].dropna(axis = 0)]
		words.append(temp)

	matcher = PhraseMatcher(nlp.vocab)
	for i in range(len(col_name)):
		matcher.add(col_name[i], None, *words[i])
	
	doc = nlp(text)
	matches = matcher(doc)
	d = {}
	for match_id, start, end in matches:
		rule_id = nlp.vocab.strings[match_id] 
		span = doc[start : end]  
		if rule_id in d:
			d[rule_id] = d[rule_id] + 1
		else:
			d[rule_id] = 1
	
	nd = {}
	nd['Candidate Names'] = data['name'].rstrip()
	total = 0
	for u in col_name:
		if u not in d:
			nd[u] = 0
		else:
			nd[u] = d[u]
			total += d[u]

	nd['Experience'] = data['total_experience']
	total += data['total_experience']
	nd['Total Score'] = total
	temp_frame = temp_frame.append(nd, ignore_index=True)
	return temp_frame
	


 


	
	




