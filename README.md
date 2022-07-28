# delete-data-magento2-api

To use the script you will need the Magento url and the api authentication code.

1) Rename the .env.example to .env and fill the varibals with the url and the auth.

2) In ACTION there are only two options(for now): product and address

3) Inside the files folder you leave the csv with the entity_id and parent_id column (this is only reference) of the customer_address_entity table or sku for products

5) Execute from the console

python3 main.py

If everything is ok, the response should be true, otherwise, there may be an authentication error or with the address
