# TP_INTRO_AGUILAR_DEVITT
# Tp grupal intro, Aguilar y Devitt


## Install

´´´bash
python3 -m venv venv
source venv/bin/activate
pip install flask
sudo apt install postgresql
´´´

## Run

´´´
source venv/bin/activate
cd back
flask run --debug
brew services start postgresql@14    ESTO ERA PARA MAC
sudo systemctl start postgresql
´´´