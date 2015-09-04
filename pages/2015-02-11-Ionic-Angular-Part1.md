title: Building an app with Ionic and Angular - Part 1
categories: [programming]
tags: [angular, ionic]
description: Follow along as I build an app a researcher might use in the field to collect survey data from participants.


This is the first post in a series for building an iOS app using Ionic
and Angular.js. The basic idea is to create an app that a researcher could have participants install to collect information from them at random points in the day. For example, someone studying smoking habits might have a question pop up randomly during the day asking if they already had a cigarette or how intense their craving was at that particular moment. 

Before beginning you need to have Node.js installed. There are plenty of online tutorials
for installing Node on your machine and I won't go through the steps
here. Regardless it's a fairly painless installation process. 

After installing Node.js let's go to our terminal and install Ionic and
Cordova (for accessing some native phone functionality):<br>
`npm install ionic -g`<br>
`npm install cordova -g`

And that's it. We're ready to start using Ionic. 

Let's build out the app using a blank template. 

`ionic start researcher blank`

This gives us a folder for our new app 'researcher.' Now we'll make sure
everything is working. CD into your directory and check your app is
working by typing `ionic serve` into your terminal. Using a browser to visit the address the terminal returns (mine is localhost 8100) you'll see the Ionic starter kit, a very sparse
app structure...but it works!

After checking this works, let's open the index.html script from the 'www' subfolder.

Where you see `<ion-pane>` add in the following:
{% highlight html %} 
   <ion-pane>
      <ion-header-bar class="bar-stable">
        <h1 class="title">Ionic Researcher</h1>
      </ion-header-bar>
      <ion-content>
      </ion-content>

      <ion-tabs class="tabs-energized tabs-icon-top">
        <ion-tab title="Home" icon="ion-earth" href="#">
        </ion-tab>
        <ion-tab title="Survey" icon="ion-document" href="#">
        </ion-tab>
        <ion-tab title="Account" icon="ion-settings" href="#">
        </ion-tab>
       </ion-tabs>
      </div>
    </ion-pane>
{% endhighlight %}

Note that there are plenty of other free Ion icons available online at
ionicons.com, just search for what you need. For example, instead of
`ion-earth` I could use `ion-pizza` (which is an icon on that site) and
have some pizza navigation.

If you have been following up to this point you should be seeing
something very similar to the following in your browser: <br>
![Ionic-App](/assets/media/Basic-Ionic-App.png)

Next time we'll be able set some of our routes and views for this app
and think through exactly what kind of functionality we'll need. At
least we have the basics done!

Here are some terminal commands that we'll be needing as we continue to
use Ionic:

* **start** - start a new project
* **serve** - starts local server
* **platform** - configures our platform
* **build** - builds the app locally
* **emulate** - emulates the app in a simulator
* **run** - runs the app on a development server
