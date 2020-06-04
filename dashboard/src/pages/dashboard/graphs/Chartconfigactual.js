import React, { Component } from 'react';
import { Doughnut } from 'react-chartjs-2';
import axios from 'axios';

class Chartconfigactual extends Component {

    constructor(props) {
        super(props);
        let colorBomba = '#77FF33';

        if (this.props.colorBomba != null) {
            colorBomba = this.props.colorBomba;
        }

        this.state = {
            chartData: {
                labels: [
                    'Potencia actual (%)'
                ],
                datasets: [{
                    data: [100, 100 - 100],
                    backgroundColor: [
                        colorBomba,
                        '#CBCBCB'
                    ],
                    hoverBackgroundColor: [
                        colorBomba,
                        '#CBCBCB'
                    ]
                }]
            }
        }
    }

    componentDidMount() {

        axios.get('http://54.90.124.184:8000/api/solutions/')
            .then(res => {

                if(this.props.bomba == "bomb1"){
                    this.setState({
                        chartData: {
                            datasets: [{
                                data: [res.data.bomba1, 100 - res.data.bomba1]
                            }]
                        }
                    });
                }else if(this.props.bomba == "bomb2"){
                    this.setState({
                        chartData: {
                            datasets: [{
                                data: [res.data.bomba2, 100 - res.data.bomba2]
                            }]
                        }
                    });
                }else if(this.props.bomba == "bomb3"){
                    this.setState({
                        chartData: {
                            datasets: [{
                                data: [res.data.bomba3, 100 - res.data.bomba3]
                            }]
                        }
                    });
                }else if(this.props.bomba == "bomb4"){
                    this.setState({
                        chartData: {
                            datasets: [{
                                data: [res.data.bomba4, 100 - res.data.bomba4]
                            }]
                        }
                    });
                }

            });
    }

    render() {
        const potencia = this.state.chartData.datasets[0].data[0];
        return (
            <div className="chart">
                <h3> {this.props.titulo}</h3>
                <Doughnut
                    data={this.state.chartData}
                    width={150}
                    height={150}
                    options={{
                        maintainAspectRatio: false,
                        cutoutPercentage: 80
                    }}
                />
                <h2> Potencia al {potencia}% </h2>
            </div>
        )
    }
}

export default Chartconfigactual;
