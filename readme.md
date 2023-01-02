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


----

# Updating to Digital Ocean Since Heroku is in the Shitter

- minimize costs by creating servers on the fly?  Or even if not, might be fun to bundle this as a one-off that can be created from the command line or from curl.  
- https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-20-04
- cloud config
    - https://www.digitalocean.com/community/questions/how-to-edit-and-re-run-cloud-config-user-data 
    - https://www.digitalocean.com/community/tutorials/how-to-use-cloud-config-for-your-initial-server-setup
    - https://www.digitalocean.com/community/questions/invoke-a-script-or-command-using-after-creating-a-droplet
    - https://www.digitalocean.com/community/tutorials/an-introduction-to-cloud-config-scripting
    - https://docs.digitalocean.com/tutorials/droplet-cloudinit/ 
    - https://docs.digitalocean.com/products/droplets/how-to/provide-user-data/
    - https://www.digitalocean.com/community/tutorials/automating-initial-server-setup-with-ubuntu-18-04
- force APT with Y 
    - https://askubuntu.com/questions/805067/is-there-a-way-to-force-yes-to-any-prompts-when-installing-from-apt-get-from
    - (or I could just create a docker image??)   
        - https://docs.digitalocean.com/products/app-platform/how-to/deploy-from-container-images/ (but this is for app platfrorm not for VPS?  is app platform cheaper? looks like 5 bucks a month.
        - https://www.digitalocean.com/community/tutorials/how-to-use-the-docker-1-click-install-on-digitalocean looks more appropriate
        - https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04#step-3-using-the-docker-command
- also want to wrap ghostscript for PDF merging and calibre for ebook conversion. 
    - ghostscript: https://www.linuxjournal.com/content/tech-tip-using-ghostscript-convert-and-combine-files 
    - calibre: https://manual.calibre-ebook.com/generated/en/cli-index.html
        - https://calibre-ebook.com/download_linux