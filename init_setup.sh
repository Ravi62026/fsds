echo [$(date)]: "start"

echo [$(date)]: "creating env with python 3.10.* version"

conda create --prefix ./env python=3.10 -y

echo [$(date)]: "activating the enviroment"

source activate ./env

echo [$(date)]: "installing thedev dependensies"

pip install -r requirements.txt

echo [$(date)]: "end"