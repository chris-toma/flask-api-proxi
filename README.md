# flask-api-proxi

Run main file and make a postman call to `http://127.0.0.1:5000/nbnote_invoice` using base auth and `nbnotes_no` as user and pass.

User config structure:
```python
{
    "USERNAME": {
        "pass": "PASS", 
        "routes": {
            "/ROUTE_1",
            "/ROUTE_2",
        }
    },
}
```
