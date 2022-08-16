# eval_metrics_for_text_generation
This repo is devoted to the comparison of evaluation metrics for NLG systems. The main focus is on the metrics for machine translation.

To obtain the scores of the particular metric, we either run the corresponding notebook located in the `run_metrics_noteboks` directory or set up the external github repository where the metric is implemented and run the code due to instructions there. Notebooks located in the`run_metrics_noteboks` directory are set up to run Google Colab.

__Instructions on where to find metric implementation and how to run it__:    

- BLEU, chrF, TER, METEOR, NIST, RIBES, and hLEPOR metrics don't require any specific set up and we use compute their scores directly in the analysis notebooks. BLEU, chrF, and TER are implemented in SacreBLEU \url{https://github.com/mjpost/sacrebleu/}. For METEOR, NIST, and RIBES, we use their NLTK implementation. hLEPOR implementation was taken from this package: \url{https://pypi.org/project/hLepor/}.

- The WMD implementation is in `gensim` package, which has a function `wmdistance` that corresponds to the WMD metric. We have the corresponding notebook in `run_metrics_noteboks` for WMD.

- GTM scores are obtained using [this software](http://nlp.cs.nyu.edu/GTM/). The command to GTM locally in shell:   
```
gtm: java -jar gtm.jar +s -d -t ../all_mt_snts_21.txt ../all_ref_snts_21.txt >> res.txt 
```

- For the ROUGE metric, we use the [SacreROUGE](https://github.com/danieldeutsch/sacrerouge) implementation and have the corresponding notebook in `run_metrics_noteboks`.

- For TERp, we use [this package](https://github.com/snover/terp). 

- For the BEER metric, we used BEER 2.0 version implemented [here](https://github.com/stanojevic/beer). 

- YiSi implementation was taken from [here](https://github.com/chikiulo/yisi). 

- For Prism, we have the corresponding notebook in `run_metrics_noteboks`.

- For BERTScore, we have the corresponding notebook in `run_metrics_noteboks`.

- We use [this](https://github.com/google-research/bleurt) implementation of BLEURT with the \textit{BLEURT-20} checkpoint. We recommend to run BLEURT on the chunks of data to not run out of memory.

- For COMET, we have the corresponding notebook in `run_metrics_noteboks`.

- For MTEQA, we clone [this repo](https://github.com/ufal/MTEQA) and compute metric scores by running the following command:
```
    python mteqa_score.py --reference ref --hypothesis out --lang en
```

- For MoverScore, we have the corresponding notebook in `run_metrics_noteboks`.
