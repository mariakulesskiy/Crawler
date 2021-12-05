# Crawler

The crawler crawls the site: https://pastebin.com/ and store the most recent "pastes" to mongoDb.
Database collection: posts
Data Structure:
- Author - String
- Title - String
- Content - String
- Date - Date

## Run with Docker
cd to Crawler folder
`docker-compose up`

## Run local with custom MongoDb database
update MONGO_CONNECTION_STRING in src\config.py file
Run 'python src\app.py'
