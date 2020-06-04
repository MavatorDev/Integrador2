const express = require('express');
const morgan = require('morgan');
const cors = require('cors');
const app = express();

const { mongoose } = require('./database');

// Settings
app.set('port', process.env.PORT || 5000);

// Middlewares
app.use(morgan('dev'));
app.use(express.json());
app.use(cors({origin: 'http://localhost:3000'}));

//Routes
app.use(require('./routes/routes'));

// Starting the server

app.listen(5000, () => {
    console.log('Server on port',app.get('port'));
});