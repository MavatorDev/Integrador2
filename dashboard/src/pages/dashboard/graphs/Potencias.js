import React, { Component } from 'react';
import Chartconfigactual from './Chartconfigactual';
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';

class Potencias extends Component {

    constructor(props) {
        super(props);

        this.state = {
            potBomba1: "66",
            potBomba2: "50",
            potBomba3: "12",
            potBomba4: "60",
        }
    }

    render() {
        return (
            <Grid container spacing={3}>
                <Grid item xs={3} md={3} lg={3}>
                    <Paper>
                        <React.Fragment>
                            <Chartconfigactual titulo="Bomba de frío 1" potencia={this.state.potBomba1} colorBomba="#0093FF" />
                        </React.Fragment>
                    </Paper>
                </Grid>
                <Grid item xs={3} md={3} lg={3}>
                    <Paper>
                        <React.Fragment>
                            <Chartconfigactual titulo="Bomba de frío 2" potencia={this.state.potBomba2} colorBomba="#0093FF" />
                        </React.Fragment>
                    </Paper>
                </Grid>
                <Grid item xs={3} md={3} lg={3}>
                    <Paper>
                        <React.Fragment>
                            <Chartconfigactual titulo="Bomba de calor 1" potencia={this.state.potBomba3} colorBomba="#FFC900" />
                        </React.Fragment>
                    </Paper>
                </Grid>
                <Grid item xs={3} md={3} lg={3}>
                    <Paper >
                        <React.Fragment>
                            <Chartconfigactual titulo="Bomba de calor 2" potencia={this.state.potBomba4} colorBomba="#FFC900" />
                        </React.Fragment>
                    </Paper>
                </Grid>
            </Grid>
        )
    }
}

export default Potencias;
