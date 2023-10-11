broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost/1'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
# timezone = 'Europe/Oslo'
enable_utc = True

result_extended=True