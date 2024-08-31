#!/bin/bash

# Launch the server in the background
python server.py &

# Wait a few seconds to ensure the server starts before the clients connect
sleep 2

# Launch the first client
python c1.py &

# Launch the second client
python c2.py &

python c3.py &
# Wait for the clients to finish
wait
