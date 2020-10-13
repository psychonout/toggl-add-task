# TOGGL ADD TASK

__The script should work with Python 3.7+ and there are few additional steps:__
* You need to register an application at: https://developers.plan.toggl.com/applications
* You'd then need edit `config.py` and fill in the `key` and `secret` of your application as well as your Toggl `credentials`

__These only make sense if you haven't got `requests` installed for your default Python__
* Add a virtual environment for the script: `python -m venv venv`
* Activate the virtual environment using: `source venv/bin/activate`
* Install the requirements: `pip install -r requirements.txt`

__The script should be working now, however, if you wish to run it directly from within Linux terminal:__
* Change the shebang within `add_task.py` to whichever Python executable you choose.
* Change the file permissions so it can be executed `chmod a+x /path/to/add_task.py`
* Finally add an alias within `~/.bash_aliases`, f.e. `alias addtask='/root/toggl_addtask/add_task.py'`
