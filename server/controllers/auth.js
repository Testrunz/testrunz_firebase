const User = require("../models/Users");
const Experiment = require("../models/Experiments");
const jwt = require("jsonwebtoken");
const _ = require("lodash");
const expressJWT = require("express-jwt");
const { OAuth2Client } = require("google-auth-library");
const fetch = require("node-fetch");
require("dotenv").config();





const authAccountregister = (req, res) => {
  //const { token } = req.body;
  console.log(req.body)
    
    User.create({
        email : req.body.email,
        name : req.body.name
      }).then((user)=>{
        console.log(user.json())
       return res.json({status:"ok"})
      })
    .catch((err)=>{
    return  res.json({status:err})
    })
      
   
  
};

const authAccountlogin = (req, res, next) => {
  const email  = req.body.email;
  User.findOne({ email })
    .exec()
    .then((user) => {
      const { _id, email, role } = user;
      return res.json({
        user: { _id, email, role },
      });
    })
    .catch((error) => {
      return res.status(400).json({ error: "User with that email not exits" });
    });
};

const adminMiddleware = (req, res, next) => {
  User.findById(req.user._id)
    .exec()
    .then((user) => {
      if (!user)
        return res
          .status(400)
          .json({ error: "User with this email does'nt exits" });
      if (user.role !== "admin") {
        return res.status(400).json({ error: "Admin resource access denied" });
      }
      req.profile = user;
      next();
    })
    .catch((error) => {
      return res.status(400).json({ error });
    });
};





      
const googleLogin = (req, res, next) => {
  const email  = req.body.email;
        User.findOne({ email })
          .exec()
          .then((user) => {


            if (!user) {
              User.create({
                email : req.body.email,
                name : req.body.name
              }).then((user)=>{
                const { _id, email,name, role, designation} = user;
                console.log(_id,email,name)
                res.json({
                  user: { _id, email, name, role, designation },
                });
              })
            }
          else {
              const { _id, email, name, role, designation } = user;
              res.json({
                user: { _id, email, name, role, designation },
              });
            }
          })
        
};

const deleteuser=(req, res, next)=>{
  const userid  = req.body.userid;
  console.log(userid)
  Experiment.deleteMany({userid:userid})
  .then(()=>{
    console.log("experiments Deleted")
    User.deleteMany({_id:userid})
    .then((user)=>{
      console.log("user deleted")
      res.json({
        detail: "user Deleted",
      });
      });
    });

    
  
}



module.exports = {
  authAccountregister,
  authAccountlogin,
  adminMiddleware,
  googleLogin,
  deleteuser
};
