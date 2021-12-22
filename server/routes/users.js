const router = require("express").Router();
const usersController = require("../controllers/users");
const authController = require("../controllers/auth");

router.get("/users/:id",  usersController.read);
router.patch(
  "/users/update",
  usersController.update
);
router.patch(
  "/admin/update",

  authController.adminMiddleware,
  usersController.update
);


module.exports = router;
