from batch import BatchRequest

batch_request_manager = BatchRequest([
    'http://httpbin.org/ip',
    'http://httpbin.org/get',
])

batch_request_manager.run()

responses = batch_request_manager.responses

print(responses)
