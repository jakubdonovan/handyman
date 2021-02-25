<a href="">
    <img src="https://i.ibb.co/R0Z6gB4/logo.png" alt="3P logo" title="3P" align="right" height="120" />
</a>

<h1 style="margin-top:24px;"><b>HANDYMAN</b></h1>

<h3>The marketing, checkout & product delivery pages.</h3>

<p>
Handyman is an open-source SaaS. Originally developed for a bootcamp project, the joint focus was to also make a buck.
</p>

<h5>You can view the product <a href=''>here.</a></h5>

<br> </br>

<p align="center">
<img src="https://i.ibb.co/f9rRMhj/handyman-marketing-page-capture.webp">
</p>

<br></br>

<h3><b>Deploy it</b></h3>

You're going to need:

<ol>
 <li>an rdp with dokku installed </li>
 <li> You then need to make a dokku app </li>
 <li>The dokku postges plugin installed and connected to your app</li>
 <li>A domain thats connected to the app </li>
 <li>Finally, you need to install and setup the dokku lets encrypt plugin</li>
 
 <br> </br>
</ol>
<b> Once Done</b>

Fork the project and add the ssh key to your server <a>here</a>.

Now every push to github will be deployed to your domain on dokku.

<br></br>

<h3><b>Run locally</b></h3>

You're going to need the following on your dev machine:

<ol>
    <li> Node 12+ </li>
    <li> Python 3.9 </li>
    <li> Poetry 1+ </li>

</ol>
    <br> </br>

Then simply run:

<pre>
    <code>
    poetry install
    poetry run python3.9 manage.py liveserver
    </code>
</pre>
