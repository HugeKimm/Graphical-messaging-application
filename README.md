# Graphical-messaging-application

This project sets up a messaging application using MQTT to publish and subscribe to messages, and Tkinter to manage the user interface. The functions allow publishing messages, subscribing to and unsubscribing from MQTT topics, and display the current messages and subscriptions in a graphical interface.

## Installation

We need to install pip because it is the package installer for Python.
Pip allows us to easily install and manage additional libraries and dependencies 
that are not included in the Python standard library. By using pip, 
we can ensure that our project has access to all the required modules 
and that they are up-to-date. This is especially important for maintaining 
the functionality and security of our application.

```http
pip install paho-mqtt
```
After installation, you can verify if the module is properly installed by opening a Python session and trying to import it:

``import paho.mqtt.client as mqtt``
