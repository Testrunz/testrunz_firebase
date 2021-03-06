const router = require("express").Router();
const authController = require("../controllers/auth");

router.post( "/login", authController.authAccountlogin);
router.post("/register", authController.authAccountregister);

router.post("/google_login", authController.googleLogin);
router.delete("/deleteuser", authController.deleteuser);

module.exports = router;
