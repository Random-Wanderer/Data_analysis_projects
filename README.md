# Notes
Notebook questions for:
Exploring crypto,
Cookie cats A/B test,
Old business analysis,
World Bank SQL query \
Came from www.Datacamp.com


# Startup the project

The initial setup.

Create virtualenv and install the project:
```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv ~/venv ; source ~/venv/bin/activate ;\
    pip install pip -U; pip install -r requirements.txt
```

Unittest test:
```bash
make clean install test
```

Check for packgenproject in gitlab.com/{group}.
If your project is not set please add it:

- Create a new project on `gitlab.com/{group}/packgenproject`
- Then populate it:

```bash
##   e.g. if group is "{group}" and project_name is "packgenproject"
git remote add origin git@github.com:{group}/packgenproject.git
git push -u origin master
git push -u origin --tags
```

Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
packgenproject-run
```

# Install

Go to `https://github.com/{group}/packgenproject` to see the project, manage issues,
setup you ssh public key, ...

Create a python3 virtualenv and activate it:

```bash
sudo apt-get install virtualenv python-pip python-dev
deactivate; virtualenv -ppython3 ~/venv ; source ~/venv/bin/activate
```

Clone the project and install it:

```bash
git clone git@github.com:{group}/packgenproject.git
cd packgenproject
pip install -r requirements.txt
make clean install test                # install and test
```
Functionnal test with a script:

```bash
cd
mkdir tmp
cd tmp
packgenproject-run
```
