# Overview
For this project, I wanted to push myself a bit and build something that felt more like real-world software instead of just another small script. I’ve been trying to get better with networking, multithreading, and writing programs that actually communicate with each other, so I decided to make a simple Remote System Monitoring tool.

It’s made up of two pieces:

A server app that listens for incoming connections and logs whatever data clients send it.

A client app that grabs your system’s CPU, RAM, and battery usage and sends it over to the server in real time.

Using it is pretty easy: you start the server first, then run the client, type in the server’s IP, press Connect, and your machine starts streaming stats across the network. I really wanted to learn how all those moving parts work together and it definetly was difficult, but worth it.

My goal with this software was basically to learn by doing, to understand sockets better, to work with threads without everything crashing, and to manage configuration in a cleaner way using a .env file. Plus, building a GUI with Tkinter made everything feel more like a “real” app.

# Network Communication
The setup is a classic client/server structure. The server hangs out waiting for clients, and every new connection gets its own thread so the app doesn’t freeze whenever multiple clients are talking at once.

Everything runs over TCP, since I wanted the messages to arrive reliably and in order. By default, everything uses port 5050, but you can change that in the .env file if needed.

The messages themselves are simple text, nothing fancy, just a string that looks like:

CPU: <percent>% | RAM: <percent>% | Battery: <percent or N/A>

The server reads the text, shows it in the GUI, and logs it to a CSV file.

# Development Environment

* Python 3.13.5
* Tkinter for the GUI
* Socket (built-in Python standard library module)
* Threading (built-in Python standard library module)
* Psutil to grab system stats
* Python-dotenv to handle environment variables
* VS Code

# Useful Websites

* [Client-server model](https://en.wikipedia.org/wiki/Client%E2%80%93server_model)
* [TCP](https://www.howtogeek.com/190014/htg-explains-what-is-the-difference-between-tcp-and-udp/)
* [Server Libraries](https://docs.python.org/3.6/library/socketserver.html)
* [Socket Libraries](https://docs.python.org/3.6/library/socket.html)
* [Tkinter](https://docs.python.org/3/library/tkinter.html)
* [Psutil](https://psutil.readthedocs.io/en/latest/)
* [YouTube Socket Tutorial](https://www.youtube.com/watch?v=3QiPPX-KeSc)

# Future Work

* Add some sort of login/auth system
* Make the UI look way cleaner (Tkinter only goes so far…)
* Show graphs or charts of CPU/RAM history
* Add a feature to monitor disk usage, network speed, or temperature sensors.