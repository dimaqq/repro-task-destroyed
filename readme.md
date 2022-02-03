# Task was destroyed but it is pending!

MRE for https://github.com/pgjones/hypercorn/issues/50

## How to

Terminal 1:
* `poetry shell`
* `poetry install`
* `hypercorn main:app`

Terminal 2:
* `curl -v http://localhost:8000 --http2-prior-knowledge`
* repeat some 20 times
