import React from 'react';
import Title from '../Title';
import Button from '@material-ui/core/Button';
import PlayArrowIcon from '@material-ui/icons/PlayArrow';
import TextField from '@material-ui/core/TextField';
import axios from 'axios';

export default function Buttons2() {
    const [varEntrada, setVarEntrada] = React.useState('0.0');

    const handleChangeVarEntrada = (event) => {
        setVarEntrada(event.target.value);
    };

    const handleClick = (event) => {
        console.log("Se ha iniciado el modelo con valor: "+varEntrada);
        
        axios.post('http://localhost:8000/api/start/', {varEntrada})
        .then(res=> {
            console.log(res.data);
        });

    };

    return (
        <React.Fragment>
            <Title> Iniciar ejecución del modelo </Title>

            <form autoComplete="off">
                <TextField
                    id="varEntrada"
                    label="Valor de entrada"
                    type="number"
                    value={varEntrada}
                    onChange={handleChangeVarEntrada}
                />
            </form>
            <br />
            <Button
                variant="contained"
                color="primary"
                startIcon={<PlayArrowIcon />}
                onClick={handleClick}
            >
                Iniciar modelo
            </Button>
        </React.Fragment>
    );
}
