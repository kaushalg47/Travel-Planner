const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const ejs = require('ejs');
const session = require("express-session");
const{v4:uuidv4}=require("uuid");

const router=require

const app = express();
const PORT = 5000;


app.set('view engine', 'ejs');
app.use(bodyParser.json())

app.use(express.static(__dirname + '/public'));
app.use(bodyParser.urlencoded({extended: true}));

app.use(session({
    secret:uuidv4(),
    resave:false,
    saveUninitialized:true
}))

app.get('/', (req, res)=>{

    res.render("home");
})
app.get('/login', (req, res)=>{

    res.render("login");
})
app.get('/contact', (req, res)=>{

  res.render("contactus");
})





mongoose.connect('mongodb+srv://vishwajeettiwari2003:qbGI7RAikkaFtZ8Y@cluster0.mj2hk8s.mongodb.net/?retryWrites=true&w=majority', {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(console.log("database connected"));

const userSchema = mongoose.Schema({
    username: String,
    password: String
})
const contactSchema = mongoose.Schema({
  username: String,
  email: String,
  mob: String,
 

})

const User = mongoose.model('user', userSchema);
const contact = mongoose.model('contact', contactSchema);



 app.post('/login', (req, res)=>{
    const username = req.body.username;
   const password = req.body.password;
   const newUser = new User({
       username, password
     })
     newUser.save().then(()=>{
         res.redirect('/')
     })
 })
 app.post('/contact', (req, res)=>{
  const username = req.body.username;
 const email = req.body.email;
 const mob = req.body.mob;
 
 const newContact = new contact({
     username, email, mob
   })
   newContact.save().then(()=>{
       res.redirect('/')
   })
})





 app.use('/route', router );



app.listen(PORT, ()=>{
    console.log('Port is running on http://localhost:5000');
})

