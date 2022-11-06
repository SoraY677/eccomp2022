env-init:
  conda create -n eccomp2022 python=3.8

env-activate:
	conda activate eccomp2022

install:
	pip install -r requirements.txt

run-demo:
	python main.py demo

run-prod:
	python main.py prod

package:
	pip freeze > requirements.txt

env-deactivate:
	conda deactivate

env-delete:
	conda remove -n eccomp2022 --all
