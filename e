eval $(gp env -e)

cp lichessbot/pyvenv.cfg /home/gitpod/.cache/pypoetry/virtualenvs/lichessbot-IEoI1RvR-py3.8/pyvenv.cfg
cp test/pyvenv.cfg /home/gitpod/.cache/pypoetry/virtualenvs/test-rMMDreiZ-py3.8/pyvenv.cfg

ls /home/gitpod/.cache/pypoetry/virtualenvs/lichessbot-IEoI1RvR-py3.8/ -al
ls /home/gitpod/.cache/pypoetry/virtualenvs/test-rMMDreiZ-py3.8/ -al

poetry config repositories.testpypi https://test.pypi.org/legacy/
