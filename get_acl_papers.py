import requests
from bs4 import BeautifulSoup

from config import *


def get_paper_content(url, store=False):
    '''
    Loads paper from url and stores it if `store` = True
    '''
    res = requests.get(url, allow_redirects=True)
    content = res.content
    if store:
        name = url.split('/')[-1]
        with open(name, 'wb') as f:
            f.write(content)
    return content


def filter_papers_based_on_abstract():
    """
    TODO: add years; construct appropriate urls
    """
    
    paper_links = {}
    years = [2021] 
    for year in years:
        paper_links[year] = {}
        for t in ['long', 'short']:
            papers = {}
            num = 1
            exists = True
            while exists:
                p = f'2021.acl-{t}.{num}'
                paper_url = f"{acl_url}{p}"
                response = requests.get(paper_url+'/')
                if response.status_code != 200:
                    exists = False
                    continue
                soup_response = BeautifulSoup(response.text, 'html.parser')
                paper_name = soup_response.find("a", attrs={"href": f'/{p}/'}).text
                abstract = soup_response.find("div", attrs={"class": "card-body acl-abstract"}).find("span")
                abstract = abstract.text.lower()
                
                if summary_and_metrics(abstract) or about_text_generation(abstract):
                    papers[f'{year}_{t}_{num}'] = (paper_name, paper_url)
            paper_links[year][t] = papers
    
    return paper_links


def filter_papers_based_on_content(paper_dict, search_for=['BLEU']):
    '''
    Loads paper, checks if there are any words from the `search_for` dict in its 
    content, and if yes prints the name of paper. 
    '''
    for _, p_val in paper_dict.items():
        name, url = p_val
        print(f'\nFilter paper `{name}`')
        pdf_url = url + '.pdf'
        content = get_paper_content(pdf_url)
        for k in search_for:
            if k in content:
                print(f'`{k}`` appears in this paper')
                

def about_text_generation(abstract):
    '''
    Checks if all words from `gen_keywords` list are in abstract.
    '''
    for k in gen_keywords:
        if k not in abstract:
            return False
    print('Text generation topic')
    return True


def summary_and_metrics(abstract):
    '''
    Checks if any of `keywords` is in abstract.
    '''
    for k in keywords:
        if k in abstract:
            print(f'Summary and/or metrics. Keyword: {k}')
            return True
    return False


def check_used_metrics(paper):
    for mk in metric_keywords:
        if mk in paper:
            print(mk)


if __name__ == '__main__':
    res = filter_papers_based_on_abstract()
    papers = filter_papers_based_on_content(res)
    for p in papers:
        print(p)
