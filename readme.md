currently not building, see details at https://stackoverflow.com/questions/53035971/how-to-get-heroku-apt-buildpack-to-build 


notes:

trying on docker now.  pipenv and docker and heroku is a combination not terribly well documented, so running experiments.

current problem: click, which apparently pipenv depends on, blows up with ascii environment on py3.  suggestion from the error message is to set an environment variable to order everything to be utf-8 (see [more details](https://click.palletsprojects.com/en/7.x/python3/)).  Trying that.

heroku config:set LC_ALL=C.UTF-8
heroku config:set LANG=C.UTF-8

(if need be, I can always just use requirements.txt.)
