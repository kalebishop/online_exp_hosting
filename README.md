# online_exp_hosting

## 0. setup

Clone this repo:
`git clone --recursive https://github.com/kalebishop/online_exp_hosting.git`

Start up a python venv (ideally using python3.9) and install the prereqs:
`python3.9 -m venv venv && source venv/bin/activate`
`pip install -r requirements.txt`

In the background, get the Docker image for overcooked running (It's a surprise tool that'll help us later)
`cd 3_overcooked && ./up.sh`
(You can ctrl-C this once the container is built)