有两个文本文件： documents.txt  和 stopwords.txt 
其中:
documents.txt里有多行文本，我们假设一行文本表示一篇文档document, 则所有的文本构成了一个文档集合； 
stopwords.txt里有多行，每行仅有一个停用词，即所有行构成停用词表；

现在要求写一个python脚本preproccess.py，执行：
$ python preproccess.py documents.txt stopwords.txt

得到如下两个结果（注意，我们在处理文本时，通常英文都是大写转小写）。
（1）把每一篇document表示成 词袋(Bag of words) 模型，即每个文档是一个词向量表示(用list结构代替)，但要去掉所有停用词，并将结果输出。
正确的结果应该如下：

[['human', 'machine', 'interface', 'lab', 'abc', 'computer', 'applications'], 
['survey', 'user', 'opinion', 'computer', 'system', 'response', 'time'], 
['eps', 'user', 'interface', 'management', 'system'], 
['system', 'human', 'system', 'engineering', 'testing', 'eps'], 
['relation', 'user', 'perceived', 'response', 'time', 'error', 'measurement'], 
['generation', 'random', 'binary', 'unordered', 'trees'], 
['intersection', 'graph', 'paths', 'trees'], 
['graph', 'minors', 'iv', 'widths', 'trees', 'well', 'quasi', 'ordering'], 
['graph', 'minors', 'survey']]

（2）在上一步的基础上，把在所有文档集合中只出现过一次的词去掉，然后输出最终结果。
正确的结果应该如下：
[['human', 'interface', 'computer'], 
['survey', 'user', 'computer', 'system', 'response', 'time'], 
['eps', 'user', 'interface', 'system'], 
['system', 'human', 'system', 'eps'], 
['user', 'response', 'time'], 
['trees'], ['graph', 'trees'], 
['graph', 'minors', 'trees'], 
['graph', 'minors', 'survey']]
