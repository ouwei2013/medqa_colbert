# ColBERT trained on the Chinese cmedqa-v2 

#### This is a repo copy from the orignal ColBERT repo, by the Stanford NLP research team
#### 这个库是复制的斯坦福的nlp 研究团队的的ColBERT

#### But I made some minor changes to the original repo, in order to make it compatible with Chinese BERT
#### 但是我做了一点小的改动，使它能够兼容中文BERT

#### I trained ColBERT on the cmedqa-v2 dataset and observed impressive performance
#### 我在cmedqa-v2数据集上训练了ColBERT,效果不错

#### I deployed the model on HuggingFace Space, link:https://huggingface.co/spaces/diagaiwei/ir_chinese_medqa
#### 我把模型部署到了hf space,链接 https://huggingface.co/spaces/diagaiwei/ir_chinese_medqa

#### if you want to train it on your own data, please organize your data in the following format:
#### 如果你想训练自己的数据，可以按照以下格式组织数据

- it requires 3 files, queries.tsv, doc.tsv, triplets.jsonl <br>
  - the content of queries.tsv should be like this ( header is not needed in the tsv) <br>
  query_1_id \t 高血压吃什么药 ? <br> 
  query_2_id  \t 糖尿病吃什么药  <br>

  - the content of doc.tsv should be like this ( header is not needed in the tsv):<br>
  doc_1_id \t 高血压应该吃药A <br>
  doc_2_id \t 糖尿病应该吃药B <br>

  - each line in the triplets file should be like this: query_id, pos_doc_id,neg_doc_id, for example: <br>
    [query_1_id, doc_1_id, doc_2_id] <br>
    [query_1_id, doc_1_id, doc_3_id] <br>
    [...       ...    ....         ] <br>

