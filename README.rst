Music
=====


- `python -m pip install requirements.txt` to install requirements
- `python -m music --add-dummy-data` to add dummy data
- `python -m music` to run server

Fallacies
---------

- No login system. Anyone can delete anyone's files. This is fine though since there's only one huge playlist everyone is looking at.
- Uploaded files' md5 calculation might become a bottleneck at large scale.  
- Search is clumsy right now. At larget workloads, we should create an inverted index or use a standard solution like elasticsearch.
