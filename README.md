# cirepo

[![CircleCI](https://circleci.com/gh/stevedepp/cirepo.svg?style=svg)](https://circleci.com/gh/stevedepp/cirepo)
## continuous integration repo 
### 1. building the repo

- [x] step 01: new github repository
<img width="707" alt="I Repositories" src="https://user-images.githubusercontent.com/38410965/94271088-20511b00-ff0f-11ea-81e7-bc92930c1e32.png">

- [x] step 02: create `Public` with a simple `README.md` and `.gitignore` template for python 
<img width="660" alt="Create a new repository" src="https://user-images.githubusercontent.com/38410965/94270834-b46eb280-ff0e-11ea-9496-fe0a94cde93c.png">

- [x] step 03: log into https://circleci.com with github
<img width="721" alt="Log In to" src="https://user-images.githubusercontent.com/38410965/94268352-0a415b80-ff0b-11ea-95e1-b3b10f36a463.png">

- [x] step 04: select your organization
<img width="486" alt="Select an organization" src="https://user-images.githubusercontent.com/38410965/94268387-15948700-ff0b-11ea-8c12-812f9302ae45.png">

- [x] step 05: select `cirepo` project (circleci populates this with your github repos)
<img width="860" alt="Projects" src="https://user-images.githubusercontent.com/38410965/94268415-20e7b280-ff0b-11ea-8003-adfad03c2e88.png">

- [x] step 06: circleci needs a `.circleci/config.yml` file (this is a bug later)
<img width="802" alt=" Pipelines" src="https://user-images.githubusercontent.com/38410965/94269002-05c97280-ff0c-11ea-927d-7c7dfa70b7fd.png">

- [x] step 07: from terminal or console, clone github repo and create these files:
     - [x] `Makefile`
     - [x] `requirements.txt`
     - [x] `cirepolib` folder
          - [x] `__init__.py`
          - [x] `cirepomod.py`
     - [x] `tests` folder
          - [x] `test_cirepo.py`
     - [x] `.circleci` folder
          - [x] `config.yml`

<img width="682" alt="stevedepp@Steves-MBP-2 -  02DV2cirepo" src="https://user-images.githubusercontent.com/38410965/94269024-0feb7100-ff0c-11ea-9c10-6175a5185840.png">

- [x] step 08: from terminal or console, edit those files with nano or vim:
<img width="682" alt="stevedepp@Steves-MBP-2 -  02DV2cirepo" src="https://user-images.githubusercontent.com/38410965/94269309-7ec8ca00-ff0c-11ea-88b0-709155b06bea.png">

- [x] `Makefile`
     - `setup` for a python virtual environment
     - `activate` activate the virtual environment (does not work)
     - `install` required dependencies
     - `test` validates via unit tests of
     	- python code
	    - jupyter notebook
     - `lint` for warnings & errors in `cirepolib` _and later 'cli.py'_
     	- `R` disables recoomendations
	    - `C` disables configurations
     - `all` performs `install`, `lint`, and `test`
<img width="682" alt="GNU nano 2 0 6" src="https://user-images.githubusercontent.com/38410965/94269044-1b3e9c80-ff0c-11ea-89df-2cfc352244c9.png">

- [x] 'requirements.txt`
<img width="682" alt="nano requirements txt" src="https://user-images.githubusercontent.com/38410965/94269063-242f6e00-ff0c-11ea-8798-e62ebd53d2e9.png">

- [x] `cirepomod.py` 
     - `myfunc` returns 1
     - `call_web_service' will be ued by `cli.py` later
<img width="682" alt="nano cirepolibcirepomod py - nano" src="https://user-images.githubusercontent.com/38410965/94269088-2e516c80-ff0c-11ea-80bb-accb56291765.png">

- [x] `test_cirepo.py`
     - imports `cirepomod` module from `cirepolib` library
     - `test_func` asserts that cirepomod.my_func == 1
<img width="682" alt="nano teststest_cirepo py - nano" src="https://user-images.githubusercontent.com/38410965/94269121-37dad480-ff0c-11ea-99eb-f92ead11b214.png">

- [x] `.circleci/config.yml` is config for our SaaS
     - 3 run steps 
           - `make install`
		 - `make test`
		 - `make lint`
	- lines with `name:` will show up in Circle Ci as build steps
		 - `install dependences`
		 - `run tests`
		 - `run lint`
<img width="682" alt="nano circleciconfig yml" src="https://user-images.githubusercontent.com/38410965/94269159-432e0000-ff0c-11ea-9afd-bb988a178274.png">

- [x] step 12: try out `make setup`, `make activate`, and `make install`  
<img width="682" alt="make install" src="https://user-images.githubusercontent.com/38410965/94269319-825c5100-ff0c-11ea-98c4-8f9d65e96bba.png">

- [x] step 12 (continued): `make test` which fails when jupyter `notebook.ipynb` is not found
<img width="682" alt="stevedepp@Steves-MBP-2 -  02DV2cirepo" src="https://user-images.githubusercontent.com/38410965/94269339-88523200-ff0c-11ea-8a9e-9e6b39721a88.png">

- [x] step 13: start jupyter notebook
<img width="682" alt="Jupyter notebook" src="https://user-images.githubusercontent.com/38410965/94269364-9011d680-ff0c-11ea-86a6-a4843a5d35f8.png">

- [x] step 14: pull down from `New` to `Python 3` to create a new notebook
<img width="940" alt="localhost8888tree" src="https://user-images.githubusercontent.com/38410965/94269383-986a1180-ff0c-11ea-9755-d37de5c7e1b4.png">

- [x] step 15: name the notebook `notebook`, import `cirepomod` module, and populate with `my_func`, `print_name`, and `fake_data`
<img width="940" alt="notebook Jupyter No" src="https://user-images.githubusercontent.com/38410965/94269403-9e5ff280-ff0c-11ea-864d-3272055c7134.png">

- [x] step 16: save the notebook
<img width="940" alt="stevedeppmy" src="https://user-images.githubusercontent.com/38410965/94269421-a324a680-ff0c-11ea-9a2d-919dd04ecf44.png">

- [x] step 17: try out `make test` again, and try out `make lint` for the 1st time
<img width="682" alt="stevedepp@Steves-MBP-2 -  02DV2cirepo" src="https://user-images.githubusercontent.com/38410965/94269443-a91a8780-ff0c-11ea-92e2-d4115cc4a654.png">
<img width="682" alt="stevedepp@Steves-MBP-2 -  02DV2cirepo" src="https://user-images.githubusercontent.com/38410965/94269458-ae77d200-ff0c-11ea-9c8e-c6e9933e0611.png">

- [x] step 18: push `master` to `origin` at github
     - [x] `git status` _(notice anything missing?)_
     - [x] `git add` all with `*`
     - [x] `git commit -m 'initial commit'`
     - [x] 'git push`
<img width="682" alt="stevedepp@Steves-MBP-2  02DV2cirepo" src="https://user-images.githubusercontent.com/38410965/94269485-ba639400-ff0c-11ea-8ad6-7711b9c892ce.png">

- [x] step 19: circleci has the build job `Queued` _(but there is an `Build Error` already)_
<img width="1193" alt="Legacy Jobs View stevedeppcirepo" src="https://user-images.githubusercontent.com/38410965/94269543-cd766400-ff0c-11ea-8afd-9815661b10da.png">

- [x] step 19 (continued): circleci `Config Processing Error` because missing the .circleci/config.yml file _(unsure why)_
<img width="1051" alt="o Build Error (2)" src="https://user-images.githubusercontent.com/38410965/94269558-d5360880-ff0c-11ea-9783-362f1148c71d.png">

- [x] step 20: push `master` again to `origin` at github with .circleci/config.yml file this time _(it had been deleted)_
     - [x] `git status`
     - [x] `git add` all with `*`
     - [x] `git commit -m 'adding circleci/config.yml'`
     - [x] `git push`
<img width="682" alt="stevedepp@Steves-MBP-2 -  02DV2cirepo" src="https://user-images.githubusercontent.com/38410965/94269585-dbc48000-ff0c-11ea-8994-4d579cb23130.png">

- [x] step 21: circleci has the build job `Queued` _(`build` indicates no error so far)_
<img width="1051" alt="o Legacy Jobs View - stevedeppcirepo" src="https://user-images.githubusercontent.com/38410965/94269611-e252f780-ff0c-11ea-8d96-fbd024dcb69b.png">

- [x] step 21 (continued): circleci is `Running`
<img width="1051" alt="o Legacy Jobs View - stevedeppcirepo" src="https://user-images.githubusercontent.com/38410965/94269634-ea129c00-ff0c-11ea-91fe-af47d0181e05.png">

- [x] step 21 (continued): circleci `Success` _(notice the named steps, `install dependencies`, `run tests`, and `run lint`, from `config.yml`)_
<img width="1051" alt="D Legacy Jobs View" src="https://user-images.githubusercontent.com/38410965/94281522-bccdea00-ff1c-11ea-82a6-2a8b77913a23.png">


## continuous integration repo 

### 2. new repo features

- [x] step 01: from terminal or console, create a new branch named `feature_depp_20200925` via `git checkout -b feature_depp_20200925` 
<img width="682" alt="stevedepp@Steves-MBP-2 -  02DV2cirepo" src="https://user-images.githubusercontent.com/38410965/94326072-ca608f80-ff6f-11ea-969b-74fd68223b78.png">

- [x] step 02: from terminal or console, create `cli.py` file and start either of nano or vim editors 
<img width="682" alt="stevedepp@Steves-MBP-2  02DV2cirepo" src="https://user-images.githubusercontent.com/38410965/94326077-d2203400-ff6f-11ea-97a1-40779d6f713f.png">

- [x] step 03: copy and paste code for the command line tool, `cli.py`, that ...
    - [x] imports `cirepolib` modules, `json`, `click`, and `Flask` 
    - [x] set `click.option` for `--name`
    - [x] echo `print_name` module output
    - [x] echo url's for `hello`, `fakedata`, and `wname` functions
    - [x] define Flask app functions for each `app.route`
    - [x] pylint fails if `hello()`, `fakedata()`, and `wname()` functions are not called
    
<img width="682" alt="Pasted Graphic 263" src="https://user-images.githubusercontent.com/38410965/94326081-d9474200-ff6f-11ea-88c8-04ce974f477d.png">

- [x] step 04: test `cli.py` locally by running `./cli.py --name steve` which returns ...
    - "steve-apple" in blue
    - one `localhost` url for each of 3 functions
- [x] step 05: paste the 1st url, `http://localhost:5000/`, into browser
<img width="682" alt="ol for interacting with library" src="https://user-images.githubusercontent.com/38410965/94326085-e19f7d00-ff6f-11ea-8416-9e6ec121f56b.png">
<img width="771" alt="localhost5000" src="https://user-images.githubusercontent.com/38410965/94326091-ea904e80-ff6f-11ea-8e28-b1e211890a55.png">

- [x] step 06: paste the 2nd url, `http://localhost:5000/fakedata`, into browser
<img width="682" alt="cli py --name steve" src="https://user-images.githubusercontent.com/38410965/94326100-f2e88980-ff6f-11ea-9afa-609284adf04e.png">
<img width="771" alt="Pasted Graphic 267" src="https://user-images.githubusercontent.com/38410965/94326102-fb40c480-ff6f-11ea-8b01-dcac1103e902.png">

- [x] step 07: paste the 3rd url, `http://localhost:5000/wname`, into browser
<img width="682" alt="cli py --name steve" src="https://user-images.githubusercontent.com/38410965/94326108-0c89d100-ff70-11ea-9dbb-f7cbb041b9bc.png">
<img width="771" alt="localhost5000wname" src="https://user-images.githubusercontent.com/38410965/94326114-13b0df00-ff70-11ea-96f9-c3cb6963f9e3.png">

- [x] step 08: from a terminal or console, open a `jupyter notebook`
<img width="668" alt="stevedepp@Steves-MBP-2" src="https://user-images.githubusercontent.com/38410965/94326211-9afe5280-ff70-11ea-947c-d11caeb3b108.png">
<img width="771" alt="Pasted Graphic 271" src="https://user-images.githubusercontent.com/38410965/94326139-3f33c980-ff70-11ea-9b05-8ae98191b2bd.png">

- [x] step 09: run cells 1 to 4, copy & paste `!./cli.py --name steve` into a new 5th cell, and run that 5th cell to return 3 urls
- [x] step 10: click on the 1st url `http://localhost:5000/`
<img width="872" alt="Home Page -" src="https://user-images.githubusercontent.com/38410965/94326145-4529aa80-ff70-11ea-8bbb-16f7b4820d5f.png">
<img width="913" alt="localhost5000" src="https://user-images.githubusercontent.com/38410965/94326151-4b1f8b80-ff70-11ea-94e2-6b02bc4d2850.png">

- [x] step 11: click on the 2nd url `http://localhost:5000/fakedata`
<img width="872" alt="Home Page -" src="https://user-images.githubusercontent.com/38410965/94326224-aa7d9b80-ff70-11ea-8441-46bdbe05ea9a.png">
<img width="913" alt="localhost5000fakedata" src="https://user-images.githubusercontent.com/38410965/94326236-bcf7d500-ff70-11ea-8826-e82ed009e637.png">

- [x] step 12: click on the 3rd url `http://localhost:5000/wname`
<img width="872" alt="Home Page -" src="https://user-images.githubusercontent.com/38410965/94326244-c2edb600-ff70-11ea-98b1-66732bd236d8.png">
<img width="872" alt="Pasted Graphic 278" src="https://user-images.githubusercontent.com/38410965/94326248-c8e39700-ff70-11ea-8d19-42dac6b6846a.png">

- [x] step 13: remove the notebook's 5th cell created earlier; otherwise, the notebook test function `pytest --nbval` loops endlessly waiting for response 
<img width="825" alt="Home Page Select or create a notebook" src="https://user-images.githubusercontent.com/38410965/94326255-d1d46880-ff70-11ea-89c2-fe0113983e4f.png">

- [x] step 14: in a terminal or console, `cntr-c` followed by `y` kills the notebook
<img width="668" alt="Pasted Graphic 280" src="https://user-images.githubusercontent.com/38410965/94326264-dbf66700-ff70-11ea-9938-f41aee2c660b.png">

- [x] step 15: open `Makefile` with nano or vim, and ppend `cli tests/test_cirepo` to the `make lint` script so those functions are linted
<img width="668" alt="nano Makefile" src="https://user-images.githubusercontent.com/38410965/94326276-f16b9100-ff70-11ea-8b03-20cbfc1e533d.png">

- [x] step 16: test linting locally with `make lint` 
<img width="668" alt="activate" src="https://user-images.githubusercontent.com/38410965/94326281-fc262600-ff70-11ea-9fc6-51dbe6bfe0c0.png">

- [x] step 17: in a terminal or console, separately add & commit the `cli.py` and `Makefile` changes with descriptive annotations to this `feature_depp~20200925` branch 
<img width="682" alt="git add" src="https://user-images.githubusercontent.com/38410965/94326290-0516f780-ff71-11ea-9aeb-2e421477cee5.png">

- [x] step 18: to `git push` the locally committed features to the `origin` adding `--set-upstream origin feature_depp20200925` so upstream origin knows to make a this branch
<img width="682" alt="stevedepp@Steves-MBP-2 -  02DV2cirepo" src="https://user-images.githubusercontent.com/38410965/94326292-0b0cd880-ff71-11ea-9e67-48f62b1508da.png">

- [x] step 19: observe circleci successfully building and testing `feature_branch_depp_20200925`
<img width="1051" alt="Pasted Graphic 286" src="https://user-images.githubusercontent.com/38410965/94326300-1829c780-ff71-11ea-9b31-c1bc2c4bc125.png">
<img width="1051" alt="build (46) stevedeppcirepo" src="https://user-images.githubusercontent.com/38410965/94326304-1d871200-ff71-11ea-957f-f046dba02d2e.png">

- [x] step 20: on github's website, observe the `origin` repository received pushes from our remote terminal commands, and awaits a `Compare & pull request`; tap that green button
<img width="704" alt="Pasted Graphic 288" src="https://user-images.githubusercontent.com/38410965/94326313-27a91080-ff71-11ea-8391-95d4db82de95.png">

- [x] step 21: annotate the pull request, here with `this looks good`
<img width="704" alt="Pasted Graphic 289" src="https://user-images.githubusercontent.com/38410965/94326317-30014b80-ff71-11ea-9dec-67456a84f92c.png">

- [x] step 22: observe the interacting annotations between push and pull actions; tap the `Merge pull request` and then `Confirm merge`
<img width="752" alt="Pasted Graphic 290" src="https://user-images.githubusercontent.com/38410965/94326323-38598680-ff71-11ea-8506-0c3fd99d4112.png">
<img width="752" alt="Pasted Graphic 291" src="https://user-images.githubusercontent.com/38410965/94326328-43141b80-ff71-11ea-9ffb-be377ed0249d.png">

- [x] step 23: observe that the `Pull request successfully merged and closed` indicating the 2 features are successfully **_INTEGRATED_** into the `origin` `master` branch of the `cepo` repository
<img width="760" alt="build (46) - stevedeppcirepo" src="https://user-images.githubusercontent.com/38410965/94326350-57581880-ff71-11ea-9553-ca43905d0bdd.png">

(in summary, we have added features to `feature_depp_20200925` remotely and then pushed and merged `feature_depp_20200925` with the `origin` `master` repository, but the remote `master` repository does not know these features yet) 

## continuous integration repo 

### 3. 1st production release

- [x] step 01: in a terminal or console, switch from `feature_depp_20200925` branch to `master` via `git checkout master` and then `git pull` the newly merged `master` branch with new features from `origin` 
<img width="682" alt="stevedepp@Steves-MBP-2 -  02DV2cirepo" src="https://user-images.githubusercontent.com/38410965/94326362-68088e80-ff71-11ea-99fd-b0f23887b4b3.png">

- [x] step 02: from terminal or console, create a new `production` branch  via `git checkout -b production` and `git push` that branch to `origin` via `git push --set-upstream origin production`
- [x] step 03: siwtch from `production` to the `master` (devlopment) branch and open a `nano` or `vim` editor on `README.md`
<img width="682" alt="stevedepp@Steves-MBP-2 -  02DV2cirepo" src="https://user-images.githubusercontent.com/38410965/94326368-6e970600-ff71-11ea-8e07-51700f103c5e.png">

- [x] step 04: add a circleci badge to README.md to indicate build success; https://circleci.com/docs/2.0/status-badges/ explains badge configurations
<img width="682" alt="nano README md - nano" src="https://user-images.githubusercontent.com/38410965/94328499-21229500-ff81-11ea-9a15-88ee25c1ef9f.png">


- [x] step 05: from terminal or console, `git add` and `git commit` this `README.md` with annotation to indicate this is the 1st production release
- [x] step 06: switch to `production` branch and `git merge` with the `master` branch; then `git push` sending this `production` branch to github and circleci for building and testing
<img width="682" alt="Pasted Graphic 297" src="https://user-images.githubusercontent.com/38410965/94328647-377d2080-ff82-11ea-80f6-54c37ad2bd4f.png">

- [x] step 07: on the circleci.com website, observe the build, test, lint stage successes
<img width="959" alt="Admin v" src="https://user-images.githubusercontent.com/38410965/94326382-81113f80-ff71-11ea-8571-9ae9dcc27db2.png">

- [x] step 08: back at github, observe the master branch with circleci badge; observe the message confirming `production` branch pushed 
<img width="742" alt="build (49) - stevedeppcirepo" src="https://user-images.githubusercontent.com/38410965/94326387-89697a80-ff71-11ea-9510-d010d976042c.png">

- [x] step 09: on github, pull down from `master` to select `production` branch
<img width="255" alt="9 master" src="https://user-images.githubusercontent.com/38410965/94326390-90908880-ff71-11ea-8a21-724c373a8950.png">

- [x] step 10: on github, in the `production` branch, notice the circleci badge and annotation for the `1st production release` 
<img width="724" alt="Pasted Graphic 302" src="https://user-images.githubusercontent.com/38410965/94328749-0e10c480-ff83-11ea-9b83-11ca3805dd7e.png">
