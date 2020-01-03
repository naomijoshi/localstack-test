## Step 1
Run 
`docker-compose up -d`

## Step 2
Monitoring the logs using
``docker logs -f CONTAINER_NAME``

## Step 3
Execute aws cli command to create-stack

``` 
aws cloudformation create-stack \
--template-body file://template.yaml \
  --stack-name cfn-test \
  --parameters ParameterKey=BucketPrefix,ParameterValue=demo-bucket \
  --endpoint-url=http://localhost:4581 \
  --capabilities CAPABILITY_IAM
  ```
  ### Error after cloudformation create-stack
  `An error occurred (502) when calling the CreateStack operation (reached max retries: 4): Bad Gateway`
  
  Stacktrace
  ```
  2020-01-02T21:05:40:ERROR:localstack.services.generic_proxy: Error forwarding request: 'list' object has no attribute 'split' Traceback (most recent call last):
  File "/opt/code/localstack/localstack/utils/cloudformation/template_deployer.py", line 342, in parse_template
    return json.loads(template)
  File "/usr/lib/python3.7/json/__init__.py", line 348, in loads
    return _default_decoder.decode(s)
  File "/usr/lib/python3.7/json/decoder.py", line 337, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
  File "/usr/lib/python3.7/json/decoder.py", line 355, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/opt/code/localstack/localstack/utils/cloudformation/template_deployer.py", line 346, in parse_template
    return yaml.safe_load(template)
  File "/opt/code/localstack/.venv/lib/python3.7/site-packages/yaml/__init__.py", line 162, in safe_load
    return load(stream, SafeLoader)
  File "/opt/code/localstack/.venv/lib/python3.7/site-packages/yaml/__init__.py", line 114, in load
    return loader.get_single_data()
  File "/opt/code/localstack/.venv/lib/python3.7/site-packages/yaml/constructor.py", line 43, in get_single_data
    return self.construct_document(node)
  File "/opt/code/localstack/.venv/lib/python3.7/site-packages/yaml/constructor.py", line 52, in construct_document
    for dummy in generator:
  File "/opt/code/localstack/.venv/lib/python3.7/site-packages/yaml/constructor.py", line 404, in construct_yaml_map
    value = self.construct_mapping(node)
  File "/opt/code/localstack/.venv/lib/python3.7/site-packages/yaml/constructor.py", line 210, in construct_mapping
    return super().construct_mapping(node, deep=deep)
  File "/opt/code/localstack/.venv/lib/python3.7/site-packages/yaml/constructor.py", line 135, in construct_mapping
    value = self.construct_object(value_node, deep=deep)
  File "/opt/code/localstack/.venv/lib/python3.7/site-packages/yaml/constructor.py", line 94, in construct_object
    data = constructor(self, tag_suffix, node)
  File "/opt/code/localstack/.venv/lib/python3.7/site-packages/moto/cloudformation/utils.py", line 61, in yaml_tag_constructor
    return {key: _f(loader, tag, node)}
  File "/opt/code/localstack/.venv/lib/python3.7/site-packages/moto/cloudformation/utils.py", line 50, in _f
    return node.value.split(".")
AttributeError: 'list' object has no attribute 'split'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/opt/code/localstack/localstack/services/generic_proxy.py", line 242, in forward
    path=path, data=data, headers=forward_headers)
  File "/opt/code/localstack/localstack/services/cloudformation/cloudformation_listener.py", line 164, in forward_request
    modified_request = transform_template(req_data)
  File "/opt/code/localstack/localstack/services/cloudformation/cloudformation_listener.py", line 71, in transform_template
    parsed = template_deployer.parse_template(template_body)
  File "/opt/code/localstack/localstack/utils/cloudformation/template_deployer.py", line 348, in parse_template
    return yaml.load(template, Loader=NoDatesSafeLoader)
  File "/opt/code/localstack/.venv/lib/python3.7/site-packages/yaml/__init__.py", line 114, in load
    return loader.get_single_data()
  File "/opt/code/localstack/.venv/lib/python3.7/site-packages/yaml/constructor.py", line 43, in get_single_data
    return self.construct_document(node)
  File "/opt/code/localstack/.venv/lib/python3.7/site-packages/yaml/constructor.py", line 52, in construct_document
    for dummy in generator:
  File "/opt/code/localstack/.venv/lib/python3.7/site-packages/yaml/constructor.py", line 404, in construct_yaml_map
    value = self.construct_mapping(node)
  File "/opt/code/localstack/.venv/lib/python3.7/site-packages/yaml/constructor.py", line 210, in construct_mapping
    return super().construct_mapping(node, deep=deep)
  File "/opt/code/localstack/.venv/lib/python3.7/site-packages/yaml/constructor.py", line 135, in construct_mapping
    value = self.construct_object(value_node, deep=deep)
  File "/opt/code/localstack/.venv/lib/python3.7/site-packages/yaml/constructor.py", line 94, in construct_object
    data = constructor(self, tag_suffix, node)
  File "/opt/code/localstack/.venv/lib/python3.7/site-packages/moto/cloudformation/utils.py", line 61, in yaml_tag_constructor
    return {key: _f(loader, tag, node)}
  File "/opt/code/localstack/.venv/lib/python3.7/site-packages/moto/cloudformation/utils.py", line 50, in _f
    return node.value.split(".")
AttributeError: 'list' object has no attribute 'split'
```

#### Note: s3 and lambda cli commands are working fine individually
