const { v4: uuidv4 } = require("uuid");

// load user model
const User = require("../models/Experiments");

// load validator
const validateRegisterInput = require("../validation/register");

const getExpAllUser = async function (req, res, next) {
  try {
    const users = await User.find();
    /* 
      // filter in server
      const newUsers = users.map(
        ({ runID, studentName, labType, experimentName }) => ({
          runID,
          studentName,
          labType,
          experimentName,
        })
      ); */
    //console.log(newUsers);
    res.json({ data: users, totalCount: users.length });
  } catch (err) {
    console.error(err);
  }
};

const getSingleUser = async function (req, res, next) {
  try {
    const user = await User.findOne({ _id: req.params._id });
    // console.log("hello",user)
     res.json(user);
  } catch (err) {
    console.error(err);
  }
};

const postUser = (req, res, next) => {
  console.log(req.body)
  const { errors, isValid } = validateRegisterInput(req.body);

  // check validation
  if (!isValid) {
    return res.status(400).json(errors);
  }

  //User.findOne()
  const newUser = new User({
    runID: uuidv4(),
    studentName: req.body.studentName,
    procedureDescription: req.body.procedureDescription,
    labType: req.body.labType,
    experimentName: req.body.experimentName,
    userid: req.body.userId
  });
  newUser
    .save()
    .then((user) => res.json(user))
    .catch((err) => console.error(err));
};

const patchUser = async (req, res) => {
  console.log("PATCH", req.params._id)
  try {
    const updatedUser = await User.findByIdAndUpdate(
      { _id: req.params._id },
      {
        $set: {
          studentName: req.body.studentName,
          procedureDescription: req.body.procedureDescription,
          labType: req.body.labType,
          experimentName: req.body.experimentName,
        },
      }
    );
    res.json(updatedUser);
  } catch (err) {
    console.error(err);
  }
};

// add data to experiments
const patchUser1 = async (req, res) => {
  const {id, ...other} = req.body;
  console.log("PATCH", other)
   try {
    const updatedUser = await User.findByIdAndUpdate(
      { _id: id },
      {
        $set: {
          datas: other,
          
        },
      }
    );
    res.json(updatedUser);
  } catch (err) {
    console.error(err);
  } 

};


const deleteUser = async (req, res) => {
  try {
    const removedUser = await User.remove({ _id: req.params._id });
    res.json(removedUser);
  } catch (err) {
    console.error(err);
  }
};

module.exports = {
  getExpAllUser,
  getSingleUser,
  postUser,
  patchUser,
  patchUser1,
  deleteUser,
};
