const MetaInfo = require("../models/MetaInfo");

const postInfo = function (req, res, next) {
  const newMetaInfo = new MetaInfo({
    id: req.body.experimentno,
    ProcedureName: req.body.experiment,
    labtype: req.body.lab,
    department: req.body.department,
    year: req.body.year,
    college: req.body.college,
  });
  newMetaInfo
    .save()
    .then((content) => res.json(content))
    .catch((err) => console.error(err));
};

const patchById = async (req, res) => {
  try {
    const modifiedMetaInfo = await MetaInfo.findOneAndUpdate(
      { id: req.params._id },
      {
        $set: {
          ProcedureName: req.body.experiment,
          labtype: req.body.lab,
          department: req.body.department,
          year: req.body.year,
          college: req.body.college,
        },
      },
      { new: true }
    );
    res.json(modifiedMetaInfo);
  } catch (err) {
    console.error(err);
  }
};

const getById = async function (req, res, next) {
  try {
    const meta = await MetaInfo.findOne({ id: req.params._id });
    res.json(meta);
  } catch (err) {
    console.error(err);
  }
};

const getInfo = async function (req, res, next) {
  try {
    const metas = await MetaInfo.find();

    res.json({ data: metas, totalCount: metas.length });
  } catch (err) {
    console.error(err);
  }
};

module.exports = { postInfo, patchById, getById, getInfo };
