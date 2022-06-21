# Batch Requests

Make batch http requests.

## Usage

### Install package
`pip install batch-requests` or `conda install batch-requests` or `pip3 install batch-requests`

```python3
from batch import BatchRequest

batch_request_manager = BatchRequest([
    'http://httpbin.org/ip',
    'http://httpbin.org/get',
])
batch_request_manager.run()
responses = batch_request_manager.responses
print(responses)
```
