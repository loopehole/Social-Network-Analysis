#!/bin/bash
# chmod +x test_api.sh -> make it executable
# ./test_api.sh -> to run this script

# Function to make a POST request to add a user
add_user() {
    local username=$1
    echo "Adding user: $username"
    curl -X POST "http://127.0.0.1:8000/add_user" -H "Content-Type: application/json" -d "{\"username\": \"$username\"}"
    echo
}

# Function to make a POST request to add a friend
add_friend() {
    local user1=$1
    local user2=$2
    echo "Adding friend relationship between: $user1 and $user2"
    curl -X POST "http://127.0.0.1:8000/add_friend" -H "Content-Type: application/json" -d "{\"user1\": \"$user1\", \"user2\": \"$user2\"}"
    echo
}

# Function to make a GET request to retrieve friends of a user
get_friends() {
    local username=$1
    echo "Retrieving friends of: $username"
    curl -X GET "http://127.0.0.1:8000/friends/$username"
    echo
}

# Adding users
add_user "Alice"
add_user "Bob"

# Adding a friend relationship
add_friend "Alice" "Bob"

# Retrieving friends of a user
get_friends "Alice"
