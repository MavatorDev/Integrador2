import React, {Component} from 'react';
import {Doughnut} from 'react-chartjs-2';

class Chartconfigactual extends Component{

    constructor(props){
        super(props);
        let colorBomba = '#77FF33';

        if(this.props.colorBomba != null){
            colorBomba = this.props.colorBomba;
        }

        this.state = {
            chartData:{
                labels: [
                    'Potencia actual (%)'
                ],
                datasets: [{
                    data: [this.props.potencia, 100 - this.props.potencia ],
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

    render(){
        return (
            <div className="chart">
                <h3> {this.props.titulo}</h3>
                <Doughnut 
                    data={this.state.chartData}
                    width={150}
                    height={150}
                    options={{
                        maintainAspectRatio:false,
                        cutoutPercentage: 80
                    }}
                />
                <h2> Potencia al {this.props.potencia}% </h2>
            </div>
        )
    }
}

export default Chartconfigactual;
