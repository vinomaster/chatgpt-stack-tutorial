[toc]

### Problem 1
*ModuleNotFoundError: No Module Named openai*

### Solution

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


### Problemn 2
OpenAI Deprecated API.

### Solution 2
[OpenAI SDK Migration](https://github.com/openai/openai-python/discussions/742)

### Problem 3
Setting OpenAI API Key

### Solution 3

```
export OPENAI_API_KEY=sk-proj-zkmbQAHkUYodRgXAHI1pT3BlbkFJu6ZVbs92vlY9QKnmg6rv
```
### Problem 4
Integrated PDF data

### Solution 4
[See library docs](https://pypi.org/project/sentence-transformers/)

```
pip install -U sentence-transformers
```