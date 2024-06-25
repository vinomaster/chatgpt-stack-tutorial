# Learning Journey
This repo captures early learning activities acround the building of a local GenAi solution.

The approach taken is iterative using the folowing steps:

* Query CHatGPT for guidance
* Investigate the usefulness of the guidance
* Expand on queries and document findings.

>A Jupyter Notebook Environment would dramatically help here.

## Approach 1
Creating a domain-specific text analytics application with a natural language interface (NLU) as the user experience (UX).

| Goal | ChatGPT Guidance |
| --- | --- |
| Establish a comprehensive guide for a beginner to explore a corpus of text data from PDF files. | [Prompt 1 Guidance](https://chatgpt.com/share/e2b69dce-5879-4793-84ec-fad29f5bb49b) |

### Observations

1. Code lacks integration of text-analytics with a model
2. Proposed code uses deprecated Open SDK APIs

### Issues

#### Problem 1
*ModuleNotFoundError: No Module Named openai*

#### Solution 1

Follow the steps below to install the openai package for the current interpreter

Enter the python terminal session using `python` and then run the following code

```
import sys
print(sys.executable)
```

get the current interpreter path

`/Users/dag/Code/sandbox/chatgpt-101/text_analytics_env/bin/python` 

Copy the path and install openai using the following command in the terminal

```
/Users/dag/Code/sandbox/chatgpt-101/text_analytics_env/bin/python -m pip install openai
```

#### Problem 2
OpenAI Deprecated API.

#### Solution 2
[OpenAI SDK Migration](https://github.com/openai/openai-python/discussions/742)

#### Problem 3
Setting OpenAI API Key

#### Solution 3

```
export OPENAI_API_KEY=<ENTER KEY  HERE>
```

## Approach 2
Integration of text-analytics with language model

Creating a domain-specific text analytics application with a natural language interface (NLU) as the user experience (UX).

| Goal | ChatGPT Guidance |
| --- | --- |
| Integrate the extracted PDF data into the text analytics application and ensure the language model (engine) can provide accurate, domain-specific responses. | [Prompt 2 Guidance](https://chatgpt.com/share/e2b69dce-5879-4793-84ec-fad29f5bb49b) |

### Observations
Two options were proposed. Explored *Option 2: Using Document Embeddings for Retrieval-Based Q&A* which yielded numerous runt-time errors.

### Issues 
#### Problem 4
Integrated PDF data

#### Solution 4
[See library docs](https://pypi.org/project/sentence-transformers/)

```
pip install -U sentence-transformers
```

#### Problem  5
Object of type SentenceTransformer is not JSON serializable

## Research Inquiry 1
Creating a domain-specific text analytics application with a natural language interface using Python involves several steps. Here’s a detailed guide for beginners to establish a reusable set of Python scripts to accomplish this task, using the latest versions of OpenAI SDK and Streamlit for the UX.

| Goal | ChatGPT Guidance |
| --- | --- |
| Propose a solution that manages embeddings and indexes manually with FAISS. | [Prompt 1 Guidance](https://chatgpt.com/share/1ca56245-5de4-4a4d-a96f-935249a82859) |


## Research Inquiry 2
How would the solution to Approach 3 be modified and improved by using Vector DBs?

| Goal | ChatGPT Guidance |
| --- | --- |
| Explore Vector DB benefits | [Technology Comparison from Prompts 3 and 5](https://chatgpt.com/share/1ca56245-5de4-4a4d-a96f-935249a82859) |

Several Vector DB options, namely, Milvus, Weaviate,
Pinecone, Cassio, and MindsDB are considered and compared. 

## Approach 3
Test an alternative using MindsDB as the Vector DB. This will aloow for the managing and querying of embeddings. MindsDB is particularly suitable for integrating machine learning models with databases, and it can work well with vector search tasks.

| Goal | ChatGPT Guidance |
| --- | --- |
| Leverage an open-source self managed vector db solution using MindsDB. | [Prompt 4 Guidance](https://chatgpt.com/share/1ca56245-5de4-4a4d-a96f-935249a82859) |


### Observations

1. [Setup](https://docs.mindsdb.com/contribute/install)

```
pip install mindsdb openai streamlit PyPDF2
brew install libmagic # for macOS
```

2. Create Virtual Env
```
python -m venv mindsdb-venv
```

3. Activate Virtual environment

```
source mindsdb-venv/bin/activate
```

### Results
Abandoned approach. MAy still be viable but new insighjts suggest [Chroma](https://docs.trychroma.com/getting-started) is a better approach.


## Approach 4
Test an alternative using Chroma as the Vector DB. This will allow for the managing and querying of embeddings. Chroma is particularly suitable for integrating machine learning models with databases, and it can work well with vector search tasks.

| Goal | ChatGPT Guidance |
| --- | --- |
| Leverage an open-source self managed vector db solution using Chroma. | [Prompt 1 Guidance](https://chatgpt.com/share/b5011cc2-e75b-47c4-af81-27f453b6849e) |


### Observations

1. [Chroma Setup](https://docs.trychroma.com/getting-started)
2. Install and run Docker Hub Image `chromadb/chroma:latest` 
3. This approach publically shares the PDF data with OpenAI Servers. To avoid this we can consider *Local Embedding Generation*.

### Decision
Explore a *Local Embedding Generation* solution.

## Approach 5
Test an alternative using Chroma as the Vector DB and local embedding. This will prevent the sharing of data and allow for the managing and querying of embeddings. Chroma is particularly suitable for integrating machine learning models with databases, and it can work well with vector search tasks.

| Goal | ChatGPT Guidance |
| --- | --- |
| Leverage an open-source self managed vector db solution using Chroma and Local Embedding Generation. | [Prompt 2 Guidance](https://chatgpt.com/share/b5011cc2-e75b-47c4-af81-27f453b6849e) |


### Observations

1. [Chroma Setup](https://docs.trychroma.com/getting-started)
2. Install and run Docker Hub Image `chromadb/chroma:latest` 
3. See [ULIDs](https://cookbook.chromadb.dev/core/document-ids/#ulids)
    ```
    pip install py-ulid
    ```
3. Good [Sentence Transformers Article](https://medium.com/nlplanet/two-minutes-nlp-sentence-transformers-cheat-sheet-2e9865083e7a)

### Status
Solution works in that it connects a front-end with local vector database that is primed with locally processed data. This will not scale but it helps to learn some of teh solution components. 

The solution **does not** currently yield actual results. It is more of an operational example that **needs  tect analytics work**.

## Next Steps
1. Work on Text Analytics capabilities so that a query will actually result in a list of meaningful results. 
2. Consider chuncking the PDF docs into sentences. 
