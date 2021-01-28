%%bash 
git clone https://github.com/ferencberes/kaggle-import-test.git
%%bash
cd kaggle-import-test
pip install .
from dummytest.print_hello import hello
hello('Dávid!')
