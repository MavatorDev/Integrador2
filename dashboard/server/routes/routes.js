const express = require('express');
const router = express.Router();
const user = require('../controllers/usuario.controller');

//Usuarios
router.post('/registerADMT', user.createUser);
router.post('/login', user.userLogin);

module.exports = router;