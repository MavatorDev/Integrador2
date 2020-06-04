const mongoose = require('mongoose');
const db = 'mongodb://localhost/dbteatro'

mongoose.connect(db, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
    .then(db => console.log('DB is coneccted'))
    .catch(err => console.error(err));

module.exports = mongoose;