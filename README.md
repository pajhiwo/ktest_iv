# Execute tests
## Set following environment variables
* API_URL - `format: https://<domain>.com`
* API_KEY - `API Keys 2FA Settings`
* API_SEC - `API Keys 2FA Settings`
* PASS_2FA - `API Keys 2FA Settings - static password`

## Start container
```bash
docker compose build
docker compose up
```

## Reports
After docker compose up, reports will be available inside `reports` folder