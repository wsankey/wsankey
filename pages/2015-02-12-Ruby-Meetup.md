title: D.C. Ruby Meetup, Salesforce and Lambdas
categories: [programming]
tags: [meetups, ruby]
description: Notes from the February Ruby Meetup in D.C.

*Note: Meetups are great, this meetup
featured free fleece jackets. Thanks Logickull.*<br>

Two presenters gave talks at this month's D.C. Ruby Meetup. The first,
P. Steininger of SocialDriver talked about integrating Salesforce, a Customer Relationship Management (CRM) service, with Rails.
The second speaker, Keith Bennett, gave a riveting talk on the power of
using Lambdas in Ruby. 

#Salesforce and Rails

*Presenter: P. Steininger*

This talk was mainly focused on how to work with Salesforce even though
you probably won't like it. At the end the speaker introduced us to an open
source gem their team is creating to help more cleanly integrate Salesforce
and Rails. 

**What is Salesforce?**<br>
Salesforce is primarily a CRM but has a development platform associated with it. There is
a developer edition for Salesforce where anyone can sign up for free and
play around.<br> 
**Why would I want to use Salesforce?**<br> Because your clients
wants it.<br> 
**How can I use it with Rails?**<br> You can use the DatabaseDotCom gem but this
hasn't been updated since 2009. In the near future the SocialDriver team
will release an updated gem. 

Using Lambdas in Ruby
---
*Presenter: Keith Bennett*

I really enjoy watching Keith talk because he's so passionate
about his craft. Keith gave his talk on Ruby lambdas, which I've seen
before at a meetup lightning round and which he's presented at other
conferences. He begins by stating that lambdas, free floating functions not associated with
an object or class, help bridge the gap between the Functional and
Object Oriented world. The idea is to incorporate the best of Functional
Programming into the Object Oriented domain.

Essentially lambdas reduces the complexity in your code by reducing our
dependency on formally state objects. For example, one might create an
'is it even or odd' filter by designing Even and Odd classes, creating
instances of those classes, and passing a set of parameters to those
instances, as shown below:

{% highlight ruby %}

class EvenFilter
  def filter(n)
    n.even?
  end
end
 
class OddFilter
  def filter(n)
    n.odd?
  end
end
 
even_filter = EvenFilter.new
odd_filter  = OddFilter.new
[1,2].each do |n|
  puts "Is #{n} even?: #{even_filter.filter(n)}"
  puts "Is #{n} odd?:  #{odd_filter.filter(n)}"
end

{% endhighlight %}
 
Yet, there's really no need for the verbosity. With lambdas we remove
the formal classes and let the functions act by themselves (though they
are still objects). We refactor the above code to the following:

{% highlight ruby %}

even_filter = ->(n) {n.even? }
odd_filter = ->(n) { n.odd? }

[1,2].each do |n|
  puts "Is #{n} even using lambdas?: #{even_filter.(n)}"
  puts "Is #{n} odd using lambdas?: #{odd_filter.(n)}"
end

{% endhighlight %} 

I won't reproduce Keith's talk here, [you can view his slides here][1] and
the [code he demonstrated here.][2]

[1]: https://speakerdeck.com/keithrbennett/ruby-lambdas-steel-city-ruby-conf-aug-2014
[2]: https://gist.github.com/keithrbennett/0df037c29198ab401cf8
