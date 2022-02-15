# DT backend course

Launch project manually:
1. set up docker postgres container on localhost:5432 using following command:
`docker run -e POSTGRES_PASSWORD=<postgres_password> -p 5432:5432 -d <postgres_db_name>`
2. create .env file, fill it using template .env.example
3. export strings from .env: `export $(grep -v '^#' .env | xargs)`
4. launch server: `python src/manage.py runserver`
5. launch bot: `python src/manage.py runbot`
6. find bot @dt_backend_evenmonk_bot in telegram and send him `/start` command

### Bot commands  
- /start   
register user  
- /set_phone \<phone number>   
set phone number  
- /me     
get user info