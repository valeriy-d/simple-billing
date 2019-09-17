# simple-billing
Simple billing implementation

### Run server
```bash
user@user:/../simple-billing$ docker-compose build
user@user:/../simple-billing$ docker-compose up -d
```

### Run unit tests with export to html
```bash
user@user:/../simple-billing$ docker-compose exec billing-api pytest --cov=./ --html=report.html
```

#### How to send request

Use [postman](https://www.getpostman.com/downloads/) for sending requests

Collection `SimpleBilling.postman_collection.json`


### Available endpoints

- /register-account/
- /balance/refill/

Request
```json

{
	"currency": "cad",
	"amount": 10.00000,
	"username": "jorah"
}
```
Response
```json
{
    "result": {
        "refill_amount": "10.0",
        "current_balance": "19.384100",
        "currency": "USD"
    }
}
```
- /currency/upload/

Request
```json
{
	"currency": "eur",
	"usd_exchange_rate": 1.115658
}
```
Response
```json
{
    "result": {
        "currency": "EUR",
        "usd_exchange_rate": "1.115658",
        "datetime": "2019-09-17T08:20:49.683Z"
    }
}
```
- /transfer-money/

Request
```json
{
	"username_from": "gertruda",
	"username_to": "jorah",
	"amount": 4,
	"currency": "usd"
}
```
Response
```json
{
    "result": "success"
}
```