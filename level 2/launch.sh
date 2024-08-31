#!/bin/bash
python server.py &
sleep 2
python c1.py &
python c2.py &
python c3.py &
wait
