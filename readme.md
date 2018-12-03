This is the rudiments of a small personal API to run on Heroku.  

Right now, all it does is document conversions with Pandoc, for the purpose of being able to generate proper PDFs with LaTeX from markdown. This is currently working (on free dyno time no less), and I'm using it myself in conjunction with the iOS Shortcuts app to do simple file conversions from my iPad. 

Ultimately, it will do more stuff, but first I need to secure it. Right now, the only security is that I haven't told anyone the URL, which obviously won't do for code that can actually have an impact on the world, but is fine just for document conversions. 

Feel free to fork this and run it yourself.  Be aware that there's a lot of cruf in the code though---you can get away with deleting everything under the test header in app.py, as well as all the routes except `\textconvert` and `\omniconvert` For more complicated document conversion use cases (but, alas, no LaTeX), try [Docverter](https://www.docverter.com/). 

This uses Docker, which requires some extra installation steps on Heroku:

```
heroku update beta
heroku plugins:install @heroku-cli/plugin-manifest
heroku create your-app-name --manifest
git add .
git commit -m "first commit"
heroku stack:set container
git push heroku master
heroku open
```

Currently, I can't get it to build on heroku with texlive-xetex, which pandoc sometimes needs for building special unicode characters (although, weirdly, not always---it can handle curly quotes for example).  It hangs on an interactive element normally, and when I try to add `ENV DEBIAN_FRONTEND noninteractive` to the dockerfile to put a stop to that, it hangs later down in the build process on one of the heroku push things. Forgetting about it now, will perhaps try to build locally and push to container registry later.
