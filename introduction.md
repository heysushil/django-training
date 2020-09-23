# Django Framework ka introduction and aage kya karna hai uski guidens hain yaha par to last tak jarur padhna

## मेरे Youtube चैनल को सबस्क्राइब करना ना भूलो ताकि आपको कोड का पूरा फ़्लो समझमे आए - https://www.youtube.com/HeySushil

## कोई भी सवाल है उसको मेरे यूट्यूब चैनल के कमेन्ट या डिस्कशन सेक्शन मे पूछ सकते हो - https://www.youtube.com/channel/UCphs2JfmIClR62wbyf76HDg/discussion

## और हाँ GitHub पर मुझे फॉलो करना ना भूलो ताकि सारे अपडेट एण्ड वर्क आपको मिलता रहे। 

### hello django tarining

## Django Framwork: MVT

### Model:

1. Models: models, field types, indexes, meta options, model class
2. QuerySets: Marking queries, QuerySet method, lookup expressions
3. Model Instances: instances methos, accessing realted objects
4. Migration: Migration, operations, schemEdtor, writing mighration
5. Advaced: Managers, Raw Sql, Transactions, Aggregation, Serch, Custom Fields, Multiple database, Custom lookups, query expressions, coditional expresstion, database function, asynchornous support
6. Other: Suppored database, optimize database access, PostgreSql specifc features

### View: (means Controller)

1. basics: URLconfs, view functions, shotcuts, decorators
2. reference: buil-in views, request/response objects, templateResponse objects
3. file uploads: file objects, storage api, mangaing files, custom storeage
4. class-based views: build-in display views, buil-in editing views, api refrence
5. advacned: generation csv, pdf
6. Middleware: buil-in middleware classes

### Template

1. basic
2. for desingers: languses overviews, buil-in tags and filters
3. for programmer: template api, custom tags and filters

### Forms:

1. basic: form api, buil-in fileds, buil-in widgts
2. advanced: forms for models, interating media, formsets, Customing validation

### Developemtn Process:

1. settings: overview, full list of settings
2. application: overview
3. exceptions: overview
4. django-admin and manage.py: overview, adding cutom commands
5. testing: introduction, writing and run testing, include testing tools, advace toops
6. deployments: overview, wsgi servers, asgi servers, static files deploying, tracing code erros in email, deployment checklist

### Admin:

1. admin site
2. admin actions
3. admin documentation generator

### Security:

1. Overview
2. Django secuity issue disclose
3. Clickjacking protection
4. Cross site request frogery protection
5. Crytographic singing

### Performace and optimazation

1. overview

### Common Web Application Tools:

1. Caching
2. Logging
3. Sending emails
4. Pagination
5. Sessions
6. Data validation

### Install:

1. Appliaction
    Template:
    View:
    Model:

# Day 37 on Django

1. Basic concepts ko majbut karne ke liye inko padh sakte ho [Django Doc](https://docs.djangoproject.com/en/3.1/intro/whatsnext/)
1. Index wise padhne ke liye [Django Index](https://docs.djangoproject.com/en/3.1/genindex/)
1. Django Advance padhne ke liye [Django Advance](https://docs.djangoproject.com/en/3.1/intro/reusable-apps/)

# Day39 on Django Framework with HeySushil

1. mysite project ka file structre jo abhi hai

        mysite/
            manage.py
            mysite/
                __init__.py
                settings.py
                urls.py
                asgi.py
                wsgi.py
            polls/
                __init__.py
                admin.py
                apps.py
                migrations/
                    __init__.py
                    0001_initial.py
                models.py
                static/
                    polls/
                        images/
                            background.gif
                        style.css
                templates/
                    polls/
                        detail.html
                        index.html
                        results.html
                tests.py
                urls.py
                views.py
            templates/
                admin/
                    base_site.html


# Day40 on Django Framework with HeySushil

Django framework me class ke reusibiltiy concept ki tarah hi app ko bhi reuse karna ka tarika milta hai.

Isse ke liye kuch point wise hum pahle samajh lete hai ki kya karna hota hai.

1. Pura python hi reusabilty ka ek bada example hain. Jaise python me hum librarys ka use karte hain.
1. Python Package Index (PyPi) https://pypi.org/ ke pas bahot hi bada package ka collection hai. Jiska use hum har bar karte rahte hain.
1. Waise hi Django me bhi bahot sare reusabel apps hain. Jada jankari ke liye check karo https://djangopackages.org/
1. Waise Django bhi ek reusable package hi hai agar ek tarike se dekho to.

## Kaise Polls app ko reusable banaya jaye?

1. Waise humne jab Polls app banaya tha hamare project me tab usko main project se jodne ke liye kya kiya tha.
1. Humne URLconf joki main settings.py file me humko milta hai useme include kiya tha. Then hum Polls app ko use kar sake the.
1. Waisa hi kuch hum yaha karne wale hain Polls app ko reusable app banae ke liye.

## But usse pahle Package aur App me antar samjhna jaruri hai?

### Package kya hai?

1. Package kai sare python files ka collection hai. Ya fir kai classes ka collection hai.
1. Jaise ki hume jab bhi kisi library ke module ka use hota hai to hum use import karte hain. Jaise ki import yourLibrary etc... to ye tarike se hum librarys ko import karte hain.
1. Yahin hain packages to App kya hai.

### App kya hai Django me?

1. App bhi lagbhag lagbhag same hai because isme bhi multiple pytho files hoti to hai but useke sath me?
1. Jaise hum jab class create karte hain to usme hame constructer create karna hi hota hai. Python me to ye compalsurry hain.
1. Same waise Polls ek file directory hai jisko Package jaise use karne ke liye?
1. App me ek special file __init__.py hoti hai joki isko as a package use karne me madad karti hai.
1. Bhale hi ye __init__.py file empty ho but ho jarur.
1. App apne app ko jakar check karo usme ye file jarur hoti hai.

### __init__.py kyo hota hai app folder me?

1. Django application asal me python package hi hai. Aur ye kisi bhi dusre Django project me use kiya ja sake uske liye hi isko aysa banaya gaya hai.
1. Django folder structre me jab hum app create karte hain to usme hume kuch important files milte hain. Jo ki hain: models, tests, urls, views.

> Note: Abhi ke liye bilkul ye thoda ka confusing hai but aage chal ke jab hum ispar work karenge then ye samjh me aane lage ga.

