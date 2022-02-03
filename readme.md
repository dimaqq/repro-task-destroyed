# Task was destroyed but it is pending!

MRE for https://github.com/pgjones/hypercorn/issues/50

## How to

Terminal 1:
* `poetry shell`
* `poetry install`
* `hypercorn main:app`

Terminal 2:
* `time curl -v http://localhost:8000 --http2-prior-knowledge`
* responds correctly after 9.0x seconds
* `time curl -v http://localhost:8000 --http2-prior-knowledge`
* errors out after 5.0x seconds
