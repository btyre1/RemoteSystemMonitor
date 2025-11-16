# Overview
For this project, I wanted to push myself a bit and build something that felt more like real-world software instead of just another small script. I’ve been trying to get better with networking, multithreading, and writing programs that actually communicate with each other, so I decided to make a simple Remote System Monitoring tool.

It’s made up of two pieces:

A server app that listens for incoming connections and logs whatever data clients send it.

A client app that grabs your system’s CPU, RAM, and battery usage and sends it over to the server in real time.

Using it is pretty easy: you start the server first, then run the client, type in the server’s IP, press Connect, and your machine starts streaming stats across the network. I really wanted to learn how all those moving parts work together and it definetly was difficult, but worth it.

My goal with this software was basically to learn by doing, to understand sockets better, to work with threads without everything crashing, and to manage configuration in a cleaner way using a .env file. Plus, building a GUI with Tkinter made everything feel more like a “real” app.

# Network Communication

{Describe the architecture that you used (client/server or peer-to-peer)}

{Identify if you are using TCP or UDP and what port numbers are used.}

{Identify the format of messages being sent between the client and server or the messages sent between two peers.}

# Development Environment

{Describe the tools that you used to develop the software}

{Describe the programming language that you used and any libraries.}

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Web Site Name](http://url.link.goes.here)
* [Web Site Name](http://url.link.goes.here)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}
* Item 1
* Item 2
* Item 3