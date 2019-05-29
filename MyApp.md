**Data & The Web - Final Coursework - My Flask App - SHAKIL ALI - README**

___________________________________________________________________________

**My App URL (Click once the app.py file is running):** http://doc.gold.ac.uk/usr/288

**If you are unable to run my application, please watch the video I have created, as advised by Dr.Vala:** http://doc.gold.ac.uk/~sali011/dnw/FlaskApp/sali011FlaskApp.mp4

**Or download the video here:**  http://doc.gold.ac.uk/~sali011/dnw/FlaskApp/sali011FlaskApp.zip

**Final App Directory:** myapp

**Test Login Credentials:**

**Username:** test123

**Password:** testpassword

**Backup Login Credentials:**

**Username:** sali011

**Password:** password

**NOTE:** If any of the given login credential attempts fail, just register a new account

**COMMIT HISTORY:**

Sali011 commit history link: https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/commits/master


___________________________________________________________________________

**INTRODUCTION:**

My app has been developed through a series of Dr.Vala's lectures, lab assistant's guidance, code demos, videos. As well as this I have used the flask documentation (http://flask.pocoo.org/docs/1.0/) and a series on youtube (https://www.youtube.com/watch?v=zRwy8gtgJ1A)

I developed my initial skill set from the beginning of term, through the combination of completing weekly lab exercises, as well as ensuring to come to lectures. In addition, the live demos gave me an insight into how to integrate code in my own work. Futhermore, the vast online resources also allowed to specialise in certain apsects of Flask and web application creation. My code has been written week by week, according to what the lab session was regarding. I have to the best of my ability applied Separation of Concerns throughout my work. Also, via the principle of DRY (Dont-Repeat-Yourself) I have been able to code in such a way as to limit code reptition and make code reading/viewing efficient. After utilising the many outlets I had possible to lear more about Flask Application, I decided to test out my new skills. I have looked at code examples, and tried to adapt and see how I could make it better or different (at best). Examples of this will be seen throughout my work.

**NOTE:** When specifying the line numbers for code, below in my table, please click the blue fonted, red higlighted links. These will take you to the exact line of code and directory. If a link fails, please just visit the directory, file and line(s) mentioned. Thanks in advance.

___________________________________________________________________________


**SUBMISSION INSTRUCTIONS:**

| **SUBMISSION INSTRUCTIONS** | **STATUS(COMPLETE/NOT COMPLETE)** |
| --- | --- |
| App run's without debug=True | ✔ |
| Your app process should run in the background: use 'python3 YOUR-APP-NAME &' | ✔ |
| The url for your app should be in a README.txt (README.md) | ✔ |
| Any login credentials should be in the README | ✔ |
| You should include a clear statement in the README submitted that describes what you have done | ✔ |
| Your app should be in the top level of your repo in "my app" subdirectory | ✔ |
| All the rest of your code for the term should be in subdirectories (lab-12, lab-13, ...) | ✔ |
| You should give master access to your repo to the following gitlab accounts: @ehoma001 and TAs (I will announce their gitlab accounts later) | ✔ |
| Check this page before submission not missing any updates on this page |  ✔  | 


___________________________________________________________________________


**DETAILED CRITERIA FOR APP**

| **APP CRITERIA** | **EXTRACT** | **DIRECTORY, FILE AND LINE NUMBER** | **DESCRIPTION** | **STATUS(COMPLETE/NOT COMPLETE)** |
| --- | --- | ---| --- | --- |
| 1) It is a flask app | Extract 1 | app.py (lines 3, 31, 172, 534) `app.py`[`Line 3`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L3)  [`Line 31`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L31) [`Line 172`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L172) [`Line 524`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L534) | The import statements signify that I am importing modules which are specific to a flask application. Next I have on line 26 created an instance of the Flask class for my web app. Line 136 is an exampple of an app route, and below is a function, which is a typical aspect of a flask app. The final line shows that Python assigns the name "main" to the script, when the script is getting executed. | ✔ |
| 2) There is more than one route and more than one view | Extract 2 | app.py (lines 172, 180, 187, 211, 225, 239, 253, 263, 310, 361, 375, 404, 434, 480, 503, 504) `app.py`[`Line 172`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L172) [`Line 180`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L180) [`Line 187`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L187) [`Line 211`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L211) [`Line 225`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L225) [`Line 239`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L239) [`Line 253`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L253) [`Line 263`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L263) [`Line 310`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L310) [`Line 361`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L361) [`Line 375`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L375) [`Line 404`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L404) [`Line 434`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L434) [`Line 480`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L480) [`Line 503`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L503) [`Line 504`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L504) | In app.py, all throughout, you can see many app routes/views. For example, for the home page I have created an @app.route('/'), for the about page I have created an @app.route('/about') etc. | ✔ |
| 3) The html is rendered using jinja templates | Extract 3 | TEMPLATES/(all files in templates directory render templates via jinja, except layout.html) | Within the templates file, there are many html files. All of these files (except layout.html) have jinja templates. An example of the jinja templates in add_article: {% extends 'layout.html' %}, {% block body %}, {% from "includes/_formhelpers.html" import render_field %}, {{ render_field(form.title, class_="form-control") }} etc. | ✔ | 
| 4) The jinja templates include some control structure | Extract 4 | TEMPLATES/(most files in templates directory have jinja templates with control structure and in INCLUDES). (lines 15 from home.html and lines 31 in _navbar.html) `home.html`[`Line 15`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/templates/home.html#L15) `_navbar.html`[`Line 31`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/templates/includes/_navbar.html#L31) | For example, within home.html (inside templates), we can see on the specified lines that a conditional if (control structure) is used to check if a user is logged in, if not it will display a different home.html page | ✔ |
| 5) It includes one or more forms | Extract 5 | classes.py (lines 11, 25) `classes.py`[`Line 11`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/classes.py#L11) [`Line 25`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/classes.py#L25) | Within the classes.py file you can see two classes which handle forms: RegisterForm and ArticleForm. | ✔|
| 6) The forms have some validation | Extract 6 | classes.py (lines  2, 13, 15, 17, 19, 21, 27, 29) `classes.py`[`Line 2`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/classes.py#L2) [`Line 13`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/classes.py#L13) [`Line 15`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/classes.py#L15) [`Line 17`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/classes.py#L17) [`Line 19`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/classes.py#L19) [`Line 21`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/classes.py#L21) [`Line 27`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/classes.py#L27) [`Line 29`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/classes.py#L29) | Inside classes, as the very top there are imports for validators. Also when the titles, body, author etc are being assigned to the form data value, they are being validated to check for length, sometimes match and for the bottom two if data is entered at all. For example: name = StringField('Name', [validators.length(min=1, max=50)]), password = PasswordField('Password', [validators.DataRequired(),validators.EqualTo('confirm', message='Passwords do not match')]) etc | ✔ |
| 7) There are useful feedback messages to the user | Extract 7 | app.py (line 3, 287, 299, 336, 369, 426, 454, 472, 494) `app.py`[`Line 2`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L3) [`Line 287`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L287) [`Line 299`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L299) [`Line 336`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L336) [`Line 369`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L336) [`Line 369`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L369) [`Line 426`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L426) [`Line 454`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L454) [`Line 472`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L472) [`Line 494`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L494) and TEMPLATES/INCLUDES/_messages.html (lines 1 - 15)  `templates/includes/_messages.py`[`Line 1-15`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/templates/includes/_messages.html#L1) | There are many flash messages used throughout the code in app.py. On the specified line you can see how the flash message displays a message and uses boostrap to highlight which sort of alert it is (e.g. success - green and danger - red). I also have a _messages.html file in my INCLUDES directory, which displays a flash message depending on the scenario. Example: flash('Username Taken', 'danger') | ✔ |
| 8) It has a database backend that implemenets CRUD operations | Extract 8 | app.py (lines 189, 265, 408, 438, 484) `app.py`[`Line 189`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L189) [`Line 265`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L408) [`Line 2`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L408) [`Line 438`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L438) [`Line 484`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L484) | This extract shows the app routes which contain and deal with CRUD (Create, Read, Update and Delete) operations. 'articles' function and html allows users to see (READ) all articles. Add_article allows users to add (CREATE) an article. Edit_article allows users to edit an article (UPDATE). Delete_article allows users to delete (DELETE) an article. | ✔ |
| 9) The create and update operations take input data from a form | Extract 9 | app.py (lines 414, 416, 448, 450) `app.py`[`Line 414`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L414) [`Line 416`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L416) [`Line 448`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L448) [`Line 450`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L450) | The app route for the create and update functions take input data as seen on the lines specified. These values are then stored (if new from is being added to the database) or updated (if old form is being edited). They are stored or updated using the following syntax: form.name_of_field.data e.g. name = form.name.data | ✔ |
| 10) There is user authentication | Extract 10 | app.py (line 314, 316, 318, 330, 328, 330, 332, 334, 336, 338, 340, 342, 344, 348, 350, 352)  `app.py`[`Line 314`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L314) [`Line 316`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L316) [`Line 318`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L318) [`Line 330`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L330) [`Line 328`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L328) [`Line 332`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L332) [`Line 334`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L334) [`Line 336`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L336) [`Line 338`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L338) [`Line 340`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L340) [`Line 342`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L342) [`Line 344`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L344) [`Line 348`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L348) [`Line 350`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L350) [`Line 352`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L352) assistant_function.py (lines 8-24) `assist_function.py`[`Lines 8-24`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/assist_function.py#L8) | The extract and lines specifed show how the user authentication works. It checks to see whether the user has got credentials which are in the database. If not it will display redirect them to the login page to try again. The use of sha256_crypt.verfy enables the salt to be added to the password entered, and check if it matches the actual password plus the salt, stored in the database. If not, user will be redirected. | ✔ |
| 11) The login process uses sessions | Extract 11 | app.py (lines 332 and 334) `app.py`[`Line 332`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L332) [`Line 334`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L334)  assist_function (line 14) `assistant_function.py`[`Line 14`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/assist_function.py#L14) | The extract and lines show how the code makes use of sessions to check if the user is currently within a session. It will display a success message to the user if they are. Else the user will have a failure message displayed. | ✔ |
| 12) Passwords are stored as hashes | Extract 12 | app.py (lines 278) `app.py`[`Line 278`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L278) | The lines and extract show how the password is encrypted via sha256. This adds a salt to the password (by default) before hashing and storing it. Therefore, reducing the chances of being 'guessed' by intruders or hacked via rainbow tables. | ✔ |
| 13) There is a way to logout | Extract 13 | app.py (line 361) `app.py`[`Line 361`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L361) | The app route in app.py, on the lines specified, show that there is a page and function that deals with logging out. It informs the user once they have logged out, via a flash message and redirects them to the login page. It also has the @is_logged_in decorator wrapping it. | ✔ |
| 14) There is a basic API. Content can be accessed as json via http methods | Extract 14 | app.py (lines 502 and 504) `app.py`[`Line 502`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L502) [`Line 504`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L504) | The simple api can be accessed via the app route '/api'. It can be seen on the nav bar. It will display all the articles present on the web application. In addition, if you click on the url and pass a username (e.g. sali011) as an extra argument, it will display all articles written by that individual (all articles by sali011) | ✔ |
| 15) It should be clear how to access the API | Extract 15 | app.py (line 90, 94, 110, 129, 150) `app.py`[`Line 90`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L90) [`Line 94`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L94) [`Line 110`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L110) [`Line 129`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L129) [`Line 150`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L150) | The simple api is explained above. For the restful api, first run the app.py file in one terminal. Then open another separate terminal (DO NOT SSH INTO UBUNTU, YOU CAN DO IT FROM THE TERMINAL). Once that is open, look at the instructions below for the restful api and how to implement CRUD operations, via commands on the terminal. | ✔ |


___________________________________________________________________________

**EXTRA APP CRITERIA (EXTENSION FOR 10%):**

| **EXTENSION CRITERIA** | **EXTRACT** | **DIRECTORY, FILE AND LINE NUMBER** | **DESCRIPTION** | **STATUS(COMPLETE/NOT COMPLETE)** |
| --- | --- | --- | --- | --- |
| using wtforms is not required but is recommended | EXTRACT 16 | app.py (line 8, 11, 537) `app.py`[`Line 8`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L8) [`Line 11`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L11) [`Line 537`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L537) and classes.py (lines 13, 15, 17, 19, 21, 27, 29) `classes.py`[`Line 13`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/classes.py#L13) [`Line 15`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/classes.py#L15) [`Line 17`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/classes.py#L17) [`Line 19`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/classes.py#L19) [`Line 21`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/classes.py#L21) [`Line 27`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/classes.py#L27) [`Line 29`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/classes.py#L29) | I have used wtforms in my app.py and classes file. I used it to validate my forms | ✔ |
| use of flask-login is not required but is recommended | EXTRACT 17 | app.py (lines 6) `app.py`[`Line 6`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L6) assist_function.py (lines 8) `assist_function.py`[`Line 8`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/assist_function.py#L8) | I have used flask login to assist in my is_logged_in. It helps with session management. This improves security, as it means non-authorised users, can not post, updated or delete any articles. | ✔ |
| using a salt is not required but is recommended | EXTRACT 18 | app.py (lines 9, 278) `app.py`[`Line 9`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L9) [`Line 278`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L278) | I have used the sha256_crypt to encrypt my password. It automatically by default adds a salt to the password and then hashes it | ✔ |
| additional credit will be given for an api that implements get,post,push and delete | EXTRACT 19 | app.py (lines 72, 76, 90, 94, 110, 129, 150) `app.py`[`Line 72`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L72) [`Line 76`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L76) [`Line 90`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L90) [`Line 94`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L94) [`Line 110`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L110) [`Line 129`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L129) [`Line 150`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L150) | I have created a restful api which allows users to add (create), delete, get (read) and edit (update) articles from the database. Some of the CRUD operations require an additional parameter, whilst some do not. (See restful API instructions, which have commands, which you can put in the terminal whilst the application is running). | ✔ | 
| use of flask-restful is not required but is recommended | EXTRACT 20 | app.py (lines 20, 21, 22, 74, 92, 108, 128, 149) `app.py`[`Line 20`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L20) [`Line 21`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L21) [`Line 22`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L22) [`Line 74`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L74) [`Line 92`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L92) [`Line 108`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L108) [`Line 128`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L128) [`Line 149`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L149) | I have used flask-restful here in order to create my restful api. My restful api allows users to carry out CRUD operations from a terminal. Marshal_with is a restful module and it is a decorator which takes your data object and applied the field filtering. It works on single object, list of objects or dicts (See restful API instructions). | ✔ |
| using sqlalchemy is not required but will attract credit | EXTRACT 21 | app.py (lines 15) `app.py`[`Line 15`](https://gitlab.doc.gold.ac.uk/sali011/term-2-lab/blob/master/myapp/app.py#L15) | I have imported and attempted to incorporate sqlalchmey (Partial Pass). This would have allowed me to have more flexibility and power over the SQL functions, queries and the overall schema. | ✔ |



___________________________________________________________________________


**RESTFUL API INSTRUCTIONS:**

Once you have set the terminals up (as mentioned above in part 15 of the detailed criteria), you can then paste the following commands for CRUD using restful api:

**NOTE: I HAVE USED CSRF TOKENS WITHIN MY FLASK APP SO SOME OF THE CURL RESTFUL API COMMANDS WILL NOT WORK. THIS IS DUE TO CSRF TOKENS NOT BEING PASSED. I HAVE BROUGHT THIS UP WITH DR.VALA AND SHE HAS ADVISED ME TO LET MARKERS KNOW THIS IN THE README. CSRF ADDS SECURITY SO IT DOES NOT ALLOW AN UNAUTHORISED USER CHANGE THE DATABASE IN ANYWAY. IF YOU WOULD LIKE TO TEST SOME OF MY RESTFUL API COMPONENTS AND SEE IF THEY WORK, IN APP.PY, COMMENT OUT LINES CONTAINING CODE FOR CSRF. ALSO WITHIN THE TEMPLATES FILES, IN EVERY HTML FILE WHICH CONTAINS A FORM, PLEASE REMOVE OR COMMENT OUT THE FOLLOWING LINE (THANK YOU):** 

< input type="hidden" name="csrf_token" value="{{ csrf_token() }}" />

- GET (This example cpmmand gets the 5th article in the database): curl http://doc.gold.ac.uk/usr/288/restfapi/6 -X GET 
- POST (This example command will post an article with author and body): curl http://doc.gold.ac.uk/usr/288/restfapi/5 -X POST
- DELETE (This example command will delete the 5th article in the database): curl http://doc.gold.ac.uk/usr/288/restfapi/5 -X DELETE
- PUT (This example command will update an exisiting articles body, i.e. article 5):  curl -d "body=<ENTER TEXT HERE>" http://doc.gold.ac.uk/usr/289/apirestful/5 -X PUT -v

___________________________________________________________________________

**DESCRIPTION OF ALL FILES AND DIRECTORIES:**

In this section, I will attempt to cross analyse all the files and directories I have created. This will hopefully give you a better idea on the structure of my flask application and what the many different components are. My 'About' page on the web application briefly does this. In depth detail will be given below (details on specific functions will either be found above in the detailed criteria for the app or in the comments in the files):

**PYTHON FILES**

In this section I will explain what my python files contain and what functionality they have. I have three python files in total.

**app.py** 

App.py is my main python file, and I run when I want to run my application from the server. It contains the majority of the python code I used to run my flask application. It begins with imports of various modules which will be essential for running certain functions in the app. It then has initialisation of ‘app’ and MySQL databases initialisations. App.py contains all the app routes of the web application. It ends with a debugger. This allows us to see the errors on the browser.

**classes.py**

Classes.py contains all the classes I have created for the app.py file and its functions. I have in app.py imported the classes.py file. This is in order to maintain SoC (separation of concerns). Classes allow us to modularise code and this is what I have done. Class Register Form (for registering a user) and class ArticleForm (for creating an article on the article page).

**assist_function.py**

Assist_function.py contains my is_logged_in function. It is a decorator which is applied to my functions (routes) which require user authorisation (user to be logged in). It makes use of the modules functools and session, which ensures any unauthorised viewers cannot affect the database in anyway. For example, they must login if they want to post, edit or delete (their articles) an article. Viewing articles is available to everyone.

**CSS FILES**

This CSS file is stored in the static directory. I have used it to style specific and extra features on my application. For example, although I used bootstrap to design my navbar, I’ve overridden bootstrap CSS by adding my own class and providing the code/styling.

**STATIC - style.css**

This CSS file is stored in the static directory. I have used it to style specific and extra features on my application. For example, although I used bootstrap to design my navbar, I’ve overridden bootstrap CSS by adding my own class and providing the code/styling.

**HTML FILES**

In this section I will discuss my main html files. They are contained in the folder ‘templates’. I have more html files, but for more specific parts of the application. They will be discussed in a later section.

**TEMPLATES - about.html**

About.html is the file you are currently viewing this page on. It makes use of jinja templates. All of my html files extend layout.html (which is my base layer html). The about page contains other general tags e.g. h1, h2, p etc.

**TEMPLATES - add_article.html** 

Add_article.html extends layout.html. It too utilises jinja templates. Within this html file I have got form tags, which perform the POST method. It takes in the title entered by the user and the body of text and submit this, via the input tag.

**TEMPLATES - article.html**

Article.html extends layout.html. I have used it to display the articles on my dynamic flask application. It is one of the direct app routes (html pages) which is displayed on the site. It gets the title, author and body of the article, from the database. I use the ‘|’ symbol to filter out the tags.


**TEMPLATES - articles.html**

Articles.html extend layout.html. This html file uses a list tag to list all the articles currently stored on the database. This is directly displayed on the application page ‘Forum’. The for-loop loops through all the articles and lists them.

**TEMPLATES - dashboard.html**

Dashboard.html extends layout.html. It uses a table (table tag) with columns: ‘ID’, ‘Title’, ‘Author’, ‘Date’. The dashboard is only accessible once a user logs in/creates an account. A for loop is used again to find and list articles, however, only articles specific to that user. I also have an edit and delete button, which function, and will be explained after.

**TEMPLATES - edit_article.html**

Edit_article extends layout.html. This html file enables the user to edit an existing article they posted previously. It uses an extra html file from the ‘includes’ directory. It uses form tags with a ‘POST’ method to get an existing article and display it (the title and body of text of the article).

**TEMPLATES - home.html**

Home.html extends layout.html. This html file contains the tags for the main page. It contains a conditional statement to maintain access control. This is so that no one can access the site through merely typing the URL in.

**TEMPLATES - layout.html**

Layout.html is the main (base) html file. All other html files extend this one. In the head of this file, I have the title and link tags to bootstrap and my personal CSS file. The body then has the navigation bar, which is displayed on all the other pages. It also contains my footer which is seen on every page. The script tags are on the bottom, for bootstrap, this also allows the page to load faster. If I want a certain feature to be on all pages, I will just place that feature on this layout.html file.

**TEMPLATES - login.html**

Login.html extends layout.html. It has a form tag which contains a ‘POST’ method. This html file is displayed when the user goes to the login page. It also has a button, to log in. It also takes into consideration access control, as it uses csrf tokens.

**TEMPLATES - register.html**

Register.html extends layout.html. This file is displayed when the user clicks on the register page. It uses a form tag, which asks the user for name, email, username and password (with confirmation). It then has a submit button (input tag). This page is also secured with csrf tokens, which validates the forms.

**TEMPLATES - scores.html**

Scores.html extends layout.html. It displays the latest scores and fixtures of every club in the premier league. It highlights Chelsea, due to the page being specifically about them. I have used an iframe in order to display the table of fixtures and results.

**TEMPLATES - stadium.html**

Stadium.html extends layout.html. This page displays a search box and map for the user. When they enter a football team and enter, the map displays the stadium location on google maps. This also utilises iframes. The form uses csrf tokens for validations and expires when session done. It also uses a ‘POST’ method in the form.

**INCLUDES (WITHIN TEMPLATES) - _formhelpers.html** 

This html file is used when we render forms. It utilises jinja templates, as well macros. Macros help to attain DRY (Don’t Repeat Yourself) principles, as well as modularising code. There is also a conditional which will throw an error message, if an error is found.

**INCLUDES (WITHIN TEMPLATES) - _messages.html**

This html file is used for the flash messages which appear throughout the application. They display alerts (messages to the user) in either a red (danger) box or green (success) box. Conditionals are used throughout to ensure the right alert is used in the right situation.

**INCLUDES (WITHIN TEMPLATES) - _navbar.html**

This html file contains the code needed to display to navigation bar. It utilises bootstrap for the design. The login, register and dashboard options are separated from the other, general, pages pf the flask app. I have used a conditional to check if the session the user is currently using, is logged in. If they are, then display logout and dashboard, else, they are not signed in, so display the login and register options.






