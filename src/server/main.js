const express = require('express');
const app = express();
const path = require('path');
const home = require('./router/home');
const remotecontrol = require('./router/remotecontrol');
const port = 3000;

app.use(express.json()); 
app.use(express.urlencoded({ extended: true })); 

app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
  next();
});

app.set('view engine', 'html'); 
app.set('views', path.join(__dirname, './html')); 
app.use(express.static(path.join(__dirname, './public')));
app.use(express.static(path.join(__dirname, './html')));

app.get('/', (req, res) => {
    res.redirect('/Home');
});

home(app,path)
remotecontrol(app,path)


app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}/`);
});