
+# MY PERSONAL BLOG.
+ This app allows one to write their own blog.The users who have subscribed are able to view the writer's blog and even write a commet about it.The writer can also write a new blog or even edit their previous blogs.
+#### By **Canssidle** 
+
+## Description
+
+This Application is python based and runs on any browser, It allows a user to view and comment posts on my blog, for a writter can also register and start posting posts that will be commented by other users, the user can also subscribe to the app to be informed of a new post via their email, a writter can publish new posts, comment them, delete posts and comments on the posts he/she created.

+### Authentication
+
++ Once the url is entered at the browser, the user gets the landing page that has all the posts, the user can comment on the various posts, view all recent posts and subscribe.
++ For a Writter he can create a personal blog by registering and login. 
+- If the user is anonymouse, He/she can only view posts, comment and subscribe.
+- If the writter on the the other hand is Authnticated but logged out, can login again to interact with the app by entering email and password details into a form.
+- The user last option is to register using a unique username and a password after which the user is redirected to login to the app.
+- Once the user is authenticated, can logout at will.
+
+### Posts.
+
++ The Writter Can add Posts and they get displayed from the most resent one.
++ The post information is displayed alongside other posts, a post contains information such as post body, post author and the time of creation.
++ On the sidebar the user can see the most recent post.
+
+### Subscription
+
++ Any user who visits the site can subscribe by submitting his/her desired email via the subscription form.
+
+### Blog
++ The writter can also writter can also edit ther blog, post a new post, delete a post and any comment associated with it.
+
+## Bugs
+
+- Everything

+### prerequisites
++ First clone the project to your camputer. ```git clone <repo url>```
++ Ensure python3 is installed.
++ Install virtual environment by running ```pip3 install virtualenv```
++ Create a virtualenvironment by running ``` virtualenv <name of environment>``` on the terminal and once its activated by running ``` source <name of environment>/bin/activate``` then install all the packages by running ```pip3 install -r requirements.txt```
++ Then start the server by running ```python3 manage.py runserver```.
++ Copy the link and paste in any browser ```http://localhost:5000```
+
+

+## Technology and Tools Used
+
++ Python3.6 - Programming language
+- Flask - Python framework
+- Git - Version control
+- Visual Studio - Code editor

+## Further help
+To get Further help you can visit the official [python](https://www.python.org/) and [flask](http://flask.pocoo.org/ ) documentation.
+
+## Licence
+MIT (c) 2017 [canssidle](https://github.com/canssidle)