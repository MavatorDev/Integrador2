import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Title from '../Title';
import Button from '@material-ui/core/Button';
import StopIcon from '@material-ui/icons/Stop';
import ReplayIcon from '@material-ui/icons/Replay';
import axios from 'axios';

const useStyles = makeStyles({
  depositContext: {
    flex: 1,
  },
});

export default function Buttons1() {
  const classes = useStyles();

  const handleClickStop = (event) => {
    console.log("Deteniendo modelo...");

    axios.get('http://54.90.124.184:8000/api/stop');

  }
  
  const handleClickRestart = (event) => {
    console.log("Reiniciando modelo...");

    axios.get('http://54.90.124.184:8000/api/restart');

  }

  return (
    <React.Fragment>
      <Title> Modelo en ejecución </Title>
      <br/>
      <Button
        variant="contained"
        color="secondary"
        className={classes.button}
        startIcon={<StopIcon />}
        onClick={handleClickStop}
      >
        Detener ejecución
      </Button>
      <br/>
      <br/>
      <Button
        variant="contained"
        color="primary"
        className={classes.button}
        startIcon={<ReplayIcon />}
        onClick={handleClickRestart}
      >
        Reiniciar modelo
      </Button>
    </React.Fragment>
  );
}
