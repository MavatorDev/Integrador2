import React, { Component } from 'react';
import Chartconfigactual from './Chartconfigactual';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import axios from 'axios';

class Potencias extends Component {

    constructor(props) {
        super(props);

        this.state = {
        }
            
    }

    render() {
        return (
            <Grid container spacing={3}>
                <Grid item xs={3} md={3} lg={3}>
                    <Paper>
                        <React.Fragment>
                            <Chartconfigactual titulo="Bomba de frío 1" bomba={"bomb1"} colorBomba="#0093FF" />
                        </React.Fragment>
                    </Paper>
                </Grid>
                <Grid item xs={3} md={3} lg={3}>
                    <Paper>
                        <React.Fragment>
                            <Chartconfigactual titulo="Bomba de frío 2" bomba={"bomb2"} colorBomba="#0093FF" />
                        </React.Fragment>
                    </Paper>
                </Grid>
                <Grid item xs={3} md={3} lg={3}>
                    <Paper>
                        <React.Fragment>
                            <Chartconfigactual titulo="Bomba de calor 1" bomba={"bomb3"} colorBomba="#FFC900" />
                        </React.Fragment>
                    </Paper>
                </Grid>
                <Grid item xs={3} md={3} lg={3}>
                    <Paper >
                        <React.Fragment>
                            <Chartconfigactual titulo="Bomba de calor 2" bomba={"bomb4"} colorBomba="#FFC900" />
                        </React.Fragment>
                    </Paper>
                </Grid>
            </Grid>
        )
    }
}

export default Potencias;
