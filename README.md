curl --location 'http://localhost:8000/api/token/' \
--form 'username="admin"' \
--form 'password="demo1234"'

curl --location 'http://localhost:8000/api/place-order/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAyNDEyMTExLCJpYXQiOjE3MDI0MDg1MTEsImp0aSI6ImNkZWMzNjk5NDZhMzRhMTQ5YWYwZjliMjY2MWM0MWI5IiwidXNlcl9pZCI6MX0.kvUW3WrVuitevxGv8vbhrLumFW3JAzTg93kJsHHmXCE' \
--form 'product_id="2"' \
--form 'quantity="5"'

curl --location 'http://localhost:8000/api/order-items/5/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAyNDEyMTExLCJpYXQiOjE3MDI0MDg1MTEsImp0aSI6ImNkZWMzNjk5NDZhMzRhMTQ5YWYwZjliMjY2MWM0MWI5IiwidXNlcl9pZCI6MX0.kvUW3WrVuitevxGv8vbhrLumFW3JAzTg93kJsHHmXCE'

curl --location 'http://localhost:8000/api/orders' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAyNDEyMTExLCJpYXQiOjE3MDI0MDg1MTEsImp0aSI6ImNkZWMzNjk5NDZhMzRhMTQ5YWYwZjliMjY2MWM0MWI5IiwidXNlcl9pZCI6MX0.kvUW3WrVuitevxGv8vbhrLumFW3JAzTg93kJsHHmXCE'
