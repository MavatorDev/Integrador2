const { Schema, model } = require('mongoose');
const bcrypt = require('bcryptjs');

const userSchema = new Schema({
    username: String,
    password: String
});

userSchema.methods.encryptPassword = async (password) => {
    const salt = await bcrypt.genSalt(10);
    return bcrypt.hash(password, salt);
};

//se utiliza como 'function' para poder traer la password del usuario
userSchema.methods.validatePassword = function (tryPassword) {
    return bcrypt.compare(tryPassword, this.password);
};

module.exports = model('User', userSchema);