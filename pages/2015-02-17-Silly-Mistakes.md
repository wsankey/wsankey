title: Silly mistakes
date: 2015-02-17
categories: [general]
tags: [advice]
description: You will make them. It's your response that counts. 

Someone once told me their rationale for maintaining a blog was so they
could archive their mistakes, trip-ups, misunderstandings, and recall
how they overcame the problem. I appreciate this rationale and it's one
of the reasons I keep this going. The added benefit of writing down your
solution is that you'll know that at least one person was able to get
around that particular road block. And you'll have a record of it.

Though I have made plenty of mistakes over time I rarely have written
documentation of the problem and resolution. There are a few notable exceptions:
like when I learned the difference between the link href tag and the
script source tag, specifically the difference on the client side between: 
{% highlight html %}
<link href="javascript file" type="text/javascript">{% endhighlight %}
and 
{% highlight html%}
<script src="javascript file"></script>
{% endhighlight %} 
allowing me to finally render a D3 visualization I had been working on for the better part of a weekend. [Here's my tortured Stackoverflow thread if you'd like to see specifics.][1]

And I do have a recent example that kept me awake for a few nights. I've
been developing an [Ionic app walkthrough][2] and have been using Pluralsight
as a reference guide. Since this is my first time developing with Ionic
I've been leaning pretty heavily on these tutorials. I got to a point in
the tutorial where my app was suppose to look like this:

![good app pic](/assets/media/Good-app-pic.png)

But instead looked like this:

![bad app pic](/assets/media/Bad-app-pic.png)

It wasn't showing the results of the rendered page...and that seemingly
minor distinction completely derailed my flow. 

I thought the course was teaching old material (it was published  2014), I thought the instructor was
using a different emulator, I thought he was doing something different and keeping the extra code hidden. I was in the process of writing a strongly worded email to him and sinking the course rating, **my response to this mistake was ruining my progress.** It could've completely ruined this other person's day as well.

Needless to say I resolved the issue, I was missing a dash in a class name statement and the content was hiding *behind* the header. I came to my senses. I realized **my reaction was far worse than the mistake.** And had cost me a lot more wasted effort. This blog post is partially to tell my future self that when confronted with a similar situation, to

###Calm down, disengage, refresh yourself and then refocus

I have resolved far trickier problems with a little bit of exercise and
eight hours of sleep. 

Fortunately this mistake and the one I listed previously did not have significant repercussions. [There are far simpler mistakes you can make in a moment of carelessness that will cost you much more.][3] And I have made far worse. But the lesson is clear.  

###You will make these kinds of mistakes. It's your response that determines your success.

*I only link to this NY Times article because I read it today and it
completely terrified me.*

[1]: http://stackoverflow.com/questions/28269490/obtaining-static-json-data-in-d3-from-flask-app
[2]: http://willsankey.com/programming/2015/02/11/Ionic-Angular-Part1.html
[3]: http://www.nytimes.com/2015/02/15/magazine/how-one-stupid-tweet-ruined-justine-saccos-life.html 
