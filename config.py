# check if any of these words appears in the abstract
keywords = ['summarization', 'summary', 'evaluation', 'metric']

# check if all these words are in the abstract
gen_keywords = ['text', 'generation', 'models'] 

mt_keywords = ['machine translation', 'MT']

# check which combination of words mentioned in the paper body (don't apply lowercase transformation)
metric_keywords = ['ROUGE', 'BLEU', 'METEOR', 'BERTScore', 'sacreBLEU'] 

anthology_bib = "anthology+abstracts.bib" # can be loaded from ACL anthology main page
parsed_anthology_bib = "papers_url_and_abstract.bib"
acl_url = "https://aclanthology.org/"
# other patterns: 'J{2 last digits of the year}-{1(2,3,4)000 + id}.pdf'  
# 1000, 2000, ... depends on the month of conference
long_papers = "acl-long"
short_papers = "acl-short"
