# Seestan
Aristotle: “Art completes what nature cannot bring to finish. The artist gives us knowledge of nature's unrealized ends.”  

## Cart Features

* Stock avalibility
* Is the product already added to card  
* Quantity adjustment before checkout
* Product preference (Size, Color, ...)
* Coupon & Discount
* Save the card locally for faster response
* Save cart in db for price calculation
* Shipment details before proceeding to payment
* Create new order when product is purchased


## Prerequisites
[Data Base Schema](https://drawsql.app/dazain/diagrams/artworks-ecommerce)


### 1- install [Node](https://nodejs.org/), [Python](https://www.python.org/downloads/)

### 2- Environment

- Linux
```
$ sudo apt update
$ sudo apt install python3-pip
$ npm install --global yarn
$ pip3 install virtualenv
```

- Windows:

1- Install [pip3](https://stackoverflow.com/questions/41501636/how-to-install-pip3-on-windows)

2- Run these commands:
```
$ npm install --global yarn
$ pip3 install virtualenv
```

### 3- pull from git to your computer
```
$ cd Desktop/
$ mkdir <folder>
$ cd <folder>/
$ git init
$ git pull https://github.com/ehsan-g/dazain.git
```


## Installing
 **Start back-end locally**
```
$ cd Seestan/
$ source myenv/bin/activate
$ cd backend/
$ pip3 install -r requirements.txt
$ python3 manage.py runserver
```
**Start front-end locally**
```
$ cd client/
$ yarn install 
$ yarn start
```

## Routes
```http://127.0.0.1:8000/routes/```

## Running the tests

...

### Break down into end to end tests

...

## Deployment

...


## Built With

Django - React - Postgres - Material UI


## Versioning

We use [SemVer](http://semver.org/) for versioning.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


