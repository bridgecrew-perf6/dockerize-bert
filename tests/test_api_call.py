import requests

# Enter API URL
url = ""

payload = "{\n  \"context\": \"We introduce a new language representation model called BERT, which stands for " \
          "idirectional Encoder Representations from Transformers. Unlike recent language epresentation models (" \
          "Peters et al., 2018a; Radford et al., 2018), BERT is designed to pretrain deep bidirectional " \
          "representations from unlabeled text by jointly conditioning on both left and right context in all layers. " \
          "As a result, the pre-trained BERT model can be finetuned with just one additional output layer to create " \
          "state-of-the-art models for a wide range of tasks, such as question answering and language inference, " \
          "without substantial taskspecific architecture modifications. BERT is conceptually simple and empirically " \
          "powerful. It obtains new state-of-the-art results on eleven natural language processing tasks, " \
          "including pushing the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% (" \
          "4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 point absolute improvement) " \
          "and SQuAD v2.0 Test F1 to 83.1 (5.1 point absolute improvement).\",\n  \"question\": \"What is BERTs best " \
          "score on Squadv2 ?\"\n} "

headers = {
  'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text.encode('utf8'))
