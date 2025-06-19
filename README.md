# Superheroes API

A Flask API for tracking heroes and their superpowers.

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pipenv install
   pipenv shell
3. Initialize the database:
   ```bash
   flask db init
   flask db migrate -m "initial migration"
   flask db upgrade
4. Seed the database:
    ```bash
    python server/seed.py
5. Run the application:
    ```bash
    python server/app.py

## API Endpoints
GET /heroes - Get all heroes

GET /heroes/<id> - Get a specific hero with their powers

GET /powers - Get all powers

GET /powers/<id> - Get a specific power

PATCH /powers/<id> - Update a power's description

POST /hero_powers - Create a new hero-power association

## Models
Hero: name, super_name

Power: name, description (min 20 chars)

HeroPower: strength (must be 'Strong', 'Weak', or 'Average'), hero_id, power_id


## Testing the API

You can test the API using the Postman collection or with these sample requests:

```bash
# Get all heroes
GET http://localhost:5555/heroes

# Get a specific hero
GET http://localhost:5555/heroes/1

# Get all powers
GET http://localhost:5555/powers

# Get a specific power
GET http://localhost:5555/powers/1

# Update a power
PATCH http://localhost:5555/powers/1
Body (JSON):
{
  "description": "Updated description that is at least 20 characters"
}

# Create a hero_power
POST http://localhost:5555/hero_powers
Body (JSON):
{
  "strength": "Average",
  "power_id": 1,
  "hero_id": 3
}