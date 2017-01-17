#!/bin/bash
if which sudo >/dev/null; then
  # Vagrant will execute these, gitlab runner needs to have them defined in before_script to work
  sudo apt-get update -y
  sudo apt-get install python-dev -y
  sudo apt-get install -y git make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils
  sudo apt-get install -y libpq-dev
  cd /vagrant
fi
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
echo 'export PATH="~/.pyenv/bin:$PATH"' > ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
echo 'export LC_ALL=en_US.utf-8' >> ~/.bash_profile
. ~/.bash_profile
pyenv install 3.6.0
pyenv virtualenv 3.6.0 wedding
echo 'pyenv activate wedding' >> ~/.bash_profile
pyenv activate wedding
pip install --upgrade pip
pip install -r requirements.txt
