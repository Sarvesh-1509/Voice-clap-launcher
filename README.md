\# Voice \& Clap controlled application launcher



A Python based system that listens for a voice keyword and clap patterns

to launch applications automatically.



\# How it works



1\. The system listens for a keyword (default: `jarvis`)

2\. After detecting the keyword, it listens for claps

3\. The number of claps determines which applications are launched



\# Architecture



\- `keyword\_listener.py` – voice keyword detection

\- `clap\_detector.py` – amplitude-based clap detection

\- `launcher.py` – application launcher

\- `config.json` – user-defined mappings



\# Configuration



Edit `config.json`:



```json

{

&nbsp; "keyword": "jarvis",

&nbsp; "actions": {

&nbsp;   "2": \["code"],

&nbsp;   "3": \["code", "https://chat.openai.com"]

&nbsp;   "4": \["notepad"]

&nbsp; }

}



