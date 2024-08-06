from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from .models import db

router = APIRouter()

class User(BaseModel):
    username: str

class Friendship(BaseModel):
    user1: str
    user2: str

@router.post("/add_user")
def add_user(user: User):
    query = "CREATE (a:User {name: $username})"
    params = {"username": user.username}
    db.query(query, params)
    return {"status": "User added"}

@router.post("/add_friend")
def add_friend(friendship: Friendship):
    query = (
        "MATCH (a:User {name: $user1}), (b:User {name: $user2}) "
        "CREATE (a)-[:FRIENDS_WITH]->(b)"
    )
    params = {"user1": friendship.user1, "user2": friendship.user2}
    db.query(query, params)
    return {"status": "Friendship created"}

@router.get("/friends/{username}")
def get_friends(username: str):
    query = (
        "MATCH (a:User)-[:FRIENDS_WITH]->(b) WHERE a.name = $username "
        "RETURN b.name AS friend"
    )
    params = {"username": username}
    result = db.query(query, params)
    friends = [record["friend"] for record in result]
    return {"friends": friends}
