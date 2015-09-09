title: DC Django-district Meetup - Python Websockets
date: 2015-03-17
categories: [meetup, python]
tags: [data]
description: The March DC Django-district meetup with Matt Makai held at iStrategyLabs


The following are my notes from the March DC Django-district meetup on websockets with python, presented by Matt Makai (@mattmakai) of Twilio. Matt Makai also maintains [**Full Stack Python**][1].

*Note: These notes might be incomplete.*

###[Asynchronous Python Web Apps with WebSockets][3]

To summarize, the core idea for the talk was:

*If you want full communication between the browser and the server this
is how to do it without resorting to Node.js*

The idea is to get a WSGI server to invoke the python code you've
written. WSGI is a blocking interface, meaning that every time a request
arrives the server will process the request and be done. In the context
of the historical world wide web this made sense.

###The old days

In the beginning, the web browser communicates with the web server. The server would
simple return back static files and that's ok *if you only have static
files.*

But if you want dynamic applications you need something more - the WSGI
server interface. When you run a Flask or Django application the web
server, WSGI, acts as a proxy - it runs some python and returns back
something: HTML, JSON, etc. 

Around 2005 AJAX was introduced, giving us richer applications. In this
regime we are able to retrieve data from the backend: [Long Polling.][2] E.g. Having Facebook pdates coming in to your feed. However, this was problematic and the web community responded with:

###Async

Async can keep the communication open between the client and the server.
Before we had Long Polling with AJAX (a constant checking for updates).
But we wanted a way of passing data between server and browser. Async
keeps that connection open.

There are differetn ways of doing this - we've usually resorted to
Node.js but we can use python solutions, like **gevent**

###Live Coding Example

**See python-websockets-example from Github**

The libraries being used:

* Flask
* Flask-socketio (written by person who wrote O'Reilly Flask book)
* Redis

Create an empty repository, install those libraries, and then

{% highlight python %} 
pip freeze 
{% endhighlight %}

the dependencies 

The python code for the older style of application:


{% highlight python %} 
import redis
from flask import Flask, render_template

app = Flask(__name__)
db = redis.StrictRedis('localhost', 6379, 0)

@app.route('/')
def main():
  c = db.incr('user_count')
  return render_template('main.html', counter=c)

if __name__ == "__main__":
  app.run(debug=True)

{% endhighlight %}


And then we code custom to render our python script (*[from here on out
you should refer to Matt's repository for the code, I won't copy and
paste it.][4]*)

[The HTML template.][5]

Ok, so the example works but we can improve it using Async libraries.

##Let's do it with Socketio

Lot of code but essentially we submit the form as SocketIo and not HTML.

The server is getting information and serving it out, but now we can use
socketio.emit to have the server send it out to all other web browsers
connecting.

Matt is presenting at this year's [pycon in Montreal][6] and I'll be
sure to post his talk here when it's complete.

[1]: http://www.fullstackpython.com/
[2]: http://en.wikipedia.org/wiki/Push_technology
[3]: http://www.mattmakai.com/presentations/2015-async-web-apps-django-district.html#/
[4]: https://github.com/makaimc/python-websockets-example
[5]: https://github.com/makaimc/python-websockets-example/blob/master/templates/main.html
[6]: https://us.pycon.org/2015/schedule/
