import React, { Component } from 'react';
import { HorizontalBar } from 'react-chartjs-2';
import axios from 'axios';

class Chartzonastemp extends Component {

    constructor(props) {
        super(props);

        this.state = {
            chartData: {
                labels: [
                    'CIII Ambulatory', 'CIII 8, stall&Galleries', 'FV 8, stall&Galleries', 'FV Foyer',
                    'FV 7, amphitheater', 'Hall Goya', 'FV Hall', 'FV Orchestra', 'CIII 7, amphitheater',
                    'FV 7, amphitheater', 'FV Ambulatory', 'FV Ambulatory', 'CIII 8, stall&Galleries',
                    'FV 8, stall&Galleries', 'z_Tr_AmbC', 'z_Tr_HalSAPAF', 'z_Tr_OrchReheF', 'z_Tr_Sng4',
                    'z_TRet_Bllt', 'z_TRet_Choir', 'z_TRet_CrcC', 'z_TRet_CrcF', 'z_TRet_Hal6F', 'z_TRet_OffiF',
                    'z_TRet_R14', 'z_TRet_Store', 'z_TRet_Tech',
                    ''
                ],
                datasets: [
                    {
                        label: 'Temperatura (°C)',
                        backgroundColor: '#5CE0FF',
                        borderColor: '#5CE0FF',
                        borderWidth: 1,
                        hoverBackgroundColor: '#3BFF3E',
                        hoverBorderColor: '#000000',
                        data: []
                    }
                ]
            }
        }
    }

    componentDidMount() {
        var zoneTemps;

        axios.get('http://54.90.124.184:8000/api/temperatures/')
            .then(res => {

                zoneTemps = [
                    res.data['s_Tr_AmbC'], res.data['s_Tr_CrcC'], res.data['s_Tr_CrcF'], res.data['s_Tr_FyrF'],
                    res.data['s_Tr_GdF'], res.data['s_Tr_GoyaF'], res.data['s_Tr_Hal1F'], res.data['s_Tr_PitF'],
                    res.data['s_Tr_StdsC'], res.data['s_Tr_StdsF'], res.data['s_TRet_AmbF'], res.data['s_TRet_StllC'],
                    res.data['s_TRet_StllF'], res.data['z_Tr_AmbC'], res.data['z_Tr_GyrreC'], res.data['z_Tr_HalSAPAF'],
                    res.data['z_Tr_OrchReheF'], res.data['z_Tr_Sng4'], res.data['z_TRet_Bllt'], res.data['z_TRet_Choir'],
                    res.data['z_TRet_CrcC'], res.data['z_TRet_CrcF'], res.data['z_TRet_Hal6F'], res.data['z_TRet_OffiF'],
                    res.data['z_TRet_R14'], res.data['z_TRet_Store'], res.data['z_TRet_Tech'],
                    0
                ];

                this.setState({
                    chartData: {
                        datasets: [
                            {
                                label: 'Temperatura (°C)',
                                backgroundColor: '#5CE0FF',
                                borderColor: '#5CE0FF',
                                borderWidth: 1,
                                hoverBackgroundColor: '#3BFF3E',
                                hoverBorderColor: '#000000',
                                data: zoneTemps
                            }
                        ]
                    }
                });
            });
    }

    render() {
        return (
            <div className="chart">
                <h2>Temperatura de las zonas del teatro</h2>
                <HorizontalBar data={this.state.chartData} />
            </div>
        )
    }
}

export default Chartzonastemp;
