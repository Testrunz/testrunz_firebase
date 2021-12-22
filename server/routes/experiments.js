const express = require("express");
const router = express.Router();

const {
  getExpAllUser,
  getSingleUser,
  postUser,
  patchUser,
  patchUser1,
  deleteUser,
  
} = require("../controllers/experimentController");

// @route GET all /users
// @desc a get req for users routes
// @access public
router.get("/", getExpAllUser);

// @route GET single /users/<>
// @desc a get req for users routes
// @access public
router.get("/:_id", getSingleUser);

// @route POST /users/create
// @desc a POST req for users registeration
// @access public
router.post("/", postUser);

// @route PATCH /users/update/<>
// @desc a PATCH req for users registeration
// @access public
router.patch("/:_id", patchUser);

router.patch("/", patchUser1);

// @route Delete /users/delete
// @desc a PATCH req for users registeration
// @access public
router.delete("/:_id", deleteUser);
module.exports = router;
