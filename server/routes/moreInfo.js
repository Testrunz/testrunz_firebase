const router = require("express").Router();
const {
  postInfo,
  patchById,
  getById,
  getInfo,
} = require("../controllers/moreInfoController");

router.post("/", postInfo);

router.patch("/:_id", patchById);

router.get("/:_id", getById);

router.get("/", getInfo);

module.exports = router;
