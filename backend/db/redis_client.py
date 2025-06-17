import redis

# Change port to 6380 if you modified docker-compose.yml
redis_client = redis.Redis(host='localhost', port=6380, decode_responses=True)

# Optional: test connection
try:
    redis_client.ping()
    print("✅ Connected to Redis successfully.")
except redis.exceptions.ConnectionError:
    print("❌ Failed to connect to Redis.")
