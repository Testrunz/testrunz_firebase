const User = require("../models/Users");
//get (read)
const read = (req, res, next) => {
  const userID = req.params.id;
  res.cookie("Id", req.params.id);
  User.findById(userID)
    .exec()
    .then((user) => {
      if (!user) return res.status(400).json({ error: "user not found" });

      const {
        role,
        _id,
        name,
        email,
        createdAt,
        updatedAt,
        designation,
        showOnce,
        collegeName,
        department,
        country,
        state,
        year,
        semester,
      } = user;
      res.cookie("role", role);
      res.cookie("userId", _id);
      res.cookie("name", name);
      res.cookie("email", email);
      res.cookie("designation", designation);
      res.cookie("showOnce", showOnce);
      res.cookie("collegeName", collegeName);
      res.cookie("department", department);
      res.cookie("createdAt", createdAt);
      res.cookie("updatedAt", updatedAt);
      res.cookie("country", country);
      res.cookie("state", state);
      return res.json({
        role,
        _id,
        name,
        email,
        createdAt,
        updatedAt,
        designation,
        showOnce,
        collegeName,
        state,
        country,
        department,
        year,
        semester,
      });
    })
    .catch((error) => {
      if (error) return res.status(400).json({ error: error });
    });
};
// update
const update = (req, res, next) => {
  console.log(req.body)
  const {
    designation,
    collegeName,
    department,
    country,
    state,
    year,
    semester,
    name,
    password,
    _id,
    showOnce,
  } = req.body;
   User.findOne({ _id: _id })
    .then((user) => {
      if (!user) return res.status(400).json({ error: "user not found" });
      user.name = name || user.name;

      if (password) {
        if (password.length < 6) {
          return res
            .status(400)
            .json({ error: "password should be min 6 long" });
        } else {
          user.password = password;
        }
      }
      if (designation) {
        user.designation = designation;
      }
      if (showOnce) {
        user.showOnce = showOnce;
      }
      if (collegeName) {
        user.collegeName = collegeName;
      }
      if (department) {
        user.department = department;
      }
      if (country) {
        user.country = country;
      }
      if (state) {
        user.state = state;
      }
      if (year) {
        user.year = year;
      }
      if (semester) {
        user.semester = semester;
      }
      user
        .save()
        .then((updated) => {
          console.log(updated)
          return res.json({ updated });
        })
        .catch((err) => {
          return res.status(400).json(err);
        });
    })
    .catch((error) => {
      return res.status(400).json(error);
    });
};



module.exports = { read, update };
