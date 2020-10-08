# Jupytent (Jupy-tent)
Minimal docker container based Jupyter lab/hub/notebook, provisioned resource via docker-compose.

### Prerequisite
- Docker for Mac / Docker for Windows: [Official site](https://www.docker.com/products/docker-desktop)
- Miniconda: [Official site](https://docs.conda.io/en/latest/miniconda.html)
- Git: [bitbucket tutorial](https://www.atlassian.com/git/tutorials/install-git) or [main site](https://git-scm.com/downloads)

### Core Dependencies
- docker-compose-templer: [aisbergg/python-docker-compose-templer](https://github.com/Aisbergg/python-docker-compose-templer)

### Usage
1. Clone this repository to your machine, export path for availability of `jupytent` command
  ```
  git clone https://github.com/sinonkt/jupytent.git
  cd jupytent
  ```
2. Create your new jupter instances stack, by copying from `./stacks/example.yml`
  ```
  cp ./stacks/example.yml ./stacks/lab1.yml
  ```
3. Adjust number of users or resources provided for each instance as you like.
  ```
  <definition yml lies here>
  ```
4. Generate your new stack configs. `Need to regenerate stack configs every time we've changes`
  ```
  ./bin/jupytent generate lab1
  ```
5. Then run our stack by.
  ```
  ./bin/jupytent up lab1
  ```
  We good to goes now! Happy Jupyting. :)

- Another shortcut command for update current stack right away which exactly just run generate then up selected stack.
  ```
  ./bin/jupytent update lab1
  ```
### Jupyter docker stacks
[Selecting an Image](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html)

### Alternatives
JupyterHub ([Official](https://github.com/jupyterhub/jupyterhub),[with kubernetes](https://zero-to-jupyterhub.readthedocs.io/en/latest/#setup-jupyterhub),[pdf](https://github.com/jupyterhub/jupyterhub-tutorial/blob/master/JupyterHub.pdf))

### Contributors
  - Krittin Phornsiricharoenphant, oatkrittin@gmail.com

### Issues
[Share GPU accross jupyter instance](https://github.com/docker/compose/issues/6691)
