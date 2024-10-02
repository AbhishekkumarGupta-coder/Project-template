echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python 3.10"
conda create --prefix ./env python=3.10 -y
echo [$(date)]: "activate requirements"
source activate ./env
echo [$(date)]: "installing requirements"
pip install -r requirements.txt
echo [$(date)]: "END"