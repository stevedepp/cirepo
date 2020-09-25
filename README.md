# cirepo
## continuous integration repo

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

- [x] step 20: push master again to origin at github with .circleci/config.yml file this time _(it had been deleted)_
     - [x] `git status`
     - [x] `git add` all with `*`
     - [x] `git commit -m 'adding circleci/config.yml'`
     - [x] 'git push`
<img width="682" alt="stevedepp@Steves-MBP-2 -  02DV2cirepo" src="https://user-images.githubusercontent.com/38410965/94269585-dbc48000-ff0c-11ea-8994-4d579cb23130.png">

- [x] step 21: circleci has the build job queued up _(`build` indicates no error so far)_
<img width="1051" alt="o Legacy Jobs View - stevedeppcirepo" src="https://user-images.githubusercontent.com/38410965/94269611-e252f780-ff0c-11ea-8d96-fbd024dcb69b.png">

- [x] step 21 (continued): circleci is `Running`
<img width="1051" alt="o Legacy Jobs View - stevedeppcirepo" src="https://user-images.githubusercontent.com/38410965/94269634-ea129c00-ff0c-11ea-91fe-af47d0181e05.png">

- [x] step 21 (continued): circleci `Success` _(notice the named steps, `install dependencies`, `run tests`, and `run lint`, from `config.yml`)_
<img width="1051" alt="D Legacy Jobs View" src="https://user-images.githubusercontent.com/38410965/94281522-bccdea00-ff1c-11ea-82a6-2a8b77913a23.png">

